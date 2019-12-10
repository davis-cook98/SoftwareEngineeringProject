# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 20:43:36 2019

@author: sabrimos
"""


class newUser:
    def __init__(self, firstName, lastName, schoolsInterestedIn, username, password, userType):
        self.firstName = firstName
        self.lastName = lastName
        self.schoolsInterestedIn = schoolsInterestedIn
        self.username = username
        self.password = password
        self.userType = userType

    
    def getFirstName(self):
        return self.firstName
    
    def setFirstName(self, newFirstName):
        self.firstName = newFirstName
        
    def getLastName(self):
        return self.lastName
    
    def setLastName(self, newLastName):
        self.lastName = newLastName
        
    def getSchoolsInterestedIn(self):
        return self.schoolsInterestedIn
    
    def setSchoolsInterestedIn(self, newSchoolsInterestedIn):
        self.schoolsInterestedIn = newSchoolsInterestedIn 

    def getUsername(self):
        return self.username
    
    def setUsername(self, newUsername):
        self.username = newUsername
                
    def getPassword(self):
        return self.password
    
    def setPassword(self, newPassword):
        self.password = newPassword
                        
    def getUserType(self):
        return self.userType
    
    def setUserType(self, newUserType):
        self.userType = newUserType
        

