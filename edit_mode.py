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
        self.df = pd.read_csv("popular_items_library.csv")
        self.df_user = pd.read_csv("user_items.csv")

        # EDIT MODE DESIGN

        #edit frame
        self.frame_edit = Frame(master, bg="#C2D7D0")
        self.frame_edit.place(relx=0.01, rely=0.01, relheight=0.87, relwidth=0.98)

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
        

        
        #printing results:
        self.result = Label(self.frame_bottom, justify="left", bg="#BE796D", font="roboto 15")
        self.result.grid(row=0, column=0, padx=2, pady=5, sticky=W)

        self.result2 = Label(self.frame_bottom, justify="left", bg="#BE796D", font="roboto 11")
        self.result2.grid(row=1, column=0, padx=2, pady=2, sticky=W)

        self.result3 = Label(self.frame_bottom, justify="left", bg="#BE796D", font="roboto 11")
        self.result3.grid(row=2, column=0, padx=2, pady=2, sticky=W)

        self.result4 = Label(self.frame_bottom, justify="left", bg="#BE796D", font="roboto 11")
        self.result4.grid(row=3, column=0, padx=2, pady=2, sticky=W)


        #SAVE button:
        self.save_button = Button(self.frame_middle, text="SAVE", command=self.save_item)
        self.save_button.pack(padx=10, pady=5)

        #DISCARD button:
        self.discard_button = Button(self.frame_middle, text="DISCARD", command=self.erase_all)
        self.discard_button.pack(padx=10, pady=5)



    def display_item(self):
        self.result.config(text="Here is the result for "+self.entry_name.get()+":")
        self.result2.config(text=Food.display_food(Food(self.entry_name.get())))
        self.result3.config(text=Food.display_expire(Food(self.entry_name.get())))
        self.result4.config(text=Food.display_notify(Food(self.entry_name.get())))

    def generate_item_dropdown(self):

    def save_item(self):

    def erase_all(self):



    #def Store_name(self):
        #name = return self.name

#print(name)

e = Fonefridge(master)

master.mainloop()