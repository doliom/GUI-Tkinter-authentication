# import tkinter
from tkinter import *

class Authentication:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x768+0+0")
        self.root.title("Authentication")
        self.root.configure(bg="LightYellow")
        Label(self.root, text="Select one", bg="beige", fg="black", height="2", width="300").pack()
        Label(self.root, text="", bg="LightYellow").pack()
        Button(self.root, text="Sign in", height="2", width="29", bg="beige", fg="black", command=self.call_sign_in).pack()
        Label(self.root, text="", bg="LightYellow").pack()
        Button(self.root, text="Sign up", height="2", width="30", bg="beige", fg="black", command=self.call_sign_up).pack()

    def call_sign_up(self):
        self.root.destroy()
        screen = Tk()
        from sign_up import Sign_up
        sign_up = Sign_up(screen)
        screen.mainloop()

    def call_sign_in(self):
        self.root.destroy()
        screen = Tk()
        from sign_in import Sign_in
        sign_in = Sign_in(screen)
        screen.mainloop()



