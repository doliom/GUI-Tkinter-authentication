from tkinter import *
from tkinter import messagebox
from pathlib import Path
import csv

class UsersList:
    def __init__(self, root, row):
        self.path = Path('user_information.csv')
        self.root = root
        self.row = row
        self.root.title("Users list")
        self.root.geometry("1200x768+0+0")
        self.root.configure(bg="DarkSeaGreen")


        Label(self.root, text=self.show_users, bg="DarkSeaGreen", fg="black", height="25", width="50").pack()

        Label(self.root, text="", bg="DarkSeaGreen").pack()
        Button(self.root, text="Cancel", bd=3, bg="PapayaWhip", fg="black", command=self.back_to_prev).pack()

    def back_to_prev(self):
        self.root.destroy()
        screen = Tk()
        from admin import Admin
        a_screen = Admin(screen, self.row)
        screen.mainloop()

    @property
    def show_users(self):
        with open(self.path, newline='') as csvfile:
            reader = csvfile.readlines()
        reader = self.listToString(reader)
        return reader

    def listToString(self, arr):
        str1 = ""
        for ele in arr:
            str1 += ele
        return str1