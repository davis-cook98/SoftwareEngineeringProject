import pymongo
import datetime

from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client.test_database
collection = db.test_collection

person = {"Username": "dcook123", "Password": "password",
"FirstName": "Davis", "LastName": "Cook", "Date": datetime.datetime.utcnow()} 
people = db.people
person_id = people.insert_one(person).inserted_id
#person_id

#print(people.find_one())

def test(this, that):
    print(this + that)
test(3, 4)