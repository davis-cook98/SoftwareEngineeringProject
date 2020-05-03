import pymongo
from pymongo import MongoClient
from .middlewares import login_required
from flask import Flask, json, g, request
from .Schemas import ArticleSchema
from .ReadMongo import ReadConnect as Read
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
@app.route('/WriteAPI', methods = ['GET', 'POST'])
def addFavorite():
    title = request.args.get('title')
    return make_favorite(title)


#definitions
def make_favorite(title):
    title = request.args.get('title') #I think this is redundent because it takes in title as a parameter
    description = request.args.get('description')
    published = request.args.get('published')
    InsertTime = request.args.get('InsertTime')
    return updateList(title, description, published, InsertTime)
