# This file will have the main code.

import pandas as pd 

db = pd.read_csv("popular_items_library.csv")
display(db.head(5))

pip list