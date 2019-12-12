from tkinter import *

screen = Tk()
screen.title("Login")
screen.geometry("200x200")


def run1():
    new_text = "Logged in!"
    print(new_text)
    passw = password.get()
    password_entry.delete(0,END)

    
def run2():
    new_text = "Registered!"
    print(new_text)
    

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
