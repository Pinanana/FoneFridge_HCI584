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
      
        app_frame = Frame(master)
        app_frame.pack() #geometry CHECK GUI LECTURE

        #visual part(no function):
        #AREAS:
        #top title frame
        self.frame_top = Frame(master, bg="#A9B6BE")
        self.frame_top.place(relx=0.01, rely=0.01, relheight=0.1, relwidth=0.98)

        #middle frame 
        self.frame_middle = Frame(master, bg="#E9BFA7")
        self.frame_middle.place(relx=0.01, rely=0.12, relheight=0.87, relwidth=0.4)

        #bottom frame
        self.frame_bottom = Frame(master, bg="#BE796D")
        self.frame_bottom.place(relx=0.42, rely=0.12, relheight=0.87, relwidth=0.57)

        #TITLES:
        #main title-FONEFRIDGE
        self.title = Label(self.frame_top, bg="#A9B6BE", text= "FONEFRIDGE", font="roboto 22")
        self.title.pack(pady=14)

        #food name search title-Search the name of your item:
        self.title = Label(self.frame_middle, bg="#E9BFA7", text= "Search the name of your item:", font="roboto 15")
        self.title.pack(pady=5)




        #text entry slot
        self.entry_name = Entry(self.frame_middle, width=50)
        self.entry_name.pack(padx=10, pady=5)

        self.search_button = Button(self.frame_middle, text="Search", command=self.display_item)
        self.search_button.pack(padx=10, pady=5)

        #printing results:
        self.result = Label(self.frame_bottom, justify="left", bg="#BE796D", font="roboto 15")
        self.result.grid(row=0, column=0, padx=2, pady=5, sticky=W)

        self.result2 = Label(self.frame_bottom, justify="left", bg="#BE796D", font="roboto 11")
        self.result2.grid(row=1, column=0, padx=2, pady=2, sticky=W)

        self.result3 = Label(self.frame_bottom, justify="left", bg="#BE796D", font="roboto 11")
        self.result3.grid(row=2, column=0, padx=2, pady=2, sticky=W)

        self.result4 = Label(self.frame_bottom, justify="left", bg="#BE796D", font="roboto 11")
        self.result4.grid(row=3, column=0, padx=2, pady=2, sticky=W)

    def display_item(self):
        self.result.config(text="Here is the result for "+self.entry_name.get()+":")
        self.result2.config(text=Food.display_food(Food(self.entry_name.get())))
        self.result3.config(text=Food.display_expire(Food(self.entry_name.get())))
        self.result4.config(text=Food.display_notify(Food(self.entry_name.get())))
    


    #def Store_name(self):
        #name = return self.name

#print(name)

e = Fonefridge(master)

master.mainloop()