import pymongo
from pymongo import MongoClient
from flask import Flask, json, jsonify, g, request, render_template
from flask_bcrypt import Bcrypt 
from flask_jwt_extended import JWTManager 
from flask_jwt_extended import create_access_token
from .Schemas import ArticleSchema
from flask_cors import CORS
from bson.objectid import ObjectId
import re



#Connect to DB
client = MongoClient('localhost', 27017)
db = client.SoftwareEngineering
ArtRepo = db.ArtRepo
UserRepo = db.UserRepo

#Setup Flask app
read = Flask(__name__)
CORS(read)
# Setup encrpytion
bcrypt = Bcrypt(read)
jwt = JWTManager(read)
with open("client_secret.json") as f:
    data = json.load(f)
    read.config['JWT_SECRET_KEY']  = data["secretKey"]

#3 dummy articles for missing data
NoFavorites =[{"Title":"Looks like you don't have any favorites",
               "Description": "You should add some (when we let you)",
               "Published": "",
               "InsertTime":"",
               "URL":"http://localhost:8080/"
}]

NoPushed =[{"Title":"Looks like we haven't pushed any articles",
            "Description": "We'll do that soon",
            "Published": "",
            "InsertTime":"",
            "URL":"http://localhost:8080/"
}]

NoSearch =[{"Title":"Looks like we haven't loaded any articles with those criteria",
            "Description": "Please try again",
            "Published": "",
            "InsertTime":"",
            "URL":"http://localhost:8080/search"
}]

#decorators

#Our search function on a custom text index
@read.route('/ReadAPI/search/')
def search():
    param = request.args.get('param')
    return search_func(param)

#Get a single article baesd on a given criteria
@read.route('/ReadAPI/getOne/')
def getSingleArticle():
    title = request.args.get('title')
    return get_article(title)

#Get all articles based on a given title
@read.route('/ReadAPI/getAll/')
def getAllArticles():
    title = request.args.get('title')
    return get_articles(title)

#Get all of the favorites for a user
@read.route('/ReadAPI/getFavorites/')
def getFavorites():
    uname = request.args.get('username')
    return get_Favorites(uname)

#Get all pushed articles
@read.route('/ReadAPI/getPushed/')
def getPushed():
    uname = request.args.get('username')
    return get_pushed(uname)

#Find a given user based on uname and pword
@read.route('/ReadAPI/findUser/')
def findUser():
    uname = request.args.get('username')
    pword = request.args.get('password')
    return find_User(uname, pword)


#Definitions
#All of the helperfunctions for our routes

def get_article(title):
    query = re.compile("^" + title, re.IGNORECASE)
    return ArticleSchema().dump(ArtRepo.find_one({"Title": query}))

def get_Favorites(uname):
    favArticlesID = []
    if UserRepo.find_one({"Username": uname})["Favorites"] == []:
        return(jsonify(NoFavorites))
    else:
        user = UserRepo.find_one({"Username": uname})
        favArticlesID = user["Favorites"]
    favArticles = []
    for x in favArticlesID:
        favArticles.append(ArtRepo.find_one({"_id": ObjectId(str(x))}))

    results = ArticleSchema().dump(favArticles, many=True)

    return(jsonify(results))

def get_pushed(uname):
    pushArticlesID = []
    if UserRepo.find_one({"Username": uname})["Pushed"] == []:
        return(jsonify(NoPushed))
    else:
        user = UserRepo.find_one({"Username": uname})
        pushArticlesID = user["Pushed"]
    pushArticles = []
    for x in pushArticlesID:
        pushArticles.append(ArtRepo.find_one({"_id": ObjectId(str(x))}))

    results = ArticleSchema().dump(pushArticles, many=True)

    return(jsonify(results))


def find_User(uname, pword):
    response = UserRepo.find_one({"Username": uname})
    if response:
        if bcrypt.check_password_hash(response["Password"], pword):
            jwtToken = create_access_token(identity = {
                "First name" : response["First_name"],
                "Last name" : response["Last_name"],
                "Username" : response["Username"]
            })
            result = jsonify({"Token":jwtToken})
        else:
            result = jsonify({"Error": "Incorrect username or password"})
    else:
        result = jsonify({"Error": "No user found, would you like to register?"})

    return(result)

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

def search_func(param):
    allArticles = []
    if str(param) == "":
        for article in ArtRepo.find({},limit=10):
            allArticles.append(article)
    elif ArtRepo.find_one({"$text": {"$search": param}}) is not None:
        for article in ArtRepo.find({"$text": {"$search": param}}).limit(10):
            allArticles.append(article)
    else:
        return(jsonify(NoSearch))
    
    results = ArticleSchema().dump(allArticles, many=True)

    return(jsonify(results))


if __name__ == "__main__":
    read.run()
