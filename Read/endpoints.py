import pymongo
from pymongo import MongoClient
from .middlewares import login_required
from flask import Flask, json, g, request
from .Schemas import UserSchema, ArticleSchema
from .ReadMongo import ReadConnect as Read
from flask_cors import CORS

#Connect to DB
client = MongoClient('localhost', 27017)
db = client.SoftwareEngineering 
ArtRepo = db.ArtRepo

app = Flask(__name__)
CORS(app)

#decorators
@app.route('/')
@app.route('/ReadAPI')
def getSingleArticle():
    return get_article("college")

@app.route('/ReadAPI')
def getAllArticles(title):
    return get_articles(title)


#definitions
def get_article(title):
    return (ArtRepo.find_one({"title" : title}))
    

def get_articles(title):
    for article in ArtRepo.find({"title" : title}):
        return article