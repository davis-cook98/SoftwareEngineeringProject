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
@app.route('/')
@login_required
@app.route('/WriteAPI/addFavorite/', methods = ['GET', 'POST'])
def addFavorite(name, title):
    title = request.args.get('title')
    return add_favorite(name, title)

@app.route('/WriteAPI/removeFavorite/', methods = ['GET', 'POST'])
def removeFavorite(name, title):
    title = request.args.get('title')
    return remove_favorite(name, title)



#definitions
def add_favorite(name, title):
    query = re.compile("^" + title, re.IGNORECASE)
    whoFavorited = ArticleSchema().dump(ArtRepo.find_one({"Title": query}))["favorited"]
    newFavorites = whoFavorited + " " + name
    return ArticleSchema().dump(ArtRepo.find_one_and_update({"Title": query}, {'favorited': newFavorites}, return_document=ReturnDocument.AFTER))

def remove_favorite(name, title):
    query = re.compile("^" + title, re.IGNORECASE)
    whoFavorited = ArticleSchema().dump(ArtRepo.find_one({"Title": query}))["favorited"]
    if name in whoFavorited:
        newFavorites = whoFavorited.replace(name, "")
        newFavorites = ' '.join(newFavorites.split())
        return ArticleSchema().dump(ArtRepo.find_one_and_update({"Title": query}, {'favorited': newFavorites}, return_document=ReturnDocument.AFTER))
    else:
        return "User not favorited"