from tkinter import *
from tkinter import messagebox
from pathlib import Path
import csv

class Restrictions:
    def __init__(self, root, row1):
        self.root = root
        self.row1 = row1
        self.root.title("Password Restrictions")
        self.root.geometry("1200x768+0+0")
        self.root.configure(bg="LightYellow")
        self.is_blocked = BooleanVar()
        self.is_blocked.set(0)
        self.username = StringVar()
        Label(text="", bg="LightYellow").pack()
        Label(text="Username:", bg="LightYellow", fg="black", height="3", width="300").pack()
        self.input_username = Entry(self.root, textvariable=self.username)
        self.input_username.pack()
        Label(text="", bg="LightYellow").pack()
        unblock = Radiobutton(text="off", bg="LightYellow", fg="black", variable=self.is_blocked, value=0)
        block = Radiobutton(text="on", bg="LightYellow", fg="black", variable=self.is_blocked, value=1)
        button = Button(text="Change", bg="LightSlateGray", fg="white", command=self.blocking)
        unblock.pack()
        block.pack()
        button.pack()
        Button(self.root, text="Cancel", bg="LightSlateGray", fg="white", command=self.back_to_prev).pack()
        root.mainloop()

    def blocking(self):
        path = Path('user_information.csv')
        username = self.username.get()
        user_information = []

        with open(path, "r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for row in new_f:
                if username not in row:
                    f.write(row)
                else:
                    user_information = list(row.split(","))
                    user_information[4] = self.is_blocked.get()
            f.truncate()

        with open(path, 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerow(user_information)
            Label(self.root, text="Successfully", fg="green").pack()

    def back_to_prev(self):
        self.root.destroy()
        screen = Tk()
        from admin import Admin
        a_screen = Admin(screen, self.row1)
        screen.mainloop()