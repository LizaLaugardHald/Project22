import requests
from tkinter import Image, Label, Entry, Button, Toplevel, W
from Helper_Functions import validate_response, host
from Turbines import Turbines
from PIL import ImageTk, Image

class Login(Toplevel):
    def __init__(self, master):
        super().__init__(master = master)

        def handle_click_login(username_entry, password_entry):
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
                print("Wrong username or password")#m.config(text="Wrong username or password. Please try again.")

        self.title("Login")
        self.geometry("800x711")
        
        vindmoelle_image = Image.open("Vindmoelle.png")
        resize_image = vindmoelle_image.resize((400, 711))
        img = ImageTk.PhotoImage(resize_image)
        image = Label(self, image=img)
        image.image = img
        image.grid(column=0, row=0, rowspan=7, sticky=W)

        login_label = Label(self, text="Login:", font="bold").place(x=500, y=250)
        login_username = Label(self, text="Username:", font="bold").place(x=500, y=280)
        username_entry = Entry(self, width=35)
        username_entry.place(x=500, y=305)
        login_password = Label(self, text="Password:", font="bold").place(x=500, y=330)
        password_entry = Entry(self, width=35, show="*")
        password_entry.place(x=500, y=355)

        button = Button(self, text="Login", command=lambda:handle_click_login(username_entry, password_entry), font="bold")
        button.place(x=500, y=385)
