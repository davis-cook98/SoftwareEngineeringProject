import pymongo
from pymongo import MongoClient
from .middlewares import login_required
from flask import Flask, json, jsonify, g, request
from .Schemas import ArticleSchema
from flask_cors import CORS
from flask import request
import re

#Connect to DB
client = MongoClient('localhost', 27017)
db = client.SoftwareEngineering
ArtRepo = db.ArtRepo
UserRepo = db.UserRepo

read = Flask(__name__)
CORS(read)

#decorators
@read.route('/ReadAPI/getOne/')
def getSingleArticle():
    title = request.args.get('title')
    return get_article(title)

@read.route('/ReadAPI/getAll/')
def getAllArticles():
    title = request.args.get('title')
    return get_articles(title)

@read.route('/ReadAPI/findUser/')
def findUser():
    uname = request.args.get('username')
    pword = request.args.get('password')
    return find_User(uname, pword)


#definitions
def get_article2():
    return ArticleSchema().dump(ArtRepo.find_one())

def get_article(title):
    query = re.compile("^" + title, re.IGNORECASE)
    return ArticleSchema().dump(ArtRepo.find_one({"Title": query}))


def find_User(uname, pword):
    username = re.compile("^" + uname, re.IGNORECASE)
    response = UserRepo.find_one({"Username": username, "Password": pword})
    if response is None:
        return "User does not exist"
    else:
        return "True"

    

def get_articles(title):
    allArticles = []
    if str(title) == "":
        for article in ArtRepo.find({},limit=5):
            allArticles.append(article)
    else:
        query = re.compile("^" + title, re.IGNORECASE)
        for article in ArtRepo.find({"Title" : query},limit=5):
            allArticles.append(article)

    results = ArticleSchema().dump(allArticles, many=True)

    return(jsonify(results))



if __name__ == "__main__":
    read.run()
