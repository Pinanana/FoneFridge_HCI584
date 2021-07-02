from app_run import Fonefridge
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

class Notification(Fonefridge):
    def __init__(self, master):
        self.df = pd.read_csv("popular_items_library.csv")
        self.df_user = pd.read_csv("user_items.csv")

        app_frame = Frame(master)
        app_frame.pack() #geometry CHECK GUI LECTURE

        #visual part(no function):
        #top title frame
        self.frame_top = Frame(master, bg="#A9B6BE")
        self.frame_top.place(relx=0.01, rely=0.01, relheight=0.06, relwidth=0.98)

        #changing BOTTOM frame:
        self.frame_change = Frame(master, bg="#E9BFA7")
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
        
        
    def change_image(self):
        self.is_add = True

        if self.is_add == True:  #add mode triggers!!
            self.add_button.config(image=self.edit_mode)
            self.is_add = False
        else:                   #edit mode triggers!!
            self.add_button.config(image=self.add_mode)
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
        self.notification_trigger()
        self.pop_up.destroy()

    def notification_trigger(self):
        self.expi = self.df_user["expiration (days)"] 
        self.noti = self.df_user["notify (days)"]

        self.notify_items = self.df_user.query("notify (days) <= @self.entry_date")


        if self.noti <= self.entry_date <= self.expi:
            self.frame_warning = Frame(master, bg="#BE796D")
            self.frame_warning.place(relx=0.05, rely=0.05, relheight=0.95, relwidth=0.95)

            self.noti_title = Label(self.frame_warning, text="WARNING", font="roboto 22")
            self.noti_title.pack(padx=10, pady=10)

            self.notification_text = Text(self.frame_warning, bg="#BE796D", font="roboto 15", height=200, width=450 bd=0)
            self.notification_text.pack(padx=10, pady=10)
            self.notification_text.insert(END, Entry_Food.notification_message(Entry_food(self.NAMEEEEEEEEE)))




e = Fonefridge(master)

master.mainloop()