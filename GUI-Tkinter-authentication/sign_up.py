from tkinter import *
from pathlib import Path
from tkinter import messagebox
import csv

class Sign_up:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign up")
        self.root.geometry("1200x768+0+0")
        self.root.configure(bg="LightYellow")
        self.username, self.password = StringVar(), StringVar()
        Label(text="Create your account", bg="beige", fg="black", height="3", width="300").pack()
        Label(text="", bg="LightYellow").pack()
        Label(text="Username:", bg="LightYellow", fg="black", height="3", width="300").pack()
        self.input_username = Entry(self.root, textvariable=self.username)
        self.input_username.pack()
        Label(text="Password:", bg="LightYellow", fg="black", height="2", width="300").pack()
        self.input_password = Entry(self.root, textvariable=self.password, show='*')
        self.input_password.pack()
        Label(text="", bg="LightYellow").pack()
        Button(text="Register", bg="LightSlateGray", fg="white", command=self.register).pack()
        Label(text="", bg="LightYellow").pack()
        Button(text="Cancel", bg="Bisque", fg="black", command=self.back_to_auth_screen).pack()
        self.root.mainloop()

    def back_to_auth_screen(self):
        self.root.destroy()
        screen = Tk()
        from authentication import Authentication
        sign_up = Authentication(screen)
        screen.mainloop()

    def register(self):
        user_information = [self.username.get(), self.password.get(), len(self.password.get()), 0, 0]
        path = Path('user_information.csv')

        if self.retest(path):
            with open(path, 'a') as csvfile:
                writer = csv.writer(csvfile, delimiter=",")
                writer.writerow(user_information)
                Label(self.root, text="Register Successfully", fg="green").pack()

        self.input_username.delete(0, END)
        self.input_password.delete(0, END)

    def retest(self, path):
        check = True
        username = self.username.get()
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if row[0] == username:
                    messagebox.showwarning(title="Wrong username", message="A user with this login already exists. Try another username.")
                    check = False
                    break
        return check