from os import name
import pandas as pd 
import datetime
from tkinter import * 
from tkcalendar import *

from class_food import Food
from class_entry_food import Entry_Food



master = Tk()
master.title("FoneFridge")
canvas = Canvas(master, bg="#FCF0E4", height=750, width=750)
canvas.pack()

class Fonefridge(Frame):
    def __init__(self, master):
        app_frame = Frame(master)
        app_frame.pack() #geometry CHECK GUI LECTURE

        #visual part(no function):
        #top title frame
        self.frame_top = Frame(master, bg="#A9B6BE")
        self.frame_top.place(relx=0.01, rely=0.01, relheight=0.1, relwidth=0.98)
        #main title-FONEFRIDGE
        self.title = Label(self.frame_top, bg="#A9B6BE", text= "FONEFRIDGE", font="roboto 22")
        self.title.pack(pady=14)

        #sides:
        # MODES--------
        self.add_mode = PhotoImage(file="toggle/add.png")
        self.edit_mode = PhotoImage(file="toggle/edit.png")

        #button variable:
        global is_add
        is_add = True

        self.add_button = Button(self.frame_top, image=self.add_mode, command=switch_toggle)
        self.add_button.pack(padx=5, pady=5, side=RIGHT)

        
        # CALENDAR--------
        self.entry_date = DateEntry(self.frame_top, width= 50, height= 50, background= "#FCF0E4", foreground= "#576566", locale= "de_DE")
        self.entry_date._top_cal.overrideredirect(False)
        self.entry_date.pack(padx=5, pady=5, side=LEFT)

        #changing BOTTOM frame:
        self.frame_change = Frame(master)
        self.frame_change.pack(relx=0.01, rely=0.01, relheight=0.87, relwidth=0.98)
        
    def switch_toggle(self):
        global is_add
        if is_add == True:
            self.add_button.config(image=self.edit_mode)
            is_add = False
        else:
            self.add_button.config(image=self.add_mode)
            is_add = True
        

e = Fonefridge(master)

master.mainloop()