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
    """Class Edit is the EDIT mode of FoneFridge desktop app where the user can see their items and delete or change amount. 
    The expired items have dark pink background, about tp expire items have medium pink background, okay to use items have beige background.
    Editing functions work with doubleclick and the editing tools dissapear anytime something is changed. 
    
    PLEASE make sure your Tk version is higher than 8.6.10.
    """
    def __init__(self, master):

        #---------------------------------------------GENERAL-------------------------------------------------
        #reading the .csv files here:
        self.df = pd.read_csv("popular_items_library.csv")
        self.df_user = pd.read_csv("user_items.csv")
        #making the app frame:
        app_frame = Frame(master)
        app_frame.pack()
        #---------------------------------------------GENERAL-------------------------------------------------

        #---------------------------------------------TOP RIBBON-------------------------------------------------
        #top title frame
        self.frame_top = Frame(master, bg="#A9B6BE")
        self.frame_top.place(relx=0.01, rely=0.01, relheight=0.056, relwidth=0.98)

        # MAIN TITLE:
        self.title = Label(self.frame_top, bg="#A9B6BE", text= "FONEFRIDGE", font="roboto 22")
        self.title.grid(column=1, row=0, ipadx=151)

        # MODE SWITCH:
        self.add_button = Button(self.frame_top, width=10, text="ADD MODE", font="roboto 15", bg="#A9B6BE",command=self.change_mode)
        self.add_button.grid(column=0, row=0, ipadx=5)

        #---------------------------------------------TOP RIBBON-------------------------------------------------

        #---------------------------------------------EDIT BODY-------------------------------------------------
        #DISPLAY FRAME:
        self.frame_edit = Frame(master, bg="#576566")
        self.frame_edit.place(relx=0.01, rely=0.08, relheight=0.81, relwidth=0.98)

        # EDIT MODE DESIGN

        #TITLES:
        #food name search title-Search the name of your item:
        self.title = Label(self.frame_edit, bg="#576566", text= "EDIT INVENTORY", font="roboto 15")
        self.title.place(relx=0.5, rely=0.01, anchor="n")

        self.sub_title = Label(self.frame_edit, bg="#576566", text="Double click on an item to edit.", font="roboto 11")
        self.sub_title.place(relx=0.5, rely=0.05, anchor="n")

         #TREEVIEW:
        #PLEASE MAKE SURE YOUR Tk VERSION IS HIGHER THAN 8.6.10!!

        # treeview style:
        self.style_tw = Style()
        self.style_tw.theme_use("default")
        self.style_tw.configure("Treeview", foreground="black", rowheight=25, fieldbackground="#FCF0E4", background=("#FCF0E4"))
        self.style_tw.map("Treeview", foreground=[("selected", "#576566")], background=[("selected", "#C2D7D0")])

        #treeview item display:
        self.user_inventory = Treeview(self.frame_edit, selectmode=BROWSE)
        self.user_inventory.place(rely=0.1, relx=0.5, relwidth=0.98, relheight=0.88, anchor="n")
        #getting the columns from user_items.csv file (self.df_user is the dataframe containing it)
        self.user_inventory["column"] = list(self.df_user.columns)
        self.user_inventory["show"] = "headings" # #0 column doesn't show when this line works.
        #creating the columns:
        self.user_inventory.column("#0", width=40)
        self.user_inventory.column("title", width=95)
        self.user_inventory.column("type", width=95)
        self.user_inventory.column("amount", width=55)
        self.user_inventory.column("entry date", width=140)
        self.user_inventory.column("notify (days)", width=140)
        self.user_inventory.column("expiration (days)", width=140)
        #creating the headings:
        self.user_inventory.heading("#0", text="-")
        self.user_inventory.heading("title", text="TITLE", anchor="w")
        self.user_inventory.heading("type", text="TYPE", anchor="w")
        self.user_inventory.heading("amount", text="SERVINGS", anchor="w")
        self.user_inventory.heading("entry date", text="ENTRY DATE", anchor="w")
        self.user_inventory.heading("notify (days)", text="NOTIFICATION DAY", anchor="w")
        self.user_inventory.heading("expiration (days)", text="EXPIRATION DAY", anchor="w")

        #for edit page today is set to datetime.today
        self.today = datetime.datetime.today().date().strftime("%Y-%m-%d")

        # tags:
        self.user_inventory.tag_configure("expired", background="#BE796D")
        self.user_inventory.tag_configure("notified", background="#E9BFA7")
        self.user_inventory.tag_configure("others", background="#FCF0E4")

        #inserting the values:
        #expired:
        self.df_expired = self.df_user.loc[self.df_user["expiration (days)"] <= self.today]
        self.df_expired_rows = self.df_expired.to_numpy().tolist()
        for row in self.df_expired_rows:
            self.user_inventory.insert("", "end", values=row, tags=("expired", ))
        #notified:
        self.df_noti = self.df_user.loc[self.df_user["notify (days)"] <= self.today]
        self.df_notify = pd.concat([self.df_noti, self.df_expired]).drop_duplicates(keep=False)
        self.df_expired_rows = self.df_expired.to_numpy().tolist()
        for row in self.df_expired_rows:
            self.user_inventory.insert("", "end", values=row, tags=("notified", ))
        #rest of the items:
        self.df_rest_of_items = self.df_user.loc[self.df_user["notify (days)"] > self.today]
        self.df_user_rows = self.df_user.to_numpy().tolist()
        for row in self.df_user_rows:
            self.user_inventory.insert("", "end", values=row, tags=("others", ))
        

        #scrollbar
        self.inv_scroll = Scrollbar(self.frame_edit, orient=VERTICAL, command=self.user_inventory.yview)
        self.user_inventory.config(yscrollcommand=self.inv_scroll.set)
        self.inv_scroll.place(relx=0.99, rely=0.54, relheight=0.87, anchor="e")

        #edit & delete--------------------
        self.user_inventory.bind("<Double-1>", self.edit_tools)
        
        #---------------------------------------------EDIT BODY-------------------------------------------------

        #---------------------------------------------EDIT BUTTONS-------------------------------------------------

        #the bottom
        self.bottom_frame = Frame(master, bg="#576566")
        self.bottom_frame.place(relx=0.01, rely=0.89, relheight=0.1, relwidth=0.98)
        #since the initial condition doesn't have any selection, the message requests a selection.
        self.changing_item_label = Label(self.bottom_frame, bg="#576566", text="Please double click on the item you want to edit.", font="roboto 15")
        self.changing_item_label.place(relx=0.5, rely=0.01, anchor="n")

        #---------------------------------------------EDIT BUTTONS-------------------------------------------------

    #==============================DEFS=====================
    def change_mode(self):
        """change_mode function closes one mode window and opens the other one.
        In edit mode, it closes edit mode and runs add mode.
        Args:
            none
        Returns:
            the add mode window.
        Raises:
            none
        """
        master.destroy()
        os.system("add_mode_run.py")

    def edit_tools(self, e):
        """This function creates the delete button, servings selection dropdown menu, and change amount button.
        Once the user double clicks on an item these widgets populate the bottom part with a title telling which item added when.

        This function also catches the selection by .selection() function. 
        Then the 0th item in the values list of that item is compared with names of the user_items.csv file (self.df_same_name).
        Since there can be multiple items with the same name the entry date is also compared. 
        Once the item is found, the index number is stored in self.index_select_number variable for later uses.
        Args:
            e: doubleclick on an item
        Returns:
            the editing tools: self.delete_but (button), self.serv_drop (dropdown menu), and self.serv_but (button)
        Raises:
            none
        """
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

        
        self.serv_but = Button(self.bottom_frame, text="CHANGE AMOUNT", command=self.change_amount_button, state="disabled")
        self.serv_but.place(relx=0.9, rely=0.7, relwidth=0.28, anchor="e")

        self.serv_drop.bind("<<ComboboxSelected>>", self.activate_button)

    def activate_button(self, e):
        """To prevent user error if they click on change amount without selecting amount, the button is originally disabled. 
        This function only changes the state of the button from disabled to normal.
        Args:
            e: selection in derv_drop dropdown menu
        Returns:
            self.serv_but button is usable now
        Raises:
            none
        """
        self.serv_but.config(state="normal")


    def delete_button(self):
        """once the delete button is clicked, a user error preventing pop up appears. 
        Args:
            clicking self.delete_but
        Returns:
            self.pop_up_del that asks the user if they are sure to delete.
        Raises:
            none
        """
        self.pop_up_del = Toplevel(master)
        self.pop_up_del.geometry("500x50")

        self.del_label = Label(self.pop_up_del, text="Are you sure you want to delete this item?", font="roboto 12")
        self.del_label.place(relx=0.5, rely=0.01, anchor="n")

        self.del_button = Button(self.pop_up_del, text="DELETE", command=self.delete_item)
        self.del_button.place(relx=0.4, rely=0.5, anchor="n")

        self.keep_button = Button(self.pop_up_del, text="CANCEL", command=self.close_1)
        self.keep_button.place(relx=0.6, rely=0.5, anchor="n")

    def change_amount_button(self):
        """once the change amount button is clicked, a user error preventing pop up appears.
        In the message the original amount and new amount are stated. 
        Args:
            clicking self.serv_but
        Returns:
            self.pop_up_amount that asks if they want to change amount from self.select_amo to self.drop.get()
        Raises:
            none
        """
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
        """If the user clicks delete in the self.pop_up_del window, the item is dropped from the user_items.csv file. 
        From the edit_tool function, the selection index number was stored in self.index_select_num.
        That number is used to drop that exact item from the user_items.csv file.
        After deleting the item, the treeview is updated, the title goes back to no selection condition, buttons and dropdown menu are removed, and finally the pop up window gets closed. 
        Args:
            clicking self.del_button
        Returns:
            updated .csv file
            editing tools are removed
            self.update_treeview()
        Raises:
            none
        """
        self.df_user.drop(self.index_select_number, inplace=True)
        self.df_user.to_csv("user_items.csv", index=False)
        self.update_treeview()
        self.changing_item_label.config(text="Please double click on the item you want to edit.")
        self.delete_but.destroy()
        self.serv_drop.destroy()
        self.serv_but.destroy()
        self.close_1()

    def change_amount_incsv(self):
        self.df_user.loc[self.index_select_number, "amount"] = self.serv_drop.get()
        self.df_user.to_csv("user_items.csv", index=False)
        self.update_treeview()
        self.changing_item_label.config(text="Please double click on the item you want to edit.")
        self.delete_but.destroy()
        self.serv_drop.destroy()
        self.serv_but.destroy()
        self.close_2()

    def close_1(self):
        self.pop_up_del.destroy()

    def close_2(self):
        self.pop_up_amount.destroy()

    def update_treeview(self):
        for i in self.user_inventory.get_children():
            self.user_inventory.delete(i)
            
        #expired:
        self.df_expired = self.df_user.loc[self.df_user["expiration (days)"] <= self.today]
        self.df_expired_rows = self.df_expired.to_numpy().tolist()
        for row in self.df_expired_rows:
            self.user_inventory.insert("", "end", values=row, tags=("expired", ))

        #notified:
        self.df_noti = self.df_user.loc[self.df_user["notify (days)"] <= self.today]
        self.df_notify = pd.concat([self.df_noti, self.df_expired]).drop_duplicates(keep=False)
        self.df_expired_rows = self.df_expired.to_numpy().tolist()
        for row in self.df_expired_rows:
            self.user_inventory.insert("", "end", values=row, tags=("notified", ))

        #rest of the items:
        self.df_rest_of_items = self.df_user.loc[self.df_user["notify (days)"] > self.today]
        self.df_user_rows = self.df_user.to_numpy().tolist()
        for row in self.df_user_rows:
            self.user_inventory.insert("", "end", values=row, tags=("others", ))


e = Edit(master)

master.mainloop()