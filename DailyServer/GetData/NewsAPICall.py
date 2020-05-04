import requests
import json
import datetime
import pymongo

from pymongo import MongoClient

#Connect to DB
client = MongoClient('localhost', 27017)

db = client.SoftwareEngineering
 
ArtRepo = db.ArtRepo

#Parse json made by NewsAPICall and insert into MongoDB
def jsonParse(filename):

    #with open("NewsFiles/" + filename + ".json") as jsonFile:
    #    data = json.load(jsonFile)

        articles = filename["articles"]

        for article in articles:
            title = article["title"]
            description = article["description"]
            date = article["publishedAt"]

            insertArt = {"Title": title, 
                    "Description": description,
                    "Published": date, 
                    "InsertTime": datetime.datetime.utcnow(),
                    "favorited": ""
                    }

            ArtRepo.insert_one(insertArt)

def InsertData():
    with open("../../client_secret.json") as f:
        data = json.load(f)

    #URL for get request
    url = ('https://newsapi.org/v2/everything?'
            'q=College&'
            'q=University&'
            'q=HigherEducation&'
            'SortBy=recent&'
            'apiKey=' + data["NewsApi"])

    response = requests.get(url)

    #Gets a nice name for a file
    now = datetime.datetime.now()
    dateString = str(now.year) + str(now.month) + str(now.day)

    jsonData = response.json()

    #Saves the output to json for processing
    #with open("NewsFiles/" + dateString + ".json", "w") as dateFile:
    #    json.dump(jsonData, dateFile)
    # print(response.json())

    #Calls an aux function to insert the data
    jsonParse(jsonData)

InsertData()
