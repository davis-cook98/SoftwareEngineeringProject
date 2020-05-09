import pymongo
from pymongo import MongoClient
from pymongo import ReturnDocument
from flask import Flask, json, g, request, jsonify
from flask_bcrypt import Bcrypt 
from flask_jwt_extended import JWTManager 
from flask_jwt_extended import create_access_token
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
bcrypt = Bcrypt(write)
jwt = JWTManager(write)
with open("client_secret.json") as f:
    data = json.load(f)
    write.config['JWT_SECRET_KEY'] = data["secretKey"]

#decorators
@write.route('/addUser/', methods = ['GET', 'POST'])
def addUser():
    username = request.args.get('username')
    password = request.args.get('password')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    return add_User(username, password, first_name, last_name)

@write.route('/toggleFavorite/', methods = ['GET', 'POST'])
def toggleFavorite():
    title = request.args.get('title')
    name = request.args.get('name')
    return toggle_favorite(name, title)

@write.route('/togglePushed/', methods = ['GET', 'POST'])
def togglePushed():
    title = request.args.get('title')
    return toggle_pushed(title)


#definitions
def add_User(uname, pword, fname, lname):
    cleanName = re.compile("^" + uname, re.IGNORECASE)
    password = bcrypt.generate_password_hash(pword).decode("utf-8")
    if UserRepo.find_one({"Username": cleanName}) is None:
        UserRepo.insert_one({"Username": uname, 
                             "Password": password, 
                             "First_name": fname, 
                             "Last_name": lname, 
                             "Favorites": [], 
                             "Pushed": []})
        returnVal = {"Username": str(uname) + " registerd succesfully, welcome"} 
        return (jsonify({"Result": returnVal}))
    else:
        return (jsonify({"Error" : "Username in use, please choose another one"}))

def toggle_pushed(title):
    query = re.compile("^" + title, re.IGNORECASE)
    artId = ArtRepo.find_one({"Title": query})["_id"]
    removed = False
    for user in UserRepo.find():
        pushedArts = UserSchema().dump(user)["Pushed"]
        if str(artId) in pushedArts:
            removed = True
            pushedArts.remove(str(artId))
            UserRepo.find_one_and_update({"Username": user["Username"]}, {"$set": {"Pushed": pushedArts}})
        else:
            pushedArts.append(str(artId))
            UserRepo.find_one_and_update({"Username": user["Username"]}, {"$set": {"Pushed": pushedArts}})

    if removed:
        return("Article " + (str(title)) + " removed")
    else:
        return("Article " + (str(title)) + " added")           




def toggle_favorite(uname, title):
    query = re.compile("^" + title, re.IGNORECASE)
    artId = ArtRepo.find_one({"Title": query})["_id"]
    userFavs = UserSchema().dump(UserRepo.find_one({"Username": uname}))["Favorites"]
    if str(artId) in userFavs:
        userFavs.remove(str(artId))
        UserRepo.find_one_and_update({"Username": uname}, {"$set": {"Favorites": userFavs}}, return_document=ReturnDocument.AFTER)
        return("Article unfavorited")
    else:
        userFavs.append(str(artId))
        UserSchema().dump(UserRepo.find_one_and_update({"Username": uname}, {"$set": {"Favorites": userFavs}}, return_document=ReturnDocument.AFTER))
        return("Article favorited")

if __name__ == "__main__":
    write.run()
