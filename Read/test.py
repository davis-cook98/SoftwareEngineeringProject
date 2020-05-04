import pymongo
from pymongo import MongoClient
from middlewares import login_required
from flask import Flask, json, g, request
from Schemas import ArticleSchema
from flask_cors import CORS
from flask import request
import re

#Connect to DB
client = MongoClient('localhost', 27017)
db = client.SoftwareEngineering 
ArtRepo = db.ArtRepo

def get_article(title):
    query = re.compile("^" + title, re.IGNORECASE)
    print(ArticleSchema().dump(ArtRepo.find_one({"Title": query})))

get_article(input("hi "))