import pymongo
from pymongo import MongoClient
from pymongo import ReturnDocument
from .middlewares import login_required
from flask import Flask, json, g, request
from .Schemas import ArticleSchema
from flask_cors import CORS
from flask import request
import re


#Connect to DB
client = MongoClient('localhost', 27017)
db = client.SoftwareEngineering 
ArtRepo = db.ArtRepo

app = Flask(__name__)
CORS(app)

#decorators
@login_required
@app.route('/WriteAPI/addFavorite/', methods = ['GET', 'POST'])
def addFavorite():
    title = request.args.get('title')
    name = request.args.get('name')
    return add_favorite(name, title)

@login_required
@app.route('/WriteAPI/removeFavorite/', methods = ['GET', 'POST'])
def removeFavorite():
    title = request.args.get('title')
    name = request.args.get('name')
    return remove_favorite(name, title)



#definitions
def add_favorite(name, title):
    query = re.compile("^" + title, re.IGNORECASE)
    whoFavorited = ArticleSchema().dump(ArtRepo.find_one({"Title": query}))["favorited"]
    newFavorites = whoFavorited + " " + name
    return ArticleSchema().dump(ArtRepo.find_one_and_update({"Title": query}, {'$set': {'favorited': newFavorites}}, return_document=ReturnDocument.AFTER))

def remove_favorite(name, title):
    query = re.compile("^" + title, re.IGNORECASE)
    whoFavorited = ArticleSchema().dump(ArtRepo.find_one({"Title": query}))["favorited"]
    if name in whoFavorited:
        newFavorites = whoFavorited.replace(name, "")
        newFavorites = ' '.join(newFavorites.split())
        return ArticleSchema().dump(ArtRepo.find_one_and_update({"Title": query}, {'$set' : {'favorited': newFavorites}}, return_document=ReturnDocument.AFTER))
    else:
        return "User not favorited"