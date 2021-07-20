from os import name
import pandas as pd 
from tkinter.ttk import Combobox, Style, Treeview
import datetime
from tkinter import *
from tkcalendar import *
import sys
import os


#  style things:
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
    def __init__(self, master):
        self.df = pd.read_csv("popular_items_library.csv")
        self.df_user = pd.read_csv("user_items.csv")

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
        self.add_button = Button(self.frame_top, width=10, text="EDIT MODE", font="roboto 15", bg="#A9B6BE",command=self.change_mode)
        self.add_button.grid(column=0, row=0, ipadx=5)
        self.is_add = True

        # CALENDAR--------
        #self.calendar_button = Button(self.frame_top, width=10, text="SET DATE", font="roboto 15", bg="#A9B6BE", command=self.calendar_entry)
        #self.calendar_button.grid(column=2, row=0, ipadx=5))
        self.entry_cal = DateEntry(self.frame_top, background= "#A9B6BE", foreground= "#576566")
        self.entry_cal.grid(column=2, row=0, ipadx=5)
        self.entry_cal.bind("<<DateEntrySelected>>", self.calendar_get) # gets fired when a date was selected
        def calendar_get(self):
                self.entry_date = self.entry_cal.get_date()

        #---------------------------------------------TOP RIBBON-------------------------------------------------
        
        #-----------------------------------------ADD MODE UPPER HALF-------------------------------------------
        #middle frame
        self.frame_middle = Frame(master, bg="#E9BFA7")
        self.frame_middle.place(relx=0.01, rely=0.08, relheight=0.49, relwidth=0.98)

        #food name search title--------Search the name of your item:
        self.title = Label(self.frame_middle, bg="#E9BFA7", text= "-----PLEASE SELECT THE DATE FIRST-----", font="roboto 15")
        self.title.place(relx=0.5, anchor="n")
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
        self.frame_results = Frame(self.frame_middle, bg="#E9BFA7")
        self.frame_results.place(relx=0.5, rely=0.4, relheight=0.35, relwidth=0.9, anchor="n")

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

        #treeview style:


        self.style_tw = Style()
        self.style_tw.theme_use("default")
        self.style_tw.configure("Treeview", background="#FCF0E4" ,rowheight=25, fieldbackground="#FCF0E4")
        self.style_tw.map('Treeview', foreground=self.fixed_map('foreground'), background=self.fixed_map('background'))
        

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

        self.df_user = self.df_user.sort_values(by=["entry date", "title"], ascending=False)
        self.df_user_rows = self.df_user.to_numpy().tolist()
        for row in self.df_user_rows:
            self.user_inventory.insert("", "end", values=row)

        #scrollbar
        self.inv_scroll = Scrollbar(self.frame_bottom, orient=VERTICAL, command=self.user_inventory.yview)
        self.user_inventory.config(yscrollcommand=self.inv_scroll.set)
        self.inv_scroll.place(relx=0.99, rely=0.54, relheight=0.87, anchor="e")

        self.count = 0
        #-----------------------------------------------ADD MODE DISPLAY HALF-------------------------------------------------------

    #ttk version 8.6 apparently has a bug that makes background etc. doesn't work.
    #I found this def from https://core.tcl-lang.org/tk/tktview?name=509cafafae 
    def fixed_map(self, e):
        return [elm for elm in self.style_tw.map('Treeview', query_opt=self) if elm[:2] != ('!disabled', '!selected')]

    #========================TOP RIBBON FUNCTIONS===========================

    def change_mode(self):
        master.destroy()
        os.system("edit_mode.py")
        
    # calendar pop-up window def here
    # CH - not needed
    # def calendar_entry(self):  
    #     self.pop_up = Toplevel(master)

    #     self.date_label = Label(self.pop_up, text="Choose date", font="roboto 12")
    #     self.date_label.pack(padx=10, pady=10)

    #     self.entry_cal = DateEntry(self.pop_up, background= "#A9B6BE", foreground= "#576566")
    #     self.entry_cal.pack(padx=10, pady=10)

    #     self.ok_button = Button(self.pop_up, text="OK", bd=0, command=self.calendar_get)
    #     self.ok_button.pack(padx=10, pady=10)
    
    def calendar_get(self, e): # with bind, it needs a 2. arg for the event
        self.entry_date = self.entry_cal.get_date()
        print("date set to", self.entry_date)
        #self.message_label.config(text=" ")
        #self.title.config(text="SEARCH ITEM")
        #self.pop_up.destroy()
        #self.notification_trigger() 
    

    #========================ADD MODE UPPER HALF FUNCTIONS===========================
    
    def show_the_item(self):
        self.item_info = self.df.query("title == @self.food_names_dropdown.get()").values[0]
        self.result.configure(text=self.food_names_dropdown.get().upper()+":")
        self.result3.configure(text=self.food_names_dropdown.get().capitalize()+" is a type of "+self.food_type_dropdown.get().lower()+". It will expire in "+str(self.item_info[3])+" days.")
        self.result4.configure(text="You will get a notification message "+str(self.item_info[2])+" days before expiration.")

    def generate_item_dropdown(self, e):
        self.items_df = self.df.query("types == @self.food_type_dropdown.get()")
        self.food_names_list = list(self.items_df["title"])
        self.food_names_dropdown.config(value=self.food_names_list) 

    def fact_check(self):
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

    def update_treeview(self):    #==========HIGHLIGHT DOESN'T WORK YET!!!!!!!1
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