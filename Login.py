import requests
from tkinter import Label, Entry, Button, Toplevel
from Helper_Functions import validate_response, host
from Turbines import Turbines

class Login(Toplevel):
    def __init__(self, master):
        super().__init__(master = master)

        def handle_click_login():
            try:
                #Convert the username and password from an entry object to a string
                username = username_entry.get()
                password = password_entry.get()
                login_data = validate_response(
                    requests.post(host + "/api/v1/auth/signin/", data={
                        'email': username,
                        'password': password
                    })
                )
                #The user successfuly logged in, so now we create a new window.
                turbines = Turbines(login_data, master)
            except:
                login_label.config(text="Wrong username or password. Please try again.")

        self.title("Login")
        self.geometry("300x175")

        login_label = Label(self, text="Login")
        login_username = Label(self, text="Username:")
        username_entry = Entry(self, width=35)
        login_password = Label(self, text="Password:")
        password_entry = Entry(self, width=35)
        login_button = Label(self)

        button = Button(self, text="Login", command=handle_click_login)

        login_label.pack()
        login_username.pack()
        username_entry.pack()
        login_password.pack()
        password_entry.pack()
        login_button.pack()
        button.pack()