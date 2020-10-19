from tkinter import *
from tkinter import messagebox
from pathlib import Path
import csv

class Admin:
    def __init__(self, root, row):
        self.path = Path('user_information.csv')
        self.root = root
        self.row = row
        self.root.title("ADMIN")
        self.root.geometry("1200x768+0+0")
        self.root.configure(bg="DarkSeaGreen")
        self.old_password, self.new_password = StringVar(), StringVar()
        Label(text="MENU", bg="DarkSeaGreen", fg="white", height="5", width="300").pack()
        Button(self.root, text="CHANGE PASSWORD", bd=3, bg="PapayaWhip", fg="black", width="50", command=self.change_password).pack()
        Label(self.root, text="", bg="DarkSeaGreen").pack()
        Button(self.root, text="USERS LIST", bd=3, bg="PapayaWhip", fg="black", width="50", command=self.users_list).pack()
        Label(self.root, text="", bg="DarkSeaGreen").pack()
        Button(self.root, text="ADD NEW USER", bd=3, bg="PapayaWhip", fg="black", width="50", command=self.add_new_user).pack()
        Label(self.root, text="", bg="DarkSeaGreen").pack()
        Button(self.root, text="USER LOCKOUT", bd=3, bg="PapayaWhip", fg="black", width="50", command=self.user_lockout).pack()
        Label(self.root, text="", bg="DarkSeaGreen").pack()
        Button(self.root, text="PASSWORD RESTRICTIONS", bd=3, bg="PapayaWhip", fg="black", width="50", command=self.password_rest).pack()
        Label(self.root, text="", bg="DarkSeaGreen").pack()
        Button(self.root, text="SIGN OUT", bd=3, bg="PapayaWhip", fg="black", width="50", command=self.sign_out).pack()
        Label(self.root, text="", bg="DarkSeaGreen").pack()

    def change_password(self):
        self.root.destroy()
        screen = Tk()
        from functional.change_password import ChangePassword
        chp_screen = ChangePassword(screen, self.row)
        screen.mainloop()

    def users_list(self):
        self.root.destroy()
        screen = Tk()
        from functional.users_list import UsersList
        chp_screen = UsersList(screen, self.row)
        screen.mainloop()

    def add_new_user(self):
        self.root.destroy()
        screen = Tk()
        from functional.add_new_user import NewUser
        chp_screen = NewUser(screen, self.row)
        screen.mainloop()

    def user_lockout(self):
        self.root.destroy()
        screen = Tk()
        from functional.user_lockout import Lockout
        lock_screen = Lockout(screen, self.row)
        screen.mainloop()

    def password_rest(self):
        self.root.destroy()
        screen = Tk()
        from functional.restrictions import Restrictions
        lock_screen = Restrictions(screen, self.row)
        screen.mainloop()

    def sign_out(self):
        self.root.destroy()
        screen = Tk()
        from authentication import Authentication
        a_screen = Authentication(screen)
        screen.mainloop()

    def enter_pass_phrase(self):
        self.root.destroy()
        screen = Tk()
        from functional.key_phrase import KeyPhrase
        pass_screen = KeyPhrase(screen)
        screen.mainloop()