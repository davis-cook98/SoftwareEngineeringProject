import pymongo
from pymongo import MongoClient
from .middlewares import login_required
from flask import Flask, json, jsonify, g, request, render_template
from .Schemas import ArticleSchema
from flask_cors import CORS
from flask import request
import re

#Connect to DB
client = MongoClient('localhost', 27017)
db = client.SoftwareEngineering 
ArtRepo = db.ArtRepo
read = Flask(__name__)
CORS(read)

#decorators
@read.route('/ReadAPI/search/')
def search():
    param = request.args.get('param')
    allArticles = []
    for article in ArtRepo.find({"$text": {"$search": param}}).limit(10):
        allArticles.append(article)
    
    results = ArticleSchema().dump(allArticles, many=True)

    return(jsonify(results))


@read.route('/ReadAPI/getOne/')
def getSingleArticle():
    title = request.args.get('title')
    return get_article(title)

@read.route('/ReadAPI/getAll/')
def getAllArticles():
    title = request.args.get('title')
    return get_articles(title)


#definitions
def get_article2():
    return ArticleSchema().dump(ArtRepo.find_one())

def get_article(title):
    query = re.compile("^" + title, re.IGNORECASE)
    return ArticleSchema().dump(ArtRepo.find_one({"Title": query}))
    

def get_articles(title):
    allArticles = []
    if str(title) == "":
        for article in ArtRepo.find({},limit=10):
            allArticles.append(article)
    else:
        query = re.compile("^" + title, re.IGNORECASE)
        for article in ArtRepo.find({"Title" : query},limit=5):
            allArticles.append(article)
    
    results = ArticleSchema().dump(allArticles, many=True)

    return(jsonify(results))

if __name__ == "__main__":
    read.run()