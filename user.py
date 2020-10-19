from tkinter import *
from tkinter import messagebox
from pathlib import Path
import csv

class User:
    def __init__(self, root, row):
        self.root = root
        self.row = row
        self.root.title(row[0])
        self.root.geometry("1200x768+0+0")
        self.root.configure(bg="LightSeaGreen")
        Label(text="MENU", bg="DarkSeaGreen", fg="white", height="5", width="300").pack()
        Button(self.root, text="CHANGE PASSWORD", bd=3, bg="PapayaWhip", fg="black", width="50", command=self.change_password).pack()
        Label(self.root, text="", bg="LightSeaGreen").pack()
        Button(self.root, text="SIGN OUT", bd=3, bg="PapayaWhip", fg="black", width="50", command=self.sign_out).pack()

    def change_password(self):
        self.root.destroy()
        screen = Tk()
        from change_user_pass import ChangeUserPassword
        chp_screen = ChangeUserPassword(screen, self.row)
        screen.mainloop()

    def sign_out(self):
        self.root.destroy()
        screen = Tk()
        from authentication import Authentication
        a_screen = Authentication(screen)
        screen.mainloop()