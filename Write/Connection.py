import pymongo
import datetime

from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client.test_database

person = {"Username": "dcook123", "Password": "password",
"FirstName": "Davis", "LastName": "Cook", "Date": datetime.datetime.utcnow()} 
people = db.people
#people.insert_one(person).inserted_id

def addPerson(user, passw):
    insertPers = {"Username": user, 
                  "Password": passw,
                  "FirstName": "", 
                  "LastName": "", 
                  "Date": datetime.datetime.utcnow()
                 }
    people.insert_one(insertPers).inserted_id
    
    
#print(people.find_one())