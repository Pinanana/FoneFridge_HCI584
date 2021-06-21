import pandas as pd 
import datetime
from tkinter import * 
from tkcalendar import *

from class_food import *
from class_entry_food import *



master = Tk()
master.title(FoneFrid)
canvas = Canvas(master, bg="#FCF0E4", height=750, width=750)
canvas.pack()

class Fonefridge(object):
    def __init__(self, master):
      
        app_frame = Frame(master)
        app_frame.pack()

        #visual part(no function):
        #AREAS:
        #top frame
        self.frame_top = Frame(master, bg="#A9B6BE")
        self.frame_top.place(relx=0.01, rely=0.01, relheight=0.1, relwidth=0.98)

        #bottom left frame 
        self.frame_bottom_left = Frame(master, bg="#E9BFA7")
        self.frame_bottom_left.place(relx=0.01, rely=0.12, relheight=0.87, relwidth=0.4)

        #bottom right frame
        self.frame_bottom_right = Frame(master, bg="#BE796D")
        self.frame_bottom_right.place(relx=0.42, rely=0.12, relheight=0.87, relwidth=0.57)

        #TITLES:
        #main title-FONEFRIDGE
        self.title = Label(self.frame_top, bg="#A9B6BE", text= "FONEFRIDGE", font="roboto 22")
        self.title.pack(pady=14)

        #food name search title-Search the name of your item:
        self.title = Label(self.frame_bottom_left, bg="#E9BFA7", text= "Search the name of your item:", font="roboto 15")
        self.title.pack(pady=5)




        #text entry slot
        self.entry_name = Entry(master, textvariable=self.name, width=50)
        self.entry_name.pack(padx=10, pady=5)

        self.name = StringVar()    #IntVar() & DoubleVar()      self.entry_name.get(command=Store_name)

        self.search_button = Button(self.frame_bottom_left, text="Search", command=self.display_item)
        self.search_button.pack(padx=10, pady=5)

        self.result = Label(self.frame_bottom_right, text="Here is the result for"+self.name.get()+":\n\n"+Food.display_food(Food(name))+"\n"+Food.display_expire(Food(name)))+"\n"+Food.display_notify(Food(name)), bd=1, relief="sunken", justify="left", bg="#BE796D", font="roboto 11")
        self.result.pack(padx=10, pady=5, ipadx=5, ipady=5)

   

    #def Store_name(self):
        #name = return self.name

print(name)

e = Fonefridge(master)

master.mainloop()