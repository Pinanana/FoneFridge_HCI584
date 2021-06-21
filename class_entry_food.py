import pandas as pd 
import datetime
from class_food import *

#df = pd.read_csv("popular_items_library.csv")
#name = input("search foods from popular items library:")
#name = "strawberry"

#item_info = df.query("title == @name")

#if len(item_info) > 0:
    #print("error, more than one result found.")
    #item_info.reset_index(drop=True, inplace=True)
    #print(res)
    #item_info = item_info.loc[0]


class Entry_Food(Food):
    def __init__(self, name, amount):
        
        self.df = pd.read_csv("popular_items_library.csv")
        self.item_info = self.df.query("title == @name")

        if len(self.item_info) > 0:
            #print("error, more than one result found.")
            self.item_info.reset_index(drop=True, inplace=True)
            #print(res)
            self.item_info = self.item_info.loc[0]

        self.name = name
        self.typef = self.item_info[1]
        self.notifyd = self.item_info[2]
        self.expired = self.item_info[3]
    
        self.amount = amount

        self.today = datetime.datetime.today().date()
        self.expirationd = self.today + datetime.timedelta(days=int(item_info["expiration (days)"]))
        self.notificationd = self.expirationd - datetime.timedelta(days=int(item_info["notify (days)"]))

    def display_food_entry(self):
        return "Item name: {}\nType: {}\nServings: {}\nEntry Date: {}\nExpiration Day: {}\nNotification Date: {}".format(self.name, self.typef, self.amount, self.today, self.expirationd, self.notificationd)

    def expiration_date(self):
        return "Your item will expire on {}".format(self.expirationd)

    def notification_date(self):
        return "You will get a notification on {}".format(self.notificationd)

    def notification_message(self):
        return "WARNING!\nThe {} will expire soon ({}).\nYou have {} servings left.".format(self.name, self.expirationd, self.amount)


#get this value from user
#amount = 5


#food_itemm = Entry_Food(name, amount)
#print(Entry_Food.display_food_entry(food_itemm))
#print(Entry_Food.expiration_date(food_itemm))
#print(Entry_Food.notification_date(food_itemm))
