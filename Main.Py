from asyncio.windows_events import NULL
import requests
from tkinter import Text, Tk, Label, Entry, Button, Toplevel
import json
from types import SimpleNamespace

#USERNAME="liza.voros@hotmail.com"
#PASSWORD="liza123"

host="https://raven-api-eu.clobotics.com"

def validate_response(response):
    print(response)
    response_data = response.json()
    assert response.ok
    assert not response_data["error"]
    return response_data

def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values

class Turbine(Toplevel):
    def __init__(self, turbine):
        super().__init__(master = master)

        turbine_name = turbine['name']

        self.title("Turbine: " + turbine_name)
        self.geometry("400x200")


#Class for handling login of the user.
class Turbines(Toplevel):
    def __init__(self, login_data):
        super().__init__(master = master)

        #Function to show a window with information on a selected turbine.
        def handle_turbine_select(turbine):
            turbine_window = Turbine(turbine)

        token = login_data["token"]
        headers = {'Authorization': 'Token ' + token}
        campaign_id = json_extract(login_data, 'id')
        campaign_id = campaign_id[1] # Dårlig løsning. Find på noget bedre. Det skal være dynamisk. Modificer måske json_extract
        

        turbine_data = validate_response(
            requests.get(host + "/api/v1/campaign/" + campaign_id + "/turbines/", headers=headers)
        )

        self.title("Turbines")
        self.geometry("400x200")

        #print(turbine_data)
        #we now need to extract the turbine data to variables we can call upon.

        turbines_label = Label(self, text="Turbines in campaign " + campaign_id + ":")
        turbines_label.pack()

        for turbine in turbine_data['turbines']:
            turbine_name = turbine['name']
            turbine_name_button = Button(self, text="Click for info on turbine named: " + turbine_name, command=lambda t=turbine: handle_turbine_select(t))
            turbine_name_button.pack()

        print("made it to here")


def handle_click_login():
    try:
        #Convert the username and password from an entry object to a string
        username = username_entry.get()
        password = password_entry.get()
        print(username)
        print(password)
        login_data = validate_response(
        requests.post(host + "/api/v1/auth/signin/", data={
            'email': username,
            'password': password
        })
        )
        #The user successfuly logged in, so now we create a new window.
        turbines = Turbines(login_data)
        master.withdraw()
    except:
        login_label.config(text="Wrong username or password. Please try again.")

#Start of program
master = Tk()
master.title("Login")
master.geometry("300x175")

login_label = Label(text="Login")
login_username = Label(text="Username:")
username_entry = Entry(width=35)
login_password = Label(text="Password:")
password_entry = Entry(width=35)
login_button = Label()

button = Button(text="Login", command=handle_click_login)

login_label.pack()
login_username.pack()
username_entry.pack()
login_password.pack()
password_entry.pack()
login_button.pack()
button.pack()

master.mainloop()



# token = login_data["token"]

# campaign_id = json_extract(login_data, 'id')
# campaign_id = campaign_id[1] # Dårlig løsning. Find på noget bedre. Det skal være dynamisk. Modificer måske json_extract

# headers = {'Authorization': 'Token ' + token}

# turbine_data = validate_response(
#     requests.get(host + "/api/v1/campaign/" + campaign_id + "/turbines/", headers=headers)
# )
# #print(turbine_data)

# turbine_id = json_extract(turbine_data, 'id')
# turbine_id = turbine_id[0]

# defect_details_data = validate_response(
#     requests.get(host + "/api/v1/turbine/" + turbine_id + "/defects/detailed/", headers=headers)
# )

#print(defect_details_data)

