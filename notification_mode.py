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