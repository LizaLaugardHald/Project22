from tkinter import Y, Scrollbar, Label, Toplevel, RIGHT, LEFT, BOTH, VERTICAL, Frame, Canvas
import webbrowser
import webbrowser

class Turbine_Defect(Toplevel):
    def __init__(self, defect, master):
        super().__init__(master = master)

        defect_name = defect['defect_type']
        self.title("Turbine defect: " + defect_name)
        self.geometry("800x800")

        cframe = Frame(self)
        cframe.pack(fill=BOTH, expand=1)

        my_canvas = Canvas(cframe)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        
        scrollbar = Scrollbar(cframe, orient=VERTICAL, command=my_canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=scrollbar.set)
        my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        second_frame = Frame(my_canvas)
        my_canvas.create_window((0,0), window=second_frame, anchor="nw")

        defect_name_label = Label(second_frame, text="Defect name: " + defect_name).pack()
        defect_defect_id_label = Label(second_frame, text="Defect id: " + defect['defect_id']).pack()
        defect_distance_from_root_label = Label(second_frame, text="Distance from root: " + str(defect['distance_from_root'])).pack()

        step_count = 1
        for step in defect['steps']:
            buffer_label = Label(second_frame, text="").pack()
            step_count_label = Label(second_frame, text="Step: " + str(step_count)).pack()
            defect_elcometer_datapoint_label = Label(second_frame, text="Elcometer datapoint:").pack()
            defect_ts_label = Label(second_frame, text="ts: " + str(step['elcometer_datapoint']['ts'])).pack()
            defect_rh_label = Label(second_frame, text="rh: " + str(step['elcometer_datapoint']['rh'])).pack()
            defect_td_label = Label(second_frame, text="td: " + str(step['elcometer_datapoint']['td'])).pack()
            defect_tdelta_label = Label(second_frame, text="tdelta: " + str(step['elcometer_datapoint']['tdelta'])).pack()
            defect_tdb_label = Label(second_frame, text="tdb: " + str(step['elcometer_datapoint']['tdb'])).pack()
            defect_twb_label = Label(second_frame, text="twb: " + str(step['elcometer_datapoint']['twb'])).pack()
            defect_sh_label = Label(second_frame, text="sh: " + str(step['elcometer_datapoint']['sh'])).pack()
            defect_altitude_label = Label(second_frame, text="Altitude: " + str(step['altitude'])).pack()
            defect_root_distance_label = Label(second_frame, text="Root distance: " + str(step['root_distance'])).pack()
            defect_component_length_label = Label(second_frame, text="Component length: " + str(step['component_length'])).pack()
            defect_timestamp_label = Label(second_frame, text="Timestamp: " + str(step['timestamp'])).pack()
            defect_linked_label = Label(second_frame, text="Linked: " + str(step['linked'])).pack()
            defect_rep_step_label = Label(second_frame, text="Rep step: " + str(step['rep_step'])).pack()
            defect_rep_side_label = Label(second_frame, text="Rep side: " + str(step['rep_side'])).pack()
            defect_blade_label = Label(second_frame, text="Blade: " + str(step['blade'])).pack()
            defect_comment_label = Label(second_frame, text="Comment: " + str(step['comment'])).pack()
            defect_px_mm_label = Label(second_frame, text="px mm: " + str(step['px_mm'])).pack()

            buffer_label = Label(second_frame, text="").pack()

            if(step['damage_line_cords'] != None):
                damage_line_cord_count = 1
                for damage_line_cord in step['damage_line_cords']:
                    damage_line_cord_count_label = Label(second_frame, text="Damage line cord number: " + str(damage_line_cord_count)).pack()
                    damage_line_cord_label = Label(second_frame, text=str(damage_line_cord[0]) + ", " + str(damage_line_cord[1])).pack()
                    buffer_label = Label(second_frame, text="").pack()
                    damage_line_cord_count = damage_line_cord_count + 1
                step_count = step_count + 1

            #Insert image.
            image_label = Label(second_frame, text="Image", fg="blue", cursor="hand2")
            image_label.pack()
            image_label.bind("<Button-1>", lambda e: webbrowser.open_new(step['image']['blob']))
            defect_raven_label = Label(second_frame, text="Raven: " + step['image']['raven']).pack()