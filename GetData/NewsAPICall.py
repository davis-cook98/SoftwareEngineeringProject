import requests
import json
import os

with open("../client_secret.json") as f:
    data = json.load(f)

url = ('https://newsapi.org/v2/everything?'
        'q=College&'
        'q=University&'
        'q=HigherEducation&'
        'SortBy=recent&'
        'apiKey=' + data["NewsApi"])

response = requests.get(url)

print(response.json())
    
