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
        #modes

        #calendar
        self.entry_date = DateEntry(self.frame_top, width= 120, height= 120, background= "#FCF0E4", foreground= "#576566", borderwidth= 1, locale= "de_DE")
        self.entry_date._top_cal.overrideredirect(False)
        self.entry_date.pack(padx=5, pady=5, side=LEFT)

        #changing place:
        self.frame_change = Frame(master)
        self.frame_change.pack(relx=0.01, rely=0.01, relheight=0.87, relwidth=0.98)




e = Fonefridge(master)

master.mainloop()