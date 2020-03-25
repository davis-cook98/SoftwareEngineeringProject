import json
import pymongo
import datetime

from pymongo import MongoClient

#Connect to DB
client = MongoClient('localhost', 27017)

db = client.SoftwareEngineering
 
ArtRepo = db.ArtRepo

#Parse json made by NewsAPICall and insert into MongoDB
def jsonParse(filename):
    with open("NewsFiles/" + filename + ".json") as jsonFile:
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



