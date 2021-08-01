from os import name
import pandas as pd 
from tkinter.ttk import Combobox, Style, Treeview
import datetime
from tkinter import *
from tkcalendar import *
import sys
import os


#  TYPE & COLORS:

#main title = 22
#other titles = 15
#text = 11 or 9
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

class Fonefridge(object):
    """
    Class FoneFridge is the ADD mode of FoneFridge desktop app. 
    In this class window, we see 3 main sections.
    Top ribbon:
        The title ribbon has mode changing button (change_mode(self)) and date selection calendar (calendar_get(self, e))
    Middle section:
        In the middle section of GUI there are 3 dropdown menus to get necessary information from the user to properly save their item.
        The notification message shows underneath those dropdown menus. 
        Item preview also shows in the same place. 
        The save and discard buttons are also in this section. 
    Bottom section:
        In the bottom section the user_items.csv file is previewed. 
        Recently added item is highlighted.
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
        self.add_button = Button(self.frame_top, width=10, text="EDIT MODE", font="roboto 15", bg="#A9B6BE",command=self.change_mode)
        self.add_button.grid(column=0, row=0, ipadx=5)
        self.is_add = True

        # CALENDAR:
        self.entry_cal = DateEntry(self.frame_top, background= "#A9B6BE", foreground= "#576566", state="readonly")
        self.entry_cal.grid(column=2, row=0, ipadx=5)
        self.entry_cal.bind("<<DateEntrySelected>>", self.calendar_get)

        #---------------------------------------------TOP RIBBON-------------------------------------------------
        
        #-----------------------------------------ADD MODE UPPER HALF-------------------------------------------
        #middle frame
        self.frame_middle = Frame(master, bg="#E9BFA7")
        self.frame_middle.place(relx=0.01, rely=0.08, relheight=0.49, relwidth=0.98)

        #TITLE
        #food name search title--------Search the name of your item:
        self.title = Label(self.frame_middle, bg="#E9BFA7", text= "-----PLEASE SELECT THE DATE FIRST-----", font="roboto 15")
        self.title.place(relx=0.5, anchor="n")
        #search variables' frame
        self.frame_vars = Frame(self.frame_middle, bg="#FCF0E4")
        self.frame_vars.place(relx=0.01, rely=0.1, relheight=0.28, relwidth=0.98)


        #TYPE SELECT:

        self.type_label = Label(self.frame_vars, text="Select type:" ,bg="#FCF0E4", font="roboto 11")
        self.type_label.place(relx=0.2, rely=0.05, relwidth=0.27, anchor="n")

        #making sure types show only 1 time
        self.food_types = list(self.df["types"])
        self.food_type_list = []
        for i in self.food_types:
            if i not in self.food_type_list:
                self.food_type_list.append(i)

        #type drop down:
        self.food_type_dropdown = Combobox(self.frame_vars, value=self.food_type_list, state="readonly")
        self.food_type_dropdown.place(relx=0.2, rely=0.3, relwidth=0.27, anchor="n")

        #binding the selection to creating item name dropdown list:
        self.food_type_dropdown.bind("<<ComboboxSelected>>", self.generate_item_dropdown)


        #ITEM SELECT:

        self.item_label = Label(self.frame_vars, text="Select item:" ,bg="#FCF0E4", font="roboto 11")
        self.item_label.place(relx=0.5, rely=0.05, relwidth=0.27, anchor="n")
        
        #name drop down is empty at the beginning. It is created when type is selected.
        self.food_names_dropdown = Combobox(self.frame_vars, value=[" "], state="readonly")
        self.food_names_dropdown.place(relx=0.5, rely=0.3, relwidth=0.27, anchor="n")


        #SERVINGS SELECT:

        self.serv_label = Label(self.frame_vars, text="Servings amount:" ,bg="#FCF0E4", font="roboto 11")
        self.serv_label.place(relx=0.8, rely=0.05, relwidth=0.27, anchor="n")

        self.servings_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        #servings drop down:
        self.servings_dropdown = Combobox(self.frame_vars, value=self.servings_list, state="readonly")
        self.servings_dropdown.place(relx=0.8, rely=0.3, relwidth=0.27, anchor="n")
        

        #PREVIEW BUTTON:
        self.preview_button = Button(self.frame_vars, text="PREVIEW SELECTED ITEM", command=self.show_the_item)
        self.preview_button.place(relx=0.5, rely=0.65, anchor="n")
        
        #printing results:
        self.frame_results = Frame(self.frame_middle, bg="#E9BFA7")
        self.frame_results.place(relx=0.5, rely=0.4, relheight=0.35, relwidth=0.9, anchor="n")

        #empty labels:
        #   to use as notification message or item preview:
        self.result = Label(self.frame_results, justify="left", bg="#E9BFA7", font="roboto 15")
        self.result.place(relx=0.5, rely=0.1, anchor="n")
        self.result3 = Label(self.frame_results, justify="left", bg="#E9BFA7", font="roboto 9")
        self.result3.place(relx=0.5, rely=0.6, anchor="n")
        self.result4 = Label(self.frame_results, justify="left", bg="#E9BFA7", font="roboto 9")
        self.result4.place(relx=0.5, rely=0.8, anchor="n")

        #SAVE button:
        self.save_button = Button(self.frame_middle, width=10, text="SAVE", command=self.fact_check)
        self.save_button.place(relx=0.4, rely=0.8, anchor="n")

        #DISCARD button:
        self.discard_button = Button(self.frame_middle, width=10, text="DISCARD", command=self.clear_all)
        self.discard_button.place(relx=0.6, rely=0.8, anchor="n")

        #message box:
        #   to communicate w the user if there is a problem:
        self.message_box = Frame(self.frame_middle, bg="#BE796D")
        self.message_box.place(relx=0.5, rely=0.9, relheight=0.08, relwidth=0.5, anchor="n")
        
        #Label to configure messages:
        self.message_label = Label(self.frame_middle, bg="#BE796D", text="Please select your entry date from the calendar.")
        self.message_label.place(relx=0.5, rely=0.91, anchor="n")

        #-----------------------------------------ADD MODE UPPER HALF-------------------------------------------

        #-----------------------------------------------ADD MODE DISPLAY HALF-------------------------------------------------------

        #bottom frame
        self.frame_bottom = Frame(master, bg="#BE796D")
        self.frame_bottom.place(relx=0.01, rely=0.58, relheight=0.41, relwidth=0.98)

        #Display user item inventory:
        self.title_inventory = Label(self.frame_bottom, bg="#BE796D", text= "YOUR ITEMS", font="roboto 15")
        self.title_inventory.place(relx=0.5, anchor="n")

        #TREEVIEW:
        #PLEASE MAKE SURE YOUR Tk VERSION IS HIGHER THAN 8.6.10!!

        # treeview style:
        self.style_tw = Style()
        self.style_tw.theme_use("default")
        self.style_tw.theme_use("default")
        self.style_tw.configure("Treeview", foreground="black", rowheight=25, fieldbackground="#FCF0E4", background=("#FCF0E4"))
        self.style_tw.map("Treeview", foreground=[("selected", "#576566")], background=[("selected", "#C2D7D0")])
        
        #treeview item display:
        self.user_inventory = Treeview(self.frame_bottom)
        self.user_inventory.place(rely=0.1, relx=0.5, relwidth=0.98, relheight=0.88, anchor="n")
        #getting the columns from user_items.csv file (self.df_user is the dataframe containing it)
        self.user_inventory["column"] = list(self.df_user.columns)
        self.user_inventory["show"] = "headings"
        #creating the columns:
        self.user_inventory.column("#0", width=0)
        self.user_inventory.column("title", width=97)
        self.user_inventory.column("type", width=97)
        self.user_inventory.column("amount", width=97)
        self.user_inventory.column("entry date", width=140)
        self.user_inventory.column("notify (days)", width=140)
        self.user_inventory.column("expiration (days)", width=140)
        #creating the headings:
        self.user_inventory.heading("#0", text="")
        self.user_inventory.heading("title", text="TITLE", anchor="w")
        self.user_inventory.heading("type", text="TYPE", anchor="w")
        self.user_inventory.heading("amount", text="SERVINGS", anchor="w")
        self.user_inventory.heading("entry date", text="ENTRY DATE", anchor="w")
        self.user_inventory.heading("notify (days)", text="NOTIFICATION DAY", anchor="w")
        self.user_inventory.heading("expiration (days)", text="EXPIRATION DAY", anchor="w")

        #inserting the values:
        self.df_user = self.df_user.sort_values(by=["entry date", "title"], ascending=False)
        self.df_user_rows = self.df_user.to_numpy().tolist()
        for row in self.df_user_rows:
            self.user_inventory.insert("", "end", values=row)

        #scrollbar:
        self.inv_scroll = Scrollbar(self.frame_bottom, orient=VERTICAL, command=self.user_inventory.yview)
        self.user_inventory.config(yscrollcommand=self.inv_scroll.set)
        self.inv_scroll.place(relx=0.99, rely=0.54, relheight=0.87, anchor="e")

        self.count = 0 #this is used when adding a new row by saving an entry.

        #-----------------------------------------------ADD MODE DISPLAY HALF-------------------------------------------------------

    #========================TOP RIBBON FUNCTIONS===========================

    def change_mode(self):
        """change_mode function closes one mode window and opens the other one.
        In add mode, it closes add mode and runs edit mode.
        Args:
            none
        Returns:
            the edit mode window.
        Raises:
            none
        """
        master.destroy()
        os.system("edit_mode_run.py")

    def calendar_get(self, e):
        """Since this program can work retrospectively, there is a date selection function. 
        The selected date is used as the entry date while saving items. 
        Args:
            e: selection from DateEntry widget.
        Returns:
            notification_trigger(self)
        Raises:
            none
        """
        self.entry_date = self.entry_cal.get_date()
        self.message_label.config(text=" ")
        self.title.config(text="SEARCH ITEM")
        self.notification_trigger() 

    #========================ADD MODE UPPER HALF FUNCTIONS===========================
    
    def show_the_item(self):
        """This function shows the item details of a selection. 
        Args:
            self: selection from Combobox widget.
        Returns:
            Detailed information about the selected item from popular_items_library.csv file.
        Raises:
            If there are missing information, the user gets message pointing out what is missing.
        """
        if self.food_type_dropdown.get() == "" and self.food_names_dropdown.get() == "":
            self.result.configure(text="Please select a type and an item to preview.")
            self.result3.configure(text="")
            self.result4.configure(text="")
        elif self.food_names_dropdown.get() == "":
            self.result.configure(text="Please select an item to preview.")
            self.result3.configure(text="")
            self.result4.configure(text="")
        else:
            self.item_info = self.df.query("title == @self.food_names_dropdown.get()").values[0]
            self.result.configure(text=self.food_names_dropdown.get().upper()+":")
            self.result3.configure(text=self.food_names_dropdown.get().capitalize()+" is a type of "+self.food_type_dropdown.get().lower()+". It will expire in "+str(self.item_info[3])+" days.")
            self.result4.configure(text="You will get a notification message "+str(self.item_info[2])+" days before expiration.")

    def generate_item_dropdown(self, e):
        """This function creates the item name dropdown menu with the selected type.
        Args:
            e: selection from Combobox widget for type selection.
        Returns:
            a configured Combobox values list with items under selected type.
        Raises:
            none
        """
        self.items_df = self.df.query("types == @self.food_type_dropdown.get()")
        self.food_names_list = list(self.items_df["title"])
        self.food_names_dropdown.config(value=self.food_names_list) 

    def fact_check(self):
        """Saving a new item is a 2 step process in this application.
        First the inputs are going through this if loop 
        Args:
            e: selection from DateEntry widget.
        Returns:
            notification_trigger(self)
        Raises:
            none
        """
        if self.food_type_dropdown.get() == (""):
            self.message_label.config(text="Please select type and item to save.")
        elif self.food_names_dropdown.get() == (""):
            self.message_label.config(text="Please select an item to save.")
        elif self.servings_dropdown.get() == (""):
            self.message_label.config(text="Please select how many servings you have before saving.")
        else:
            self.message_label.config(text="Saved!")
            self.save_item()

    def save_item(self):
        self.df_selected = self.df.query("title == @self.food_names_dropdown.get()")
        self.expire = self.entry_date + datetime.timedelta(days=int(self.df_selected["expiration (d)"]))
        self.notify = self.expire - datetime.timedelta(days=int(self.df_selected["notify (d)"]))
        self.new_row = {"title":self.food_names_dropdown.get(), "type":self.food_type_dropdown.get(), "amount":self.servings_dropdown.get(), "entry date":self.entry_date, "notify (days)": self.notify, "expiration (days)": self.expire}

        self.df_user = self.df_user.append(self.new_row, ignore_index=True)
        self.df_user.to_csv('user_items.csv', mode="w+", index=False)
        
        self.df_user = self.df_user.sort_values(by=["entry date", "title"], ascending=False)
        self.update_treeview()
        self.clear_all()

    def update_treeview(self):
        self.user_inventory.tag_configure("recent", background="#BA8E47")
        self.style_tw.map("recent", background="background")
        
        self.expire = self.entry_date + datetime.timedelta(days=int(self.df_selected["expiration (d)"]))
        self.notify = self.expire - datetime.timedelta(days=int(self.df_selected["notify (d)"]))
        self.today = self.entry_date.strftime("%Y-%m-%d")
        self.user_inventory.insert("", index=0, iid=self.count, text="" ,values=(self.food_names_dropdown.get(), self.food_type_dropdown.get(), self.servings_dropdown.get(), self.today, self.notify, self.expire), tags=("recent", ))
        self.count += 1

    def clear_all(self):
        self.food_type_dropdown.set("")
        self.food_names_dropdown.set("")
        self.servings_dropdown.set("")

    def notification_trigger(self):
        self.today = self.entry_date.strftime("%Y-%m-%d")
        #NOTIFY ITEMS
        self.df_notify = self.df_user.loc[self.df_user["notify (days)"] <= self.today] 
        self.name_notify = list(self.df_notify["title"])
        #EXPIRED THINGS
        self.df_exp_dead = self.df_user.loc[self.df_user["expiration (days)"] < self.today]
        self.names_expired = list(self.df_exp_dead["title"])

        self.list_notify_notexpired = [x for x in self.name_notify if x not in self.names_expired]

        self.result.config(text="EXPIRES SOON:")
        self.result3.config(text=", ".join(self.list_notify_notexpired))
        self.result4.config(text="EXPIRED ITEMS: "+", ".join(self.names_expired))


e = Fonefridge(master)

master.mainloop()