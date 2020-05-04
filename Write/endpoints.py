import pymongo
from pymongo import MongoClient
from pymongo import ReturnDocument
from .middlewares import login_required
from flask import Flask, json, g, request
from .Schemas import ArticleSchema, UserSchema
from flask_cors import CORS
from flask import request
import re

#Connect to DB
client = MongoClient('localhost', 27017)
db = client.SoftwareEngineering
ArtRepo = db.ArtRepo
UserRepo = db.UserRepo

write = Flask(__name__)
CORS(write)

#decorators
@write.route('/addUser/', methods = ['GET', 'POST'])
def addUser():
    username = request.args.get('username')
    password = request.args.get('password')
    return add_User(username, password)

@login_required
@write.route('/toggleFavorite/', methods = ['GET', 'POST'])
def toggleFavorite():
    title = request.args.get('title')
    name = request.args.get('name')
    return toggle_favorite(name, title)


#definitions
def add_User(uname, pword):
    cleanName = re.compile("^" + uname, re.IGNORECASE)
    if UserRepo.find_one({"Username": cleanName}) is None:
        UserRepo.insert_one({"Username": uname, "Password": pword, "Favorites": []})
        return "User has been created, welcome"
    else:
        return "Username in use, please choose another one"

def toggle_favorite(uname, title):
    query = re.compile("^" + title, re.IGNORECASE)
    artId = ArtRepo.find_one({"Title": query})["_id"]
    userFavs = UserSchema().dump(UserRepo.find_one({"Username": uname}))["Favorites"]
    if str(artId) in userFavs:
        userFavs.remove(str(artId))
        UserRepo.find_one_and_update({"Username": uname}, {"$set": {"Favorites": userFavs}}, return_document=ReturnDocument.AFTER)
        return("Article unfavorited")
    else:
        userFavs.append(artId)
        UserSchema().dump(UserRepo.find_one_and_update({"Username": uname}, {"$set": {"Favorites": userFavs}}, return_document=ReturnDocument.AFTER))
        return("Article favorited")

if __name__ == "__main__":
    write.run()
