
from os import name
import pandas as pd 
import datetime
from tkinter import * 
from tkcalendar import *
import tksheet

from class_food import Food
from class_entry_food import Entry_Food



master = Tk()
master.title("FoneFridge")
canvas = Canvas(master, bg="#FCF0E4", height=750, width=750)
canvas.pack()

class Edit(object):
    def __init__(self, master):
        app_frame = Frame(master)
        app_frame.pack() #geometry CHECK GUI LECTURE

        #visual part(no function):
        #top title frame
        self.frame_top = Frame(master, bg="#A9B6BE")
        self.frame_top.place(relx=0.01, rely=0.01, relheight=0.1, relwidth=0.98)

        #changing BOTTOM frame:
        self.frame_edit = Frame(master, bg="#576566")
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
        self.title = Label(self.frame_edit, bg="#576566", text= "INVENTORY", font="roboto 15")
        self.title.place(relx=0.5, rely=0.01, anchor="n")


        self.user_inventory = tksheet.Sheet(self.frame_edit, data=self.df_user, height=500, width=700)
        self.user_inventory.place(relx=0.5, rely=0.1, anchor="n")
        self.user_inventory.enable_bindings(("single_select", "row_select", "column_width_resize", "arrowkeys", "right_click_popup_menu", "rc_select", "rc_insert_row", "rc_delete_row", "copy", "cut", "paste", "delete", "undo", "edit_cell"))

        self.user_inventory.highlight_rows(rows=[0], bg="#C2D7D0", fg=None, highlight_index=True, redraw=False)




    #def Store_name(self):
        #name = return self.name

#print(name)

e = Edit(master)

master.mainloop()