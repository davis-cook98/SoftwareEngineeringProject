import requests
import json
import datetime

with open("../client_secret.json") as f:
    data = json.load(f)

url = ('https://newsapi.org/v2/everything?'
        'q=College&'
        'q=University&'
        'q=HigherEducation&'
        'SortBy=recent&'
        'apiKey=' + data["NewsApi"])

response = requests.get(url)

now = datetime.datetime.now()
dateString = str(now.year) + str(now.month) + str(now.day)

jsonData = response.json()

with open("../NewsFiles/" + dateString + ".json", "w") as dateFile:
    json.dump(jsonData, dateFile)
# print(response.json())
    
