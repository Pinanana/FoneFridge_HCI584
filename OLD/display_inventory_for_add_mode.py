from os import name
from tkinter.ttk import Style, Treeview
import pandas as pd 
import datetime
from tkinter import * 
from tkcalendar import *
from tksheet import *

from class_food import Food
from class_entry_food import Entry_Food


#  style things:
#main title = 22
#other titles = 15
#text = 11
#bg="#FCF0E4"
#dark pink ="#BE796D" (display box)
#purple blue ="#A9B6BE" (main title ribbon)
#light pink="#E9BFA7" (add box)
#light green blue ="#C2D7D0" 
#dark yellow ="#BA8E47" 
#dark gray blue ="#576566" (edit box)



master = Tk()
master.title("FoneFridge")
canvas = Canvas(master, bg="#FCF0E4", height=750, width=750)
canvas.pack()


class Display_items(object):
    def __init__(self, master):
        self.df = pd.read_csv("popular_items_library.csv")
        self.df_user = pd.read_csv("user_items.csv")

        app_frame = Frame(master)
        app_frame.pack() #geometry CHECK GUI LECTURE

        self.frame_top = Frame(master, bg="#A9B6BE")
        self.frame_top.place(relx=0.01, rely=0.01, relheight=0.06, relwidth=0.98)
        
        #-----------------------------------------------ADD MODE DISPLAY HALF-------------------------------------------------------

        #bottom frame
        self.frame_bottom = Frame(master, bg="#BE796D")
        self.frame_bottom.place(relx=0.01, rely=0.5, relheight=0.49, relwidth=0.98)

        #Display user item inventory:
        self.title_inventory = Label(self.frame_bottom, bg="#BE796D", text= "YOUR ITEMS", font="roboto 15")
        self.title_inventory.place(relx=0.5, anchor="n")

        #treeview style:

        #self.today_items = self.df_user.query("entry date == @self.entry_date")

        self.style_tw = Style()
        self.style_tw.theme_use("default")
        self.style_tw.configure("Treeview", foreground="black", rowheight=25, fieldbackground="#FCF0E4")
        self.style_tw.map("Treeview")

        #treeview item display:
        self.user_inventory = Treeview(self.frame_bottom)
        self.user_inventory.place(rely=0.1, relx=0.5, relwidth=0.98, relheight=0.88, anchor="n")

        self.user_inventory["column"] = list(self.df_user.columns)
        self.user_inventory["show"] = "headings"

        self.user_inventory.column("#0", width=0)
        self.user_inventory.column("title", width=97)
        self.user_inventory.column("type", width=97)
        self.user_inventory.column("amount", width=97)
        self.user_inventory.column("entry date", width=140)
        self.user_inventory.column("notify (days)", width=140)
        self.user_inventory.column("expiration (days)", width=140)

        self.user_inventory.heading("#0", text="")
        self.user_inventory.heading("title", text="TITLE", anchor="w")
        self.user_inventory.heading("type", text="TYPE", anchor="w")
        self.user_inventory.heading("amount", text="SERVINGS", anchor="w")
        self.user_inventory.heading("entry date", text="ENTRY DATE", anchor="w")
        self.user_inventory.heading("notify (days)", text="NOTIFICATION DAY", anchor="w")
        self.user_inventory.heading("expiration (days)", text="EXPIRATION DAY", anchor="w")

        self.df_user_rows = self.df_user.to_numpy().tolist()
        for row in self.df_user_rows:
            self.user_inventory.insert("", "end", values=row)

        #scrollbar
        self.inv_scroll = Scrollbar(self.frame_bottom, orient=VERTICAL, command=self.user_inventory.yview)
        self.user_inventory.config(yscrollcommand=self.inv_scroll.set)
        self.inv_scroll.place(relx=0.99, rely=0.54, relheight=0.87, anchor="e")

        #highlight recent rows:
        self.user_inventory.tag_configure("recent", background="#BA8E47")
        self.user_inventory.tag_configure("others", background="#FCF0E4")



        
e = Display_items(master)

master.mainloop()