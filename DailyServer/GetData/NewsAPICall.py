import requests
import json
import datetime
import pymongo
import pprint

from pymongo import MongoClient

#Connect to DB
client = MongoClient('localhost', 27017)
db = client.SoftwareEngineering
ArtRepo = db.ArtRepo

#Parse json made by NewsAPICall and insert into MongoDB
def jsonParse(filename):

    articles = filename["articles"]

    print(len(articles))

    for article in articles:
        title = article["title"]
        description = article["description"]
        date = article["publishedAt"]
        url = article["url"]
        
        if ArtRepo.find_one({"Title": title}) is None:
            ArtRepo.insert_one({
                    "Title": title,
                    "Description": description,
                    "Published": date, 
                    "Url": url,
                    "InsertTime": datetime.datetime.utcnow()})

def InsertData():
    with open("../../client_secret.json") as f:
        data = json.load(f)

    #URL for get request
    url = ('https://newsapi.org/v2/everything?'
            'q=College&'
            'SortBy=recent&'
            'apiKey=' + data["NewsApi"])

    response = requests.get(url)
    jsonData = response.json()

    #Calls an aux function to insert the data
    jsonParse(jsonData)

#Calls function
InsertData()
