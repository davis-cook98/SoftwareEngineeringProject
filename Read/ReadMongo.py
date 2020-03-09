import os
from pymongo import MongoClient

#Used to look at articles
class ReadConnect(object):
 def __init__(self):
   self.db = MongoClient('localhost', 27017)

 def findAllArticles(self, selector):
   return self.db.ArtRepo.find(selector)
 
 def findArticle(self, selector):
   return self.db.ArtRepo.find_one(selector)
 
 def findUser(self, selector):
   return self.db.Users.find_one(selector)
 