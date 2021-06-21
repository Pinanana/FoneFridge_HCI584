import pandas as pd 

#df = pd.read_csv("popular_items_library.csv")
#name = input("search foods from popular items library:")
#name = "strawberry"

#item_info = df.query("title == @name")

#if len(item_info) > 0:
    #print("error, more than one result found.")
    #item_info.reset_index(drop=True, inplace=True)
    #print(res)
    #item_info = item_info.loc[0]


class Food(object):
    def __init__(self, name):
        
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
    
    def display_food(self):
        return "The {} is a type of {}.".format(self.name, self.typef)
    
    def display_expire(self):
        return "It will expire in {} days after the entry date.".format(self.expired)

    def display_notify(self):
        return "Notification is set to {} days before expiration.".format(self.notifyd)


#print(Food.display_food(Food(name)))

