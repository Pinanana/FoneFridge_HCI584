import pandas as pd 

df = pd.read_csv("popular_items_library.csv")
#name = input("search foods from popular items library:")
#name = "strawberry"

item_info = df.query("title == @name")

if len(item_info) > 0:
    #print("error, more than one result found.")
    item_info.reset_index(drop=True, inplace=True)
    #print(res)
    item_info = item_info.loc[0]


class Food(object):
    def __init__(self, name):
        
        self.name = name
        self.typef = item_info[1]
        self.notifyd = item_info[2]
        self.expired = item_info[3]
    
    def display_food(self):
        return "The {} is a type of {}.".format(self.name, self.typef)
    
    def display_expire(self):
        return "It will expire in {} days after the entry date.".format(self.expired)

    def display_notify(self):
        return "The notification will be sent {} days before the expiration date.".format(self.notifyd)

food_i = Food(name)
#print(Food.display_food(food_i))

