from tkinter import *
import hashlib
from tkinter import messagebox
from pathlib import Path

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
        k_phrase = self.key_phrase.get()
        if len(k_phrase) != 0:
            hash_key = hashlib.md5(k_phrase.encode())
            path = Path('hash_key.txt')
            with open(path, 'w') as hashfile:
                hashfile.write(hash_key.hexdigest())
        else:
            messagebox.showerror(title="Empty phrase", message="The key phrase cannot be empty.")

    def back_to_prev(self):
        self.root.destroy()
        screen = Tk()
        from admin import Admin
        a_screen = Admin(screen, self.row)
        screen.mainloop()
