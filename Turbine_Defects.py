import requests
from tkinter import Label, Button, Toplevel
from Turbine_Defect import Turbine_Defect
from Helper_Functions import validate_response, host

class Turbine_Defects(Toplevel):
    def __init__(self, turbine_id, headers, master):
        super().__init__(master = master)

        def handle_turbine_defect_select(defect, master):
            turbine_defect_window = Turbine_Defect(defect, master)
        defect_details_data = validate_response(
            requests.get(host + "/api/v1/turbine/" + turbine_id + "/defects/detailed/", headers=headers)
        )

        self.title("Turbine defects")

        error = "No"
        if defect_details_data['error']:
            error = "yes"
        turbines_error_label = Label(self, text="Error: " + error).pack(anchor="w")

        if defect_details_data['message'] != None:
            turbines_message_label = Label(self, text="Message: " + defect_details_data['message']).pack(anchor="w")

        for defect in defect_details_data['data']['defects']:
            defect_name = defect['defect_type']
            defect_name_button = Button(self, text="Click for info on defect named: " + defect_name, command=lambda d=defect: handle_turbine_defect_select(d, master), font="bold")
            defect_name_button.pack(anchor="w")