from tkinter import *
from MongoConnect import Connection
import datetime

from pymongo import MongoClient

#Connect to DB
client = MongoClient('localhost', 27017)

db = client.SoftwareEngineering

#Load an admin acc
admin = {"Username": "admin", "Password": "password", #lol Equifax
"FirstName": "Admin", "LastName": "McAdminerson", "Date": datetime.datetime.utcnow()} 
Users = db.Users
Users.insert_one(admin)

def addPerson(user, passw):
    insertPers = {"Username": user, 
                  "Password": passw,
                  "FirstName": "", 
                  "LastName": "", 
                  "Date": datetime.datetime.utcnow()
                 }
    Users.insert_one(insertPers)

#Setup Tkinter
screen = Tk()
screen.title("Login")
screen.geometry("200x200")

#If they login, check if creds are in db
def run1():
    testName = username.get()
    testPass = password.get()

    if(Users.find_one({"Username": testName, "Password": testPass})) is None:
        print("No user found, please check your credentials or register.")
    else:
        print("Logged in succesfully, welcome " + testName.capitalize())

    # new_text = "Logged in!"
    # print(new_text)
    #print(username.get() + passw)
    password_entry.delete(0,END)
    username_entry.delete(0,END)



#If they register, check if username is in db, if not register
def run2():
    newUser = username.get()
    newPass = password.get()
    if newUser == "" or newPass == "":
        print("Fields cannot be blank")
    elif Users.find_one({"Username": newUser}) is not None:
        print("Username taken, please change.")
    else:
        addPerson(newUser, newPass)
        print("Registered, welcome")
        print("Click login to login :D")
    

#More Tkinter setup
login_text = Label(text = "Login")
register_text = Label(text = "Register")
username_text = Label(text = "Username")
password_text = Label(text = "Password")

login_text.pack()
username_text.place(x = 15, y = 50)
password_text.place(x = 15, y = 95)

username = StringVar()
username_entry = Entry(text = "Enter username", textvariable = username)
username_entry.place(x = 73, y = 50)


password = StringVar()
password_entry = Entry(text = "Enter Password", textvariable = password)
password_entry.place(x = 73, y = 95)


login_button = Button(text = "login", fg = "white", bg = "black", command = run1)
register_button = Button(text = "register", fg = "white", bg = "black", command = run2)

login_button.place(x = 45, y = 150)
register_button.place(x = 115, y = 150)

screen.mainloop()
