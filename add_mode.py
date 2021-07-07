
from os import name
from tkinter.ttk import Combobox, Style, Treeview
import pandas as pd 
import datetime
from tkinter import * 
from tkcalendar import *

from class_food import Food
from class_entry_food import Entry_Food



master = Tk()
master.title("Add")
canvas = Canvas(master, bg="#FCF0E4", height=750, width=750)
canvas.pack()

class Add(object):
    def __init__(self, master):
        app_frame = Frame(master)
        app_frame.pack() #geometry CHECK GUI LECTURE

        #visual part(no function):
        #top title frame
        self.frame_top = Frame(master, bg="#A9B6BE")
        self.frame_top.place(relx=0.01, rely=0.01, relheight=0.06, relwidth=0.98)

        #middle frame
        self.frame_middle = Frame(master, bg="#E9BFA7")
        self.frame_middle.place(relx=0.01, rely=0.08, relheight=0.49, relwidth=0.98)

        #read .csv files here:
        self.df = pd.read_csv("popular_items_library.csv")
        self.df_user = pd.read_csv("user_items.csv")
        
        # ADD MODE

        #food name search title--------Search the name of your item:
        self.title = Label(self.frame_middle, bg="#E9BFA7", text= "Search the name of your item:", font="roboto 15")
        self.title.place(relx=0.03)
        #search variables' frame
        self.frame_vars = Frame(self.frame_middle, bg="#FCF0E4")
        self.frame_vars.place(relx=0.01, rely=0.1, relheight=0.2, relwidth=0.98)

        #TYPE SELECT:
        self.food_type_list = set(self.df["types"])

        self.type_entry = StringVar(self.frame_vars)
        self.type_entry.set("Please select type")

        #self.food_type_dropdown = OptionMenu(self.frame_vars, self.type_entry, *self.food_type_list, command=self.generate_item_dropdown)
        self.food_type_dropdown = Combobox(self.frame_vars, value=self.food_type_list, )
        self.food_type_dropdown.place(relx=0.2, rely=0.3, relwidth=0.27, anchor="n")

        #ITEM SELECT:
        self.entry_name = StringVar(self.frame_vars)
        self.entry_name.set("Please select type first")
        
        self.food_names_dropdown = OptionMenu(self.frame_vars, self.entry_name, "none") 
        self.food_names_dropdown.place(relx=0.5, rely=0.3, relwidth=0.27, anchor="n")

        #SERVINGS SELECT:
        self.servings_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.servings_entry = StringVar(self.frame_vars)
        self.servings_entry.set("Please select servings count")

        self.servings_dropdown = OptionMenu(self.frame_vars, self.servings_entry, *self.servings_list)
        self.servings_dropdown.place(relx=0.8, rely=0.3, relwidth=0.27, anchor="n")

        #selecting servings will trigger this:
        #if self.servings_entry != "Please select servings count" and self.entry_name != "Please select name" and 
        
        #printing results:
        self.frame_results = Frame(self.frame_middle, bg="#BE796D")
        self.frame_results.place(relx=0.05, rely=0.35, relheight=0.45, relwidth=0.9)

        self.result = Label(self.frame_results, text="Here is the result for "+self.entry_name.get()+":", justify="left", bg="#BE796D", font="roboto 15")
        self.result.grid(row=0, column=0, padx=2, pady=5, sticky=W)
        self.result2 = Label(self.frame_results, text=Food.display_food(Food(self.entry_name.get())), justify="left", bg="#BE796D", font="roboto 11")
        self.result2.grid(row=1, column=0, padx=2, pady=2, sticky=W)
        self.result3 = Label(self.frame_results, text=Food.display_expire(Food(self.entry_name.get())), justify="left", bg="#BE796D", font="roboto 11")
        self.result3.grid(row=2, column=0, padx=2, pady=2, sticky=W)
        self.result4 = Label(self.frame_results, text=Food.display_notify(Food(self.entry_name.get())), justify="left", bg="#BE796D", font="roboto 11")
        self.result4.grid(row=3, column=0, padx=2, pady=2, sticky=W)

        #SAVE button:
        self.save_button = Button(self.frame_middle, width=10, text="SAVE", command=self.save_item)
        self.save_button.place(relx=0.4, rely=0.9, anchor="n")

        #DISCARD button:
        self.discard_button = Button(self.frame_middle, width=10, text="DISCARD", command=self.erase_all)
        self.discard_button.place(relx=0.6, rely=0.9, anchor="n")

        #------------------------------------------------------------------------------------


    def generate_item_dropdown(self, Event):
        #ITEM SELECT:
        self.type_entry_query = self.food_names_list[self.type_entry.get()]
        self.items = self.df.query("types == @self.type_entry_query")
        self.food_names_list = set(self.items["title"])
        self.food_names_dropdown.config(self.frame_vars, self.entry_name, *self.food_items_list) 
      

    def save_item(self):
        self.expire = self.entry_date + datetime.timedelta(days=int(self.df["expiration (d)"]))
        self.notify = self.expire - datetime.timedelta(days=int(self.df["notify (d)"]))
        self.new_row = {"title":self.entry_name, "type":self.type_entry, "amount":self.servings_entry, "entry date":self.entry_date, "notify (days)": self.notify, "expiration (days)": self.expire}

        self.df_user = self.df_user.append(self.new_row, ignore_index=True)

    def erase_all(self):
        self.type_entry.set("Please select type")
        self.entry_name.set("Please select type first")
        self.servings_entry.set("Please select servings count")

#print(name)

e = Add(master)
master.mainloop()