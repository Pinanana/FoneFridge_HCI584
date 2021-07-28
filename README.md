# FoneFridge
Food items tracking project for HCI 584 summer 2021
## GENERAL DESCRIPTION

Food waste has been a huge issue for climate change, and there are some things we can do about it individually. Many people (as far as my questionnaire in the fall 2020 semester showed) struggle to keep track of their food stock when they are busy and they have little time to cook for themselves. As a result, many people throw away food items that they bought with the hope to cook them throughout the week but end up rotting in the deep corners of their fridges. For this problem, this product notifies people before the expiration date of the food items so that they can plan their meals accordingly. 

This desktop app helps people keep track of the food items in their fridge. It gives them notification message when the food item is about to expire and which ones are already expired. The user can search items from the app’s library of popular items. The items are classified based on their type (dairy, vegetable, meat, herbs, etc.). The popular items data is the popular_items_library.csv file that has generic food items such as tomatoes, eggs, and beef. This data also include a lifespan for each item in days and a generic notification time (like two days before expiration for some items).

## USER TASKS:

1. The user puts the new food items in the fridge.
2. Then enters the items in FoneFridge desktop application, by running add_mode_run.py file. (edit_mode_run.py file is the edit mode screen.)
4. In the add mode, user first selects the date from the calendar widget so that they are presented with the notification that shows expired and about to expire items before entering anything.
5. User searches for the item type.
6. After selecting a type, the item name dropdown will show the items from that type and user can select an item name.
7. They will then enter the serving count of their item from the servings dropdown menu (this could be an entry box but having all of the selection slots the same makes the interface more coherent).
8. Once they enter the amount, they will save the item to their database (user_items.csv) by clicking on the “SAVE” button. If they are not happy with the item they can change the dropdown selections or click the “DISCARD” button to empty all of the selections.
9. They will get status messages right under save and discard buttons so if there is a problem with saving their item, they can fix the problem. (for example, if they didn’t select servings amount they get "Please select how many servings you have before saving.")
10. They can see their items at the bottom of the window in add mode.
11. If they want to delete or change the servings amount, the user goes to the edit mode and double clicks on the item.
12. Once double clicked, a pop up window appears and the user either clicks delete to drop that item from their database or they select servings amount to change their record. 
13. They will get pop ups to prevent user error.

## REQUIREMENTS

Please get the required modules to run this app. 
pip install -r requirements.txt