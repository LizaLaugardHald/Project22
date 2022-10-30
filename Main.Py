from asyncio.windows_events import NULL
import requests
from tkinter import END, Tk, Label, Entry, Button, Toplevel
from types import SimpleNamespace
from tkHyperlinkManager import HyperlinkManager
import webbrowser
from functools import partial

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
        self.geometry("700x200")

        
        #General turbine info
        info_label = Label(self, text="General info:")
        turbine_name_label = Label(self, text="Turbine name: " + turbine_name).pack()
        turbine_id_label = Label(self, text="Id: " + turbine['id']).pack()
        turbine_asset_serial_no_label = Label(self, text="Asset serial number: " + turbine['asset_serial_no']).pack()
        turbine_component_length_label = Label(self, text="Component length: " + str(turbine['component_length'])).pack()
        turbine_component_width_label = Label(self, text="Component width: " + str(turbine['component_width'])).pack()
        turbine_tower_height_label = Label(self, text="Tower height: " + str(turbine['tower_height'])).pack()
        turbine_gps_label = Label(self, text="GPS: Latitude: " + str(turbine['gps']['lat']) + ", Longtitude: " + str(turbine['gps']['lon'])).pack()
        turbine_sessions_label = Label(self, text="Sessions: " + str(turbine['sessions'])).pack()

        buffer_label = Label(self, text="").pack()

        #Preconfiguration info
        turbine_preconfiguration_label = Label(self, text="Preconfiguration: ").pack()
        turbine_preconfiguration_id_label = Label(self, text="Preconfiguration id: " + turbine['preconfiguration']['id']).pack()
        turbine_preconfiguration_name_label = Label(self, text="Preconfiguration name: " + turbine['preconfiguration']['name']).pack()
        turbine_campaign_id_label = Label(self, text="Campaign id: " + turbine['preconfiguration']['campaign']['id']).pack()
        turbine_campaign_name_label = Label(self, text="Campaign name: " + turbine['preconfiguration']['campaign']['name']).pack()

        buffer_label = Label(self, text="").pack()

        #PDFs
        turbine_pdfs_label = Label(self, text="PDFs: ").pack()
        for pdf in turbine['pdfs']:
            turbine_pdf_label = Label(self).pack()
            hyperlink= HyperlinkManager(turbine_pdf_label)
            turbine_pdf_label.insert(END, "Filename: " + pdf['filename'], hyperlink.add(partial(webbrowser.open, pdf['blob'])))
        


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

        print(turbine_data)#Delete this later. Used for debugging
    
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

