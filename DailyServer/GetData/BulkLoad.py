import requests
import json
import datetime
import pprint
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
            
            if ArtRepo.find({"Title": title}) is None:
                ArtRepo.insert_one({"Title": title,
                        "Description": description,
                        "Published": date, 
                        "InsertTime": datetime.datetime.utcnow()})

def InsertData(date1, date2, keyword):
    with open("../../client_secret.json") as f:
        data = json.load(f)

    #URL for get request
    queryString = 'q=' + keyword + '&'
    dateString = 'from=' + date1 + '&to=' + date2 + '&'
    url = ('https://newsapi.org/v2/everything?' +
            queryString +
            dateString +
            'sortBy=relevance&'
            'apiKey=' + data["NewsApi"])

    response = requests.get(url)

    jsonData = response.json()

    #Saves the output to json for processing
    #with open("NewsFiles/" + dateString + ".json", "w") as dateFile:
    #    json.dump(jsonData, dateFile)
    # print(response.json())

    #Calls an aux function to insert the data
    #pprint.pprint(jsonData)
    if "articles" in jsonData:
        jsonParse(jsonData)

#chosen using the top words on google's SEO database
keywords = ["school", "eduscol", "university", "department of education", "collegiate", "academy", "undergraduate", "professor", "academica",
            "graduate", "scholastic", "unverisity system", "cyberschool", "semester", "dean", "gpas"]

#Somewhat randoms dates were chosen
startDates = ["2020-04-03", "2020-04-07", "2020-04-10", "2020-04-13", "2020-04-17", "2020-04-24", "2020-04-29", "2020-05-02"]
endDates = ["2020-04-06", "2020-04-09", "2020-04-12", "2020-04-16", "2020-04-23", "2020-04-28", "2020-05-01", "2020-05-06"]

for word in keywords:
    for (date1, date2) in zip(startDates, endDates):
        InsertData(date1, date2, word)
        print(word + "   " + date1 + "-" + date2)
