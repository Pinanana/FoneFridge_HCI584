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
        self.df_user = pd.read_csv("user_items.csv")

        app_frame = Frame(master)
        app_frame.pack() #geometry CHECK GUI LECTURE

        #visual part(no function):
        #top title frame
        self.frame_top = Frame(master, bg="#A9B6BE")
        self.frame_top.place(relx=0.01, rely=0.01, relheight=0.06, relwidth=0.98)

        #changing BOTTOM frame:
        self.frame_change = Frame(master)
        self.frame_change.place(relx=0.01, rely=0.08, relheight=0.91, relwidth=0.98)



        # MODES--------
        self.add_mode = PhotoImage(file="toggle/add.png")
        self.edit_mode = PhotoImage(file="toggle/edit.png")
        self.date_image = PhotoImage(file="toggle/date.png")
        
        #button variable:
        self.add_button = Button(self.frame_top, image=self.add_mode, bg="#A9B6BE", bd=0,command=self.change_image)
        self.add_button.grid(column=0, row=0, ipadx=5)

        # MAIN title-FONEFRIDGE------------
        self.title = Label(self.frame_top, bg="#A9B6BE", text= "FONEFRIDGE", font="roboto 22")
        self.title.grid(column=1, row=0, ipadx=175)

        
        # CALENDAR--------
        self.calendar_button = Button(self.frame_top, image=self.date_image, bg="#A9B6BE", bd=0, command=self.calendar_entry)
        self.calendar_button.grid(column=2, row=0, ipadx=5)

        #getting date: get_date()
        #calevent_cget(ev_id, option) :     Return value of given option for the event *ev_id*.
        #selection_get() :    If selectmode is 'day', return the selected date as a ``datetime.date``  instance, otherwise return ``None``.

        
        
    def change_image(self):
        self.is_add = True

        if self.is_add == True:
            self.add_button.config(image=self.edit_mode)
            self.is_add = False
        else:
            self.add_button.config(image=self.add_mode)
            self.is_add = True
        

    def calendar_entry(self):
        pop_up = Toplevel(master)
        date_label = Label(pop_up, text='Choose date')
        date_label.pack(padx=10, pady=10)

        entry_date = DateEntry(pop_up, width= 50, height= 50, background= "#A9B6BE", foreground= "#576566", locale= "de_DE")
        entry_date._top_cal.overrideredirect(False)
        entry_date.pack(padx=10, pady=10)

    #def notification_trigger(self):


e = Fonefridge(master)

master.mainloop()