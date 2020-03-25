import asyncio
import aiocron
import requests
import json
import datetime
import pymongo
import json
import pprint
from GetData.NewsAPICall import InsertData

from pymongo import MongoClient

#Connect to DB
client = MongoClient('localhost', 27017)

db = client.SoftwareEngineering

ArtInfo = db.command("collstats", "ArtRepo")

count = ArtInfo["count"]

async def main():
    #Get new Articles
    @aiocron.crontab('1 0 * * *')
    async def LoadFiles():
        InsertData()

    #Get article collection info
    ArtInfo = db.command("collstats", "ArtRepo")

    count = ArtInfo["count"]

    #Clean up records
    async def cleanDatabase():
        if count > 20000:
            limitSize = count - 20000
            OldestRecords = db.ArtRepo.find().sort({ "date_time" : -1 }).limit(limitSize)

            for record in OldestRecords:
                db.ArtRepo.delete_one(record)


asyncio.run(main())