from asyncio.windows_events import NULL
from urllib import request
import requests
from tkinter import Tk, Label, Entry, Button, Frame

USERNAME="liza.voros@hotmail.com"
PASSWORD="liza123"

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

# Function for attempting to login with the users credentials.
def handle_click_login():
    try:
        #Convert the username and password from an entry object to a string
        username = username_entry.get()
        password = password_entry.get()
        print(username)
        login_data = validate_response(
        requests.post(host + "/api/v1/auth/signin/", data={
            'email': username,
            'password': password
        })
        )
        token = login_data["token"]
        print(token)
    except:
        print("Wrong username or password")
    

root = Tk()
frame = Frame(width=100, height=100)

login_label = Label(master=frame, text="Login", width=50, height=2)
login_username = Label(master=frame, text="Username:", width=50)
username_entry = Entry(master=frame, width=50)
login_password = Label(master=frame, text="Password:", width=50)
password_entry = Entry(master=frame, width=50)
login_button = Label(master=frame, width=50)

button = Button(master=frame, text="Login", width=50, command=handle_click_login)
#button.bind("<Button-1>", )

login_label.pack()
login_username.pack()
username_entry.pack()
login_password.pack()
password_entry.pack()
login_button.pack()
button.pack()

frame.pack()

root.mainloop()

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

