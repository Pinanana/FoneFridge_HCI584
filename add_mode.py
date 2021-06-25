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

class Add(Fonefridge):
    def __init__(self, master):
        self.df = pd.read_csv("popular_items_library.csv")
        
        app_frame = Frame(master)
        app_frame.pack() #geometry CHECK GUI LECTURE

        #visual part(no function):
        #AREAS:

        #top title frame
        self.frame_top = Frame(master, bg="#A9B6BE")
        self.frame_top.place(relx=0.01, rely=0.01, relheight=0.1, relwidth=0.98)


        # ADD MODE DESIGN

        #middle frame 
        self.frame_middle = Frame(master, bg="#E9BFA7")
        self.frame_middle.place(relx=0.01, rely=0.01, relheight=0.43, relwidth=0.98)

        #bottom frame
        self.frame_bottom = Frame(master, bg="#BE796D")
        self.frame_bottom.place(relx=0.01, rely=0.44, relheight=0.43, relwidth=0.98)


        #food name search title-Search the name of your item:
        self.title = Label(self.frame_middle, bg="#E9BFA7", text= "Search the name of your item:", font="roboto 15")
        self.title.pack(pady=5)




        #TYPE SELECT:
        self.food_type_list = self.df["types"]

        self.type_entry = StringVar(self.frame_middle)
        self.type_entry.set("Please select type")

        self.food_type_dropdown = OptionMenu(self.frame_middle, self.type_entry, self.food_type_list, command=generate_item_dropdown) 
        self.food_type_dropdown.pack(padx=5, pady=5, side=LEFT)

        #ITEM SELECT:
        
        self.entry_name = StringVar(self.frame_middle)
        self.entry_name.set("Please select type first")

        self.food_names_dropdown = OptionMenu(self.frame_middle, self.entry_name, self.food_items_list) 
        self.food_names_dropdown.pack(padx=5, pady=5, side=LEFT)


        #SERVINGS SELECT:
        self.servings_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.servings_entry = StringVar(self.frame_middle)
        self.servings_entry.set("Please select servings count")

        self.servings_dropdown = OptionMenu(self.frame_middle, self.servings_entry, self.servings_list)
        self.servings_dropdown.pack(padx=5, pady=5, side=LEFT)

        #selecting servings will trigger this:

        if self.servings_entry != "Please select servings count" and self.entry_name != "Please select name" and 
        #printing results:
        self.result = Label(self.frame_middle, justify="left", bg="#BE796D", font="roboto 15")
        self.result.grid(row=0, column=0, padx=2, pady=5, sticky=W)

        self.result2 = Label(self.frame_middle, justify="left", bg="#BE796D", font="roboto 11")
        self.result2.grid(row=1, column=0, padx=2, pady=2, sticky=W)

        self.result3 = Label(self.frame_middle, justify="left", bg="#BE796D", font="roboto 11")
        self.result3.grid(row=2, column=0, padx=2, pady=2, sticky=W)

        self.result4 = Label(self.frame_middle, justify="left", bg="#BE796D", font="roboto 11")
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

        self.items = self.df.query("type == @type_entry")
        self.food_names_list = self.items["title"]
        self.entry_name.set("Please select name")

    

    def save_item(self):
        
t = res["type"]
a = 3
today = datetime.datetime.today().date()
print(today)
expire = datetime.timedelta(days=int(res["expiration (days)"]))
notify = datetime.timedelta(days=int(res["notify (days)"]))

new_row = {"title":f, "type":t, "amount":a, "entry date":today, "notify (days)": today + expire - notify, "expiration (days)": today + expire}
df_user = df_user.append(new_row, ignore_index=True)

display(df_user)


    def erase_all(self):


    #my items display:
    

#print(name)

e = Fonefridge(master)

master.mainloop()