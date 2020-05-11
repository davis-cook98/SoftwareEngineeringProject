import time
import pymongo
import json
import schedule
from GetData.NewsAPICall import InsertData

from pymongo import MongoClient

#Connect to DB
client = MongoClient('localhost', 27017)
db = client.SoftwareEngineering
ArtInfo = db.command("collstats", "ArtRepo")
count = ArtInfo["count"]

#Sets schedule for daily load. This specific one is midnight
schedule.every().day.at("00:00").do(InsertData()) 

#Run forever, load when called
while True:
    schedule.run_pending() 
    time.sleep(1) 