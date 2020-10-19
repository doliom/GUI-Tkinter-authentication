from tkinter import *
from tkinter import messagebox
from pathlib import Path
import csv

class NewUser:
    def __init__(self, root, row):
        self.root = root
        self.row = row
        self.root.title("Add new user")
        self.root.geometry("1200x768+0+0")
        self.root.configure(bg="LightYellow")
        self.username = StringVar()
        Label(text="Create your account", bg="beige", fg="black", height="3", width="300").pack()
        Label(text="", bg="LightYellow").pack()
        Label(text="Username:", bg="LightYellow", fg="black", height="3", width="300").pack()
        self.input_username = Entry(self.root, textvariable=self.username)
        self.input_username.pack()
        Label(text="", bg="LightYellow").pack()
        Button(text="ADD USER", bg="LightSlateGray", fg="white", command=self.register).pack()
        Label(text="", bg="LightYellow").pack()
        Button(text="Cancel", bg="Bisque", fg="black", command=self.back_to_prev).pack()
        self.root.mainloop()

    def back_to_prev(self):
        self.root.destroy()
        screen = Tk()
        from admin import Admin
        a_screen = Admin(screen, self.row)
        screen.mainloop()

    def register(self):
        password = ''
        user_information = [self.username.get(), password, len(password), 0, 0]
        path = Path('user_information.csv')

        if self.retest(path):
            with open(path, 'a') as csvfile:
                writer = csv.writer(csvfile, delimiter=",")
                writer.writerow(user_information)
                Label(self.root, text="Register Successfully", fg="green").pack()

        self.input_username.delete(0, END)

    def retest(self, path):
        check = True
        username = self.username.get()
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if row[0] == username:
                    messagebox.showwarning(title="Wrong username",
                                           message="A user with this login already exists. Try another username.")
                    check = False
                    break
        return check