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

class Edit(Fonefridge):
    def __init__(self, master):
        app_frame = Frame(master)
        app_frame.pack() #geometry CHECK GUI LECTURE

        #visual part(no function):
        #top title frame
        self.frame_top = Frame(master, bg="#A9B6BE")
        self.frame_top.place(relx=0.01, rely=0.01, relheight=0.1, relwidth=0.98)

        #changing BOTTOM frame:
        self.frame_edit = Frame(master, bg="#C2D7D0")
        self.frame_edit.place(relx=0.01, rely=0.12, relheight=0.87, relwidth=0.98)



        #main title-FONEFRIDGE
        self.title = Label(self.frame_top, bg="#A9B6BE", text= "FONEFRIDGE", font="roboto 22")
        self.title.pack(pady=14)


        #read .csv files here:
        self.df = pd.read_csv("popular_items_library.csv")
        self.df_user = pd.read_csv("user_items.csv")
        

        # EDIT MODE DESIGN

        #TITLES:
        #food name search title-Search the name of your item:
        self.title = Label(self.frame_middle, bg="#E9BFA7", text= "Search the name of your item:", font="roboto 15")
        self.title.pack(pady=5)


        #TYPE SELECT:
        self.food_types = self.df["types"]

        self.food_type = StringVar(self.frame_edit)
        self.food_type.set("Please select food type")

        self.food_type_dropdown = OptionMenu(frame_bottom_left, food_type, food_type_list, command=self.generate_item_dropdown) 
        self.food_type_dropdown.pack(padx=5, pady=5, side=TOP)
        




    #def Store_name(self):
        #name = return self.name

#print(name)

e = Fonefridge(master)

master.mainloop()