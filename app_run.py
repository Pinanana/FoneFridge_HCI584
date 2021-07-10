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

class Fonefridge(object):
    def __init__(self, master):
        self.df = pd.read_csv("popular_items_library.csv")
        self.df_user = pd.read_csv("user_items.csv")

        app_frame = Frame(master)
        app_frame.pack() #geometry CHECK GUI LECTURE

        #visual part(no function):
        #top title frame
        self.frame_top = Frame(master, bg="#A9B6BE")
        self.frame_top.place(relx=0.01, rely=0.01, relheight=0.056, relwidth=0.98)

        # MAIN title-FONEFRIDGE------------
        self.title = Label(self.frame_top, bg="#A9B6BE", text= "FONEFRIDGE", font="roboto 22")
        self.title.grid(column=1, row=0, ipadx=151)

        # MODES--------
        #button variable:
        self.add_button = Button(self.frame_top, width=10, text="ADD MODE", font="roboto 15", bg="#A9B6BE",command=self.change_label)
        self.add_button.grid(column=0, row=0, ipadx=5)
        self.is_add = True

        # CALENDAR--------
        self.calendar_button = Button(self.frame_top, width=10, text="CALENDAR", font="roboto 15", bg="#A9B6BE", command=self.calendar_entry)
        self.calendar_button.grid(column=2, row=0, ipadx=5)
        
    def change_label(self):
        if self.is_add == True:  #add mode triggers!!
            self.add_button.config(text="EDIT MODE", font="roboto 15")
            self.is_add = False
        else:                   #edit mode triggers!!
            self.add_button.config(text="ADD MODE", font="roboto 15")
            self.is_add = True
        
    # calendar pop-up window def here
    def calendar_entry(self):  
        self.pop_up = Toplevel(master)

        self.date_label = Label(self.pop_up, text="Choose date", font="roboto 12")
        self.date_label.pack(padx=10, pady=10)

        self.entry_cal = DateEntry(self.pop_up, background= "#A9B6BE", foreground= "#576566")
        self.entry_cal.pack(padx=10, pady=10)

        self.ok_button = Button(self.pop_up, text="OK", bd=0, command=self.calendar_get)
        self.ok_button.pack(padx=10, pady=10)
    
    def calendar_get(self):
        self.entry_date = self.entry_cal.get_date()   #========================ENTRY DATE VARIABLE self.entry_date
        print(self.entry_date)
        #self.notification_trigger() =========================NOTIFICATION TRIGGER THINGY
        self.pop_up.destroy()

e = Fonefridge(master)

master.mainloop()