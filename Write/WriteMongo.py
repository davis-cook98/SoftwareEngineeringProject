import os
from pymongo import MongoClient


class WriteConnect(object):
 def __init__(self):
   self.db = MongoClient('localhost', 27017)

 #This should never be used because articles will be loaded and never edited. Made in case
 def createArticle(self, kudo):
   return self.db.ArtRepo.insert_one(kudo)

 def updateArticle(self, selector, kudo):
   return self.db.ArtRepo.replace_one(selector, kudo).modified_count
 
 def deleteArticle(self, selector):
   return self.db.ArtRepo.delete_one(selector).deleted_count

#For creating new users
 def createUser(self, kudo):
   return self.db.Users.insert_one(kudo)

 def updateUser(self, selector, kudo):
   return self.db.Users.replace_one(selector, kudo).modified_count
 
 def deleteUser(self, selector):
   return self.db.Users.delete_one(selector).deleted_count