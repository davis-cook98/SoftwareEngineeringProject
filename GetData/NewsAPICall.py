import requests
import json
import datetime

from InsertData import jsonParse

with open("../client_secret.json") as f:
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
with open("NewsFiles/" + dateString + ".json", "w") as dateFile:
    json.dump(jsonData, dateFile)
# print(response.json())

#Calls an aux function to insert the data
jsonParse(dateString)