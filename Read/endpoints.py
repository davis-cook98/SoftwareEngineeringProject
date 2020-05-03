import pymongo
from pymongo import MongoClient
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
@app.route('/ReadAPI/')
def getSingleArticle():
    title = request.args.get('title')
    return get_article(title)

@app.route('/ReadAPI')
def getAllArticles(title):
    return get_articles(title)


#definitions
def get_article2():
    return ArticleSchema().dump(ArtRepo.find_one())

def get_article(title):
    query = re.compile("^" + title, re.IGNORECASE)
    return ArticleSchema().dump(ArtRepo.find_one({"Title": query}))
    

def get_articles(title):
    for article in ArtRepo.find({"title" : title}):
        return article