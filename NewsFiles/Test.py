import json
import pymongo
import datetime

from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client.SoftwareEngineering
 
ArtRepo = db.ArtRepo

with open("20191212.json") as jsonFile:
    data = json.load(jsonFile)

    articles = data["articles"]

    for article in articles:
        title = article["title"]
        description = article["description"]
        date = article["publishedAt"]

        insertArt = {"Title": title, 
                  "Description": description,
                  "Published": date, 
                  "InsertTime": datetime.datetime.utcnow()
                 }

        ArtRepo.insert_one(insertArt)



