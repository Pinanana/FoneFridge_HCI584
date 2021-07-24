from os import name
import pandas as pd 
from tkinter.ttk import Combobox, Style, Treeview
import datetime
from tkinter import *
from tkcalendar import *
import sys
import os



master = Tk()
master.title("FoneFridge")
canvas = Canvas(master, bg="#FCF0E4", height=750, width=750)
canvas.pack()

class Edit(object):
    def __init__(self, master):
        app_frame = Frame(master)
        app_frame.pack() #geometry CHECK GUI LECTURE
        #---------------------------------------------TOP RIBBON-------------------------------------------------
        #top title frame
        self.frame_top = Frame(master, bg="#A9B6BE")
        self.frame_top.place(relx=0.01, rely=0.01, relheight=0.056, relwidth=0.98)

        # MAIN title-FONEFRIDGE------------
        self.title = Label(self.frame_top, bg="#A9B6BE", text= "FONEFRIDGE", font="roboto 22")
        self.title.grid(column=1, row=0, ipadx=151)

        # MODES--------
        #button variable:
        self.add_button = Button(self.frame_top, width=10, text="ADD MODE", font="roboto 15", bg="#A9B6BE",command=self.change_mode)
        self.add_button.grid(column=0, row=0, ipadx=5)
        self.is_add = False

        #---------------------------------------------TOP RIBBON-------------------------------------------------

        #---------------------------------------------EDIT BODY-------------------------------------------------
        #changing BOTTOM frame:
        self.frame_edit = Frame(master, bg="#576566")
        self.frame_edit.place(relx=0.01, rely=0.08, relheight=0.81, relwidth=0.98)


        #read .csv files here:
        self.df = pd.read_csv("popular_items_library.csv")
        self.df_user = pd.read_csv("user_items.csv")
        

        # EDIT MODE DESIGN

        #TITLES:
        #food name search title-Search the name of your item:
        self.title = Label(self.frame_edit, bg="#576566", text= "EDIT INVENTORY", font="roboto 15")
        self.title.place(relx=0.5, rely=0.01, anchor="n")

        
        self.style_tw = Style()
        self.style_tw.theme_use("default")
        self.style_tw.configure("Treeview", foreground="black", rowheight=25, fieldbackground="#FCF0E4", background="#FCF0E4")
        self.style_tw.map('Treeview', foreground=self.fixed_map('foreground'), background=self.fixed_map('background'))

        #treeview item display:
        self.user_inventory = Treeview(self.frame_edit)
        self.user_inventory.place(rely=0.1, relx=0.5, relwidth=0.98, relheight=0.88, anchor="n")

        self.user_inventory["column"] = list(self.df_user.columns)
        #self.user_inventory["show"] = "headings" #now #0 column shows.

        #MAKE NEW COLUMN CALLED "-"
        #THEN MAKE EMPTY FOR EVERYTHING BUT "X" FOR SELECTED
        self.user_inventory.column("#0", width=10)
        self.user_inventory.column("title", width=95)
        self.user_inventory.column("type", width=95)
        self.user_inventory.column("amount", width=95)
        self.user_inventory.column("entry date", width=140)
        self.user_inventory.column("notify (days)", width=140)
        self.user_inventory.column("expiration (days)", width=140)

        self.user_inventory.heading("#0", text="-")
        self.user_inventory.heading("title", text="TITLE", anchor="w")
        self.user_inventory.heading("type", text="TYPE", anchor="w")
        self.user_inventory.heading("amount", text="SERVINGS", anchor="w")
        self.user_inventory.heading("entry date", text="ENTRY DATE", anchor="w")
        self.user_inventory.heading("notify (days)", text="NOTIFICATION DAY", anchor="w")
        self.user_inventory.heading("expiration (days)", text="EXPIRATION DAY", anchor="w")



        #for edit page where users won't see notifications, today is set to datetime.today
        self.today = datetime.datetime.today().date().strftime("%Y-%m-%d")
        #expired:
        self.user_inventory.tag_configure("expired", background="#BE796D")
        self.df_expired = self.df_user.loc[self.df_user["expiration (days)"] <= self.today]
        self.df_expired_rows = self.df_expired.to_numpy().tolist()
        for row in self.df_expired_rows:
            self.user_inventory.insert("", "end", values=row, tags=("expired", ))

        #notified:
        self.user_inventory.tag_configure("notified", background="#E9BFA7")
        self.df_noti = self.df_user.loc[self.df_user["notify (days)"] <= self.today]
        self.df_notify = pd.concat([self.df_noti, self.df_expired]).drop_duplicates(keep=False)
        self.df_expired_rows = self.df_expired.to_numpy().tolist()
        for row in self.df_expired_rows:
            self.user_inventory.insert("", "end", values=row, tags=("notified", ))

        #rest of the items:
        self.user_inventory.tag_configure("others", background="#FCF0E4")
        self.df_rest_of_items = self.df_user.loc[self.df_user["notify (days)"] > self.today]
        self.df_user_rows = self.df_user.to_numpy().tolist()
        for row in self.df_user_rows:
            self.user_inventory.insert("", "end", values=row, tags=("others", ))


        #scrollbar
        self.inv_scroll = Scrollbar(self.frame_edit, orient=VERTICAL, command=self.user_inventory.yview)
        self.user_inventory.config(yscrollcommand=self.inv_scroll.set)
        self.inv_scroll.place(relx=0.99, rely=0.54, relheight=0.87, anchor="e")

        #edit & delete pop up--------------------
        self.user_inventory.bind("<Double-1>", self.edit_tools)
        
        self.user_inventory.tag_configure("selected", background="#C2D7D0")
        #self.user_inventory.bind("<<TreeviewSelect>>", self.highlight)
        #---------------------------------------------EDIT BODY-------------------------------------------------

        #---------------------------------------------EDIT BOTTOMS-------------------------------------------------

        #the bottom
        self.bottom_frame = Frame(master, bg="#576566")
        self.bottom_frame.place(relx=0.01, rely=0.89, relheight=0.1, relwidth=0.98)

        self.changing_item_label = Label(self.bottom_frame, bg="#576566", text="Please double click on the item you want to edit.", font="roboto 15")
        self.changing_item_label.place(relx=0.5, rely=0.01, anchor="n")

        #---------------------------------------------EDIT BOTTOMS-------------------------------------------------

    
    #ttk version 8.6 apparently has a bug that makes background etc. doesn't work.
    #I found this def from https://core.tcl-lang.org/tk/tktview?name=509cafafae 
    def fixed_map(self, e):
        return [elm for elm in self.style_tw.map('Treeview', query_opt=self) if elm[:2] != ('!disabled', '!selected')]

    #==============================DEFS=====================
    def change_mode(self):
        master.destroy()
        os.system("add_mode_run.py")

    def highlight(self, e):
        self.previous_tag = self.user_inventory.item(self.user_inventory.focus())["tags"]
        print(self.previous_tag)
        #self.selected_item_tag = "select"
        self.user_inventory.item(self.user_inventory.focus(), tags="selected")
        self.selects = list(self.user_inventory.tag_has("selected"))
        print(self.selects)
    
    def edit_tools(self, e):
        #GETTING SELECTION
        self.selected_item = self.user_inventory.selection()

        self.select_name = self.user_inventory.item([i for i in self.selected_item], "values")[0]
        self.select_entdate = self.user_inventory.item([i for i in self.selected_item], "values")[3]

        self.df_same_name = self.df_user.query("title == @self.select_name")
        #this is the selected one for sure
        self.df_the_selected_item = self.df_same_name.loc[self.df_same_name["entry date"] == self.select_entdate]

        #GETTING THE INDEX NUMBER OF THE SELECTION IN .CSV FILE
        self.index_select = self.df_the_selected_item.index
        self.index_select_number = self.index_select.tolist()

        #bottom buttons appear:
        self.changing_item_label.config(text="Now editing "+self.select_name+" that added on "+self.select_entdate+":")

        self.delete_but = Button (self.bottom_frame, text="DELETE", command=self.delete_button)
        self.delete_but.place(relx=0.1, rely=0.7, relwidth=0.28, anchor="w")

        self.servings_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.serv_drop = Combobox(self.bottom_frame, value=self.servings_list, state="readonly")
        self.serv_drop.place(relx=0.5, rely=0.7, relwidth=0.2, anchor=CENTER)

        self.serv_but = Button(self.bottom_frame, text="CHANGE AMOUNT", command=self.change_amount_button)
        self.serv_but.place(relx=0.9, rely=0.7, relwidth=0.28, anchor="e")

    def delete_button(self):
        self.pop_up_del = Toplevel(master)
        self.pop_up_del.geometry("500x50")

        self.del_label = Label(self.pop_up_del, text="Are you sure you want to delete this item?", font="roboto 12")
        self.del_label.place(relx=0.5, rely=0.01, anchor="n")

        self.del_button = Button(self.pop_up_del, text="DELETE", command=self.delete_item)
        self.del_button.place(relx=0.4, rely=0.5, anchor="n")

        self.keep_button = Button(self.pop_up_del, text="CANCEL", command=self.close_1)
        self.keep_button.place(relx=0.6, rely=0.5, anchor="n")

    def change_amount_button(self):
        self.pop_up_amount = Toplevel(master)
        self.pop_up_amount.geometry("500x50")

        self.select_amo = self.user_inventory.item([i for i in self.selected_item], "values")[2]

        self.del_label = Label(self.pop_up_amount, text="Are you sure you want to change servings amount from "+self.select_amo+" to "+self.serv_drop.get()+"?", font="roboto 12")
        self.del_label.place(relx=0.5, rely=0.01, anchor="n")

        self.del_button = Button(self.pop_up_amount, text="OK", command=self.change_amount_incsv)
        self.del_button.place(relx=0.4, rely=0.5, anchor="n")

        self.keep_button = Button(self.pop_up_amount, text="CANCEL", command=self.close_2)
        self.keep_button.place(relx=0.6, rely=0.5, anchor="n")
        

    def delete_item(self):
        self.df_user.drop(self.index_select_number, inplace=True)
        self.df_user.to_csv("user_items.csv", index=False)
        self.update_treeview()
        self.close_1()

    def change_amount_incsv(self):
        self.df_user.loc[self.index_select_number, "amount"] = self.serv_drop.get()
        self.df_user.to_csv("user_items.csv", index=False)
        self.update_treeview()
        self.close_2()

    def close_1(self):
        self.pop_up_del.destroy()

    def close_2(self):
        self.pop_up_amount.destroy()

    def update_treeview(self):
        for i in self.user_inventory.get_children():
            self.user_inventory.delete(i)
            
        #expired:
        self.user_inventory.tag_configure("expired", background="#BE796D")
        self.df_expired = self.df_user.loc[self.df_user["expiration (days)"] <= self.today]
        self.df_expired_rows = self.df_expired.to_numpy().tolist()
        for row in self.df_expired_rows:
            self.user_inventory.insert("", "end", values=row, tags=("expired", ))

        #notified:
        self.user_inventory.tag_configure("notified", background="#E9BFA7")
        self.df_noti = self.df_user.loc[self.df_user["notify (days)"] <= self.today]
        self.df_notify = pd.concat([self.df_noti, self.df_expired]).drop_duplicates(keep=False)
        self.df_expired_rows = self.df_expired.to_numpy().tolist()
        for row in self.df_expired_rows:
            self.user_inventory.insert("", "end", values=row, tags=("notified", ))

        #rest of the items:
        self.df_rest_of_items = self.df_user.loc[self.df_user["notify (days)"] > self.today]
        self.df_user_rows = self.df_user.to_numpy().tolist()
        for row in self.df_user_rows:
            self.user_inventory.insert("", "end", values=row)


e = Edit(master)

master.mainloop()