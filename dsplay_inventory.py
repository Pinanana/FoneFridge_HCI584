from os import name
from tkinter.ttk import Treeview
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


class Display_items(object):
    def __init__(self, master):
        self.df = pd.read_csv("popular_items_library.csv")
        self.df_user = pd.read_csv("user_items.csv")

        app_frame = Frame(master)
        app_frame.pack() #geometry CHECK GUI LECTURE

        self.frame_top = Frame(master, bg="#A9B6BE")
        self.frame_top.place(relx=0.01, rely=0.01, relheight=0.06, relwidth=0.98)
        
        #middle frame 
        self.frame_middle = Frame(master, bg="#E9BFA7")
        self.frame_middle.place(relx=0.01, rely=0.08, relheight=0.41, relwidth=0.98)
        
        #bottom frame
        self.frame_bottom = Frame(master, bg="#BE796D")
        self.frame_bottom.place(relx=0.01, rely=0.5, relheight=0.49, relwidth=0.98)

        #------------------------------------------------------------------------------------
        #Display user item inventory:
        self.title_inventory = Label(self.frame_bottom, bg="#BE796D", text= "Your inventory:", font="roboto 15")
        self.title_inventory.place(relx=0.03)

        #showing the table w tksheet:
        #self.user_inventory = tksheet.Sheet(self.frame_bottom, data=self.df_user, height=360, width=730)
        #self.user_inventory.place(relx=0.01, rely=0.1)
        #self.user_inventory.enable_bindings(("single_select", "row_select", "column_width_resize", "arrowkeys", "right_click_popup_menu", "rc_select", "rc_insert_row", "rc_delete_row", "copy", "cut", "paste", "delete", "undo", "edit_cell"))

        #self.user_inventory.highlight_rows(rows=[0], bg="#C2D7D0", fg=None, highlight_index=True, redraw=False)

        
        #showing the table w treeview:
        self.user_inventory = Treeview(self.frame_bottom, columns=)




e = Display_items(master)

master.mainloop()