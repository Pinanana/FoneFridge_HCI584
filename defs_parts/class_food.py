import pandas as pd 


class Food:
    def __init__(self, name, typef, amount, entryd, notifyd, expired):
        self.name = name
        self.typef = typef
        self.amount = amount
        self.entryd = entryd
        self.notifyd = notifyd
        self.expired = expired

    def df_read(self):
        
    
    def display_food(self):
        return "The item {} is a {}. It will expire in {} days after the entry date. The notification will be sent {} days before the expiration date." format(self.name, self.typef, self.expired, self.notifyd)


#getting the food item as an instance
df = pd.read_csv("popular_items_library.csv")
#food_item = input("search foods from popular items library:")
food_item = "beef"

res = df.query("title == @food_item")

if len(res) > 1:
    print("error, more than one result found.")
    res.reset_index(drop=True, inplace=True)
    print(res)
    res = res.loc[0]

print(res)
