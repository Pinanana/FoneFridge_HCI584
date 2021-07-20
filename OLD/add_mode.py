
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
        
        #read .csv files here:
        self.df = pd.read_csv("popular_items_library.csv")
        self.df_user = pd.read_csv("user_items.csv")

        #-----------------------------------------ADD MODE UPPER HALF-------------------------------------------
        #middle frame
        self.frame_middle = Frame(master, bg="#E9BFA7")
        self.frame_middle.place(relx=0.01, rely=0.08, relheight=0.49, relwidth=0.98)

        #food name search title--------Search the name of your item:
        self.title = Label(self.frame_middle, bg="#E9BFA7", text= "Search the name of your item:", font="roboto 15")
        self.title.place(relx=0.03)
        #search variables' frame
        self.frame_vars = Frame(self.frame_middle, bg="#FCF0E4")
        self.frame_vars.place(relx=0.01, rely=0.1, relheight=0.28, relwidth=0.98)


        #TYPE SELECT:
        self.type_label = Label(self.frame_vars, text="Select type:" ,bg="#FCF0E4", font="roboto 11")
        self.type_label.place(relx=0.2, rely=0.05, relwidth=0.27, anchor="n")

        #making sure types show 1 time
        self.food_types = list(self.df["types"])
        self.food_type_list = []
        for i in self.food_types:
            if i not in self.food_type_list:
                self.food_type_list.append(i)

        #self.food_type_dropdown = OptionMenu(self.frame_vars, self.type_entry, *self.food_type_list, command=self.generate_item_dropdown)
        self.food_type_dropdown = Combobox(self.frame_vars, value=self.food_type_list)
        self.food_type_dropdown.place(relx=0.2, rely=0.3, relwidth=0.27, anchor="n")

        #bind:
        self.food_type_dropdown.bind("<<ComboboxSelected>>", self.generate_item_dropdown)


        #ITEM SELECT:
        self.item_label = Label(self.frame_vars, text="Select item:" ,bg="#FCF0E4", font="roboto 11")
        self.item_label.place(relx=0.5, rely=0.05, relwidth=0.27, anchor="n")
        
        #self.food_names_dropdown = OptionMenu(self.frame_vars, self.entry_name, "none") 
        self.food_names_dropdown = Combobox(self.frame_vars, value=[" "])
        self.food_names_dropdown.place(relx=0.5, rely=0.3, relwidth=0.27, anchor="n")


        #SERVINGS SELECT:
        self.serv_label = Label(self.frame_vars, text="Servings amount:" ,bg="#FCF0E4", font="roboto 11")
        self.serv_label.place(relx=0.8, rely=0.05, relwidth=0.27, anchor="n")

        self.servings_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        #self.servings_dropdown = OptionMenu(self.frame_vars, self.servings_entry, *self.servings_list)
        self.servings_dropdown = Combobox(self.frame_vars, value=self.servings_list)
        self.servings_dropdown.place(relx=0.8, rely=0.3, relwidth=0.27, anchor="n")


        #PREVIEW BUTTON:
        self.preview_button = Button(self.frame_vars, text="PREVIEW SELECTED ITEM", command=self.show_the_item)
        self.preview_button.place(relx=0.5, rely=0.65, anchor="n")
        
        #printing results:
        self.frame_results = Frame(self.frame_middle, bg="#BE796D")
        self.frame_results.place(relx=0.01, rely=0.4, relheight=0.45, relwidth=0.98)

        self.result = Label(self.frame_results, justify="left", bg="#BE796D", font="roboto 15")
        self.result.grid(row=0, column=0, padx=2, pady=5, sticky=W)
        self.result2 = Label(self.frame_results, justify="left", bg="#BE796D", font="roboto 11")
        self.result2.grid(row=1, column=0, padx=2, pady=2, sticky=W)
        self.result3 = Label(self.frame_results, justify="left", bg="#BE796D", font="roboto 11")
        self.result3.grid(row=2, column=0, padx=2, pady=2, sticky=W)
        self.result4 = Label(self.frame_results, justify="left", bg="#BE796D", font="roboto 11")
        self.result4.grid(row=3, column=0, padx=2, pady=2, sticky=W)

        #SAVE button:
        self.save_button = Button(self.frame_middle, width=10, text="SAVE", command=self.save_item)
        self.save_button.place(relx=0.4, rely=0.9, anchor="n")

        #DISCARD button:
        self.discard_button = Button(self.frame_middle, width=10, text="DISCARD", command=self.clear_all)
        self.discard_button.place(relx=0.6, rely=0.9, anchor="n")

        #-----------------------------------------ADD MODE UPPER HALF-------------------------------------------

    #========================ADD MODE TOP FRAME FUNCTIONS===========================
    
    def show_the_item(self):
        self.result.configure(text="Here is the result for "+self.food_names_dropdown.get()+":")
        self.result2.configure(text=Food.display_food(Food(self.food_names_dropdown.get())))
        self.result3.configure(text=Food.display_expire(Food(self.food_names_dropdown.get())))
        self.result4.configure(text=Food.display_notify(Food(self.food_names_dropdown.get())))


    def generate_item_dropdown(self, e):
        self.items_df = self.df.query("types == @self.food_type_dropdown.get()")
        self.food_names_list = list(self.items_df["title"])
        self.food_names_dropdown.config(value=self.food_names_list) 
      

    def save_item(self):
        self.expire = self.entry_date + datetime.timedelta(days=int(self.df["expiration (d)"]))
        self.notify = self.expire - datetime.timedelta(days=int(self.df["notify (d)"]))
        self.new_row = {"title":self.food_names_dropdown.get(), "type":self.food_type_dropdown.get(), "amount":self.servings_dropdown.get(), "entry date":self.entry_date, "notify (days)": self.notify, "expiration (days)": self.expire}

        self.df_user = self.df_user.append(self.new_row, ignore_index=True)

    def clear_all(self):
        self.food_type_dropdown.set("")
        self.food_names_dropdown.set("")
        self.servings_dropdown.set("")

    

#print(name)

e = Add(master)
master.mainloop()