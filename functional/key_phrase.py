from tkinter import *
from tkinter import messagebox
from pathlib import Path
import csv

class KeyPhrase:
    def __init__(self, root, row):
        self.root = root
        self.row = row
        self.root.title("Enter key phrase")
        self.root.geometry("1200x768+0+0")
        self.root.configure(bg="LightYellow")
        self.key_phrase = StringVar()
        Label(text="Enter key phrase:", bg="LightYellow", fg="black", height="3", width="300").pack()
        self.input_kphrase = Entry(self.root, textvariable=self.key_phrase)
        self.input_kphrase.pack()
        Label(text="", bg="LightYellow").pack()
        Button(text="OK", bg="LightSlateGray", fg="white", command=self.ok).pack()
        Button(self.root, text="Cancel", bg="LightSlateGray", fg="white", command=self.back_to_prev).pack()
        self.root.mainloop()

    def ok(self):
        pass

    def back_to_prev(self):
        self.root.destroy()
        screen = Tk()
        from admin import Admin
        a_screen = Admin(screen, self.row1)
        screen.mainloop()