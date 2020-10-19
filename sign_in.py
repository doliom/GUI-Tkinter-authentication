from tkinter import *
from tkinter import messagebox
from pathlib import Path
import csv

#10. Наявність рядкових і прописних букв, а також знаків арифметичних операцій

class Sign_in:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign in")
        self.root.geometry("1200x768+0+0")
        self.root.configure(bg="LightYellow")
        self.username, self.password = StringVar(), StringVar()
        Label(self.root, text="Login Screen", bg="beige", fg="black", height="3", width="300").pack()
        Label(text="", bg="LightYellow").pack()
        Label(self.root, text="Username:", bg="LightYellow", fg="black", height="3", width="300").pack()
        self.input_username = Entry(self.root, textvariable=self.username)
        self.input_username.pack()
        Label(self.root, text="Password:", bg="LightYellow", fg="black", height="3", width="300").pack()
        self.input_password = Entry(self.root, textvariable=self.password, show='*')
        self.input_password.pack()
        Label(text="", bg="LightYellow").pack()
        Button(self.root, text="Login", bg="LightSlateGray", fg="white", command=self.login).pack()
        Label(text="", bg="LightYellow").pack()
        Button(self.root, text="Cancel", bg="Bisque", fg="black", command=self.back_to_auth_screen).pack()
        self.root.mainloop()

    def login(self):
        successfully_access = 0
        username = self.username.get()
        password = self.password.get()
        self.input_username.delete(0, END)
        self.input_password.delete(0, END)
        path = Path('user_information.csv')
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if row[0] == username and row[1] == password:
                    if username == 'ADMIN':
                        successfully_access = 1
                        self.call_admin(row)
                    else:
                        successfully_access = 1
                        self.call_user(row)
        if successfully_access == 0:
            messagebox.showwarning(title="Invalid username or password", message="This user wasn't found.")

    def call_admin(self, row):
        self.root.destroy()
        screen = Tk()
        from admin import Admin
        admin_screen = Admin(screen, row)
        screen.mainloop()

    def call_user(self, row):
        if row[3] != str(0):
            messagebox.showerror(title="WARNING", message="Your account was blocked")
        else:
            self.root.destroy()
            screen = Tk()
            from user import User
            user_screen = User(screen, row)
            screen.mainloop()

    def back_to_auth_screen(self):
        self.root.destroy()
        screen = Tk()
        from authentication import Authentication
        sign_up = Authentication(screen)
        screen.mainloop()