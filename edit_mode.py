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

class Edit(Frame):
    def __init__(self, master):
        self.df = pd.read_csv("popular_items_library.csv")
        self.df_user = pd.read_csv("user_items.csv")

        # EDIT MODE DESIGN

        #edit frame
        self.frame_edit = Frame(master, bg="#C2D7D0")
        self.frame_edit.place()

        #TITLES:
        #food name search title-Search the name of your item:
        self.title = Label(self.frame_middle, bg="#E9BFA7", text= "Search the name of your item:", font="roboto 15")
        self.title.pack(pady=5)


        #TYPE SELECT:
        food_types = df["types"]

        self.food_type = StringVar(frame_bottom_left)
        self.food_type.set("Please select food type")

        self.food_type_dropdown = OptionMenu(frame_bottom_left, food_type, food_type_list, command=generate_item_dropdown) 
        self.food_type_dropdown.pack(padx=5, pady=5, side=TOP)
        




    #def Store_name(self):
        #name = return self.name

#print(name)

e = Fonefridge(master)

master.mainloop()