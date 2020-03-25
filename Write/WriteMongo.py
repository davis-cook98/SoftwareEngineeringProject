import os
from pymongo import MongoClient


class WriteConnect(object):
 def __init__(self):
   self.db = MongoClient('localhost', 27017)

 #This should never be used because articles will be loaded and never edited. Made in case
 def createArticle(self, article):
   return self.db.ArtRepo.insert_one(article)

 def updateArticle(self, selector, article):
   return self.db.ArtRepo.replace_one(selector, article).modified_count

 def deleteArticle(self, selector):
   return self.db.ArtRepo.delete_one(selector).deleted_count

#For creating new users
 def createUser(self, user):
   return self.db.Users.insert_one(article)

 def updateUser(self, user):
   return self.db.Users.replace_one(selector, article).modified_count

 def deleteUser(self, user):
   return self.db.Users.delete_one(selector).deleted_count
