#This function will be another mode, that is hidden, where 
# the frame under the title shows just the notification message and 
# when the user clicks “ok” they will be taken to edit mode. 
# If the item doesn’t get deleted, the notification appears the next day and the next day until it expires. (a while loop)


class Notification(Frame):
    def __init__(self, master):
        