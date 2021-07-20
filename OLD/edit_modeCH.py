from tkinter.ttk import Style, Treeview
from os import name
from numpy import result_type
import pandas as pd 
import datetime
from tkinter import * 
from tkcalendar import *
import tksheet

from class_food import Food
from class_entry_food import Entry_Food

import tkinter.simpledialog

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
        self.style_tw.configure("Treeview", foreground="black", rowheight=25, fieldbackground="#FCF0E4", bg="#FCF0E4")
        self.style_tw.map("Treeview")

        #treeview item display:
        self.user_inventory = Treeview(self.frame_edit)
        self.user_inventory.place(rely=0.1, relx=0.5, relwidth=0.98, relheight=0.88, anchor="n")

        self.user_inventory["column"] = list(self.df_user.columns)
        self.user_inventory["show"] = "headings"

        self.user_inventory.column("#0", width=5)
        self.user_inventory.column("title", width=95)
        self.user_inventory.column("type", width=95)
        self.user_inventory.column("amount", width=95)
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
        
        self.df_user = self.df_user.sort_values(by=["entry date", "title"], ascending=[True,True])
        # CH MUST reset index after sorting or loc[] won't work!
        self.df_user = self.df_user.reset_index(drop=True) 
        self.df_user_rows = self.df_user.to_numpy().tolist()
        for row in self.df_user_rows:
            self.user_inventory.insert("", "end", values=row)

        #scrollbar
        self.inv_scroll = Scrollbar(self.frame_edit, orient=VERTICAL, command=self.user_inventory.yview)
        self.user_inventory.config(yscrollcommand=self.inv_scroll.set)
        self.inv_scroll.place(relx=0.99, rely=0.54, relheight=0.87, anchor="e")

        #----------------------------------edit & delete pop up---------------------------------------------
        #serving change and delete pop up???
        self.user_inventory.bind("<Double-1>", self.edit_pop_up)

        # CH These should be positioned better ....
        self.delete_but = Button (self.frame_edit, text="DELETE SELECTED ITEM", command=self.delete_button)
        self.delete_but.grid(column=1, row=0)
        self.serv_but = Button(self.frame_edit, text="CHANGE AMOUNT ON SELECTED ITEM", command=self.change_amount_button)
        self.serv_but.grid(column=2, row=0)
        self.serv_but = Button(self.frame_edit, text="- 1 AMOUNT ON SELECTED ITEM", command=self.remove_one)
        self.serv_but.grid(column=3, row=0)

        # programmatically select/focus the first row, assuming iid is 'I001'
        self.user_inventory.selection_set('I001') 
        self.user_inventory.focus('I001')

        self.user_inventory.selectmode="none" # no multi select (doesn't work???)
        


    def edit_pop_up(self, e):
        self.pop_up_edit = Toplevel(master)
        self.pop_up_edit.geometry("400x50")

        self.delete_but = Button (self.pop_up_edit, text="DELETE", command=self.delete_button)
        self.delete_but.place(relx=0.01, rely=0.5, relwidth=0.4, anchor="w")

        self.servings_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.serv_drop = OptionMenu(self.pop_up_edit, *self.servings_list)
        self.serv_drop.place(relx=0.5, rely=0.5, relwidth=0.1, anchor=CENTER)

        self.serv_but = Button(self.pop_up_edit, text="CHANGE AMOUNT", command=self.change_amount_button)
        self.serv_but.place(relx=0.99, rely=0.5, relwidth=0.4, anchor="e")

        self.selected_item = self.user_inventory.selection()
        self.select_values_list = list(self.user_inventory.item([i for i in self.selected_item], "values"))
        print(self.select_values_list)

        self.index_list_df = self.df_user.index
        self.condition_title = self.df_user["title"] == self.select_values_list(0) and self.df_user["entry date"] == self.select_values_list(3)
        self.selected_name_indexes = self.index_list_df[self.condition_title]

        print(self.selected_name_indexes)

        #self.selected_index = 

        #self.df_user_selected_name = self.df_user.query("title == @self.select_values_list(0)")
        #self.df_selected_item_for_sure = self.df_user_selected_name.query("entry date == @self.select_values_list(3)")

        print(self.index_list_df)


    def delete_button(self):

        ui = self.user_inventory  # 
        selectedItem = ui.selection() # tuple with iid(s) of currently selected 

        for si in selectedItem: # empty is nothin was selected
            row = int(si[1:], 16)-1 # get df row index from iid string (16 b/c of hex)
            self.df_user.drop(row, inplace=True) # perma-delete row in df
            ui.delete(si)

        print(self.df_user)

    def change_amount_button(self):

        ui = self.user_inventory  # 
        selectedItem = ui.selection() # iid(s) of currently selected
        
        if len(selectedItem) > 0: # 0: nothing selected, otherwise take first selected row
            selectedItem = selectedItem[0]

            values = ui.item(selectedItem)["values"]
            food_name = values[0]
            df = self.df_user

            # get an int 
            new_serv = tkinter.simpledialog.askinteger(food_name, # title
                                            "New Amount?", 
                                            parent = self.frame_edit)

            if new_serv != None: # user didn't click Cancel in dialog
                row = int(selectedItem[1:], 16)-1 # get df row index from iid string
                df.loc[row, "amount"] =  new_serv 
                ui.delete(selectedItem)
                values[2] = str(new_serv)
                ui.insert("", row, values=values) # insert() needs an int for row id 
                print(df)
        
        '''
        self.pop_up_amount = Toplevel(master)
        self.pop_up_amount.geometry("500x50")

        self.del_label = Label(self.pop_up_amount, text="Are you sure you want to change servings amount?", font="roboto 12")
        self.del_label.place(relx=0.5, rely=0.01, anchor="n")

        self.del_button = Button(self.pop_up_amount, text="CHANGE", command=self.change_amount_incsv)
        self.del_button.place(relx=0.4, rely=0.5, anchor="n")

        self.keep_button = Button(self.pop_up_amount, text="KEEP", command=self.close_2)
        self.keep_button.place(relx=0.6, rely=0.5, anchor="n")
        '''
    # just remove one from the servings of selected row
    def remove_one(self):

        ui = self.user_inventory  # 
        selectedItem = ui.selection() # iid(s) of currently selected

        if len(selectedItem) > 0: # 0: nothing selected, otherwise take first selected row
            selectedItem = selectedItem[0]

            values = ui.item(selectedItem)["values"]
            current_servings = values[2]

            if current_servings > 0: # no negative servings!
                new_servings = current_servings - 1

                df = self.df_user

                row = int(selectedItem[1:], 16)-1 # get df row index from iid string
                df.loc[row, "amount"] =  new_servings 
                ui.delete(selectedItem)
                values[2] = str(new_servings)
                ui.insert("", row, values=values) # insert() needs an int for row id 
                print(df)


    # THIS DOESN'T WORK!!!! COME BACK TO THIS SOME TIME
    def delete_item(self):
        self.df_user.drop(self.selected_item, inplace=True)
        self.update_treeview()

    def change_amount_incsv(self):
        
        #.loc[row_index, "amount"] #gets the cell to change
        #self.update_treeview()
        pass



    def close_1(self):
        self.pop_up_del.destroy()

    def close_2(self):
        self.pop_up_amount.destroy()

    def update_treeview(self):
        for i in self.user_inventory.get_children():
            self.user_inventory.delete(i)
        self.df_user_rows = self.df_user.to_numpy().tolist()
        for row in self.df_user_rows:
            self.user_inventory.insert("", "end", values=row)



    #def Store_name(self):
        #name = return self.name

#print(name)

e = Edit(master)

master.mainloop()