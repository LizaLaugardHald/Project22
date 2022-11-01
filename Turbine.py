from tkinter import Label, Button, Toplevel
import webbrowser
from Turbine_Defects import Turbine_Defects

class Turbine(Toplevel):
    def __init__(self, turbine, headers, master):
        super().__init__(master = master)

        def handle_turbine_defects(turbine_id, headers, master):
            turbine_defects_window = Turbine_Defects(turbine_id, headers, master)

        turbine_name = turbine['name']

        self.title("Turbine: " + turbine_name)
        self.geometry("800x711")
        self.iconbitmap('ZentoSoft.ico')

        #General turbine info
        info_label = Label(self, text="General info:", font="bold").pack(anchor="w")
        turbine_name_label = Label(self, text="Turbine name: " + turbine_name).pack(anchor="w")
        turbine_id_label = Label(self, text="Id: " + turbine['id']).pack(anchor="w")
        turbine_asset_serial_no_label = Label(self, text="Asset serial number: " + turbine['asset_serial_no']).pack(anchor="w")
        turbine_component_length_label = Label(self, text="Component length: " + str(turbine['component_length'])).pack(anchor="w")
        turbine_component_width_label = Label(self, text="Component width: " + str(turbine['component_width'])).pack(anchor="w")
        turbine_tower_height_label = Label(self, text="Tower height: " + str(turbine['tower_height'])).pack(anchor="w")
        turbine_gps_label = Label(self, text="GPS: Latitude: " + str(turbine['gps']['lat']) + ", Longitude: " + str(turbine['gps']['lon'])).pack(anchor="w")
        turbine_sessions_label = Label(self, text="Sessions: " + str(turbine['sessions'])).pack(anchor="w")

        buffer_label = Label(self, text="").pack(anchor="w")

        #Preconfiguration info
        if turbine['preconfiguration'] != None: #If there is no preconfiguration we do not display any more things.
            turbine_preconfiguration_label = Label(self, text="Preconfiguration: ", font="bold").pack(anchor="w")
            turbine_preconfiguration_id_label = Label(self, text="Preconfiguration id: " + turbine['preconfiguration']['id']).pack(anchor="w")
            turbine_preconfiguration_name_label = Label(self, text="Preconfiguration name: " + turbine['preconfiguration']['name']).pack(anchor="w")
            turbine_campaign_id_label = Label(self, text="Campaign id: " + turbine['preconfiguration']['campaign']['id']).pack(anchor="w")
            turbine_campaign_name_label = Label(self, text="Campaign name: " + turbine['preconfiguration']['campaign']['name']).pack(anchor="w")
            turbine_start_date_label = Label(self, text="Start date: " + turbine['preconfiguration']['campaign']['start_date']).pack(anchor="w")
            turbine_end_date_label = Label(self, text="End date: " + turbine['preconfiguration']['campaign']['end_date']).pack(anchor="w")
            is_active = "No"
            if turbine['preconfiguration']['campaign']['active']:
                is_active = "yes"
            turbine_active_label = Label(self, text="Active: " + is_active).pack(anchor="w")
            turbine_number_of_turbines_label = Label(self, text="Number_of_turbines: " + str(turbine['preconfiguration']['campaign']['number_of_turbines'])).pack(anchor="w")
            turbine_project_ref_label = Label(self, text="Project reference: " + turbine['preconfiguration']['campaign']['project_ref']).pack(anchor="w")
            turbine_last_inspected_ref_label = Label(self, text="Last inspected: " + turbine['preconfiguration']['campaign']['last_inspected']).pack(anchor="w")
            turbine_project_manager_id_label = Label(self, text="Projekt manager id: " + turbine['preconfiguration']['campaign']['project_manager']['uid']).pack(anchor="w")
            turbine_project_manager_name_label = Label(self, text="Projekt manager id: " + turbine['preconfiguration']['campaign']['project_manager']['name']).pack(anchor="w")
            turbine_attatched_turbines_label = Label(self, text="Attached turbines: " + str(turbine['preconfiguration']['attatched_turbines'])).pack(anchor="w")
            
            buffer_label = Label(self, text="").pack(anchor="w")

            turbine_data_label = Label(self, text="Data:", font="bold").pack(anchor="w")
            turbine_asset_type_label = Label(self, text="Asset type: " + turbine['preconfiguration']['data']['asset_type']).pack(anchor="w")
            turbine_work_type_label = Label(self, text="Work type: " + turbine['preconfiguration']['data']['work_type']).pack(anchor="w")
            turbine_work_type_label = Label(self, text="Eye to eye width: " + str(turbine['preconfiguration']['data']['eye_to_eye_width'])).pack(anchor="w")
            turbine_site_name_label = Label(self, text="Site name: " + turbine['preconfiguration']['data']['site_name']).pack(anchor="w")
            turbine_site_gps_label = Label(self, text="Site GPS: Latitude: " + str(turbine['preconfiguration']['data']['site_gps']['lat']) + ", Longitude: " + str(turbine['preconfiguration']['data']['site_gps']['lon'])).pack(anchor="w")
            turbine_site_contry_label = Label(self, text="Site contry: " + turbine['preconfiguration']['data']['site_contry']).pack(anchor="w")
            turbine_requester_of_inspection_label = Label(self, text="Requester of inspection: " + turbine['preconfiguration']['data']['requester_of_inspection']).pack(anchor="w")

            buffer_label = Label(self, text="").pack(anchor="w")

        #PDFs
        turbine_pdfs_label = Label(self, text="PDFs: ", font="bold").pack(anchor="w")
        for pdf in turbine['pdfs']:
            def callback(url):
                webbrowser.open_new(url)
            pdf_label = Label(self, text="Filename: " + pdf['filename'], fg="blue", cursor="hand2")
            pdf_label.pack(anchor="w")
            pdf_label.bind("<Button-1>", lambda e: callback(pdf['blob']))

        buffer_label = Label(self, text="").pack(anchor="w")

        #Defects
        Defects_button = Button(self, text="Click for info on turbine defects", command=lambda: handle_turbine_defects(turbine['id'], headers, master), font="bold")
        Defects_button.pack(anchor="w")