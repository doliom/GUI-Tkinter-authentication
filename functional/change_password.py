from tkinter import *
from tkinter import messagebox
from pathlib import Path
import csv

class ChangePassword:
    def __init__(self, root, row):
        self.path = Path('user_information.csv')
        self.root = root
        self.row = row
        self.root.title("Update password")
        self.root.geometry("1200x768+0+0")
        self.root.configure(bg="DarkSeaGreen")
        self.old_password, self.new_password = StringVar(), StringVar()

        Label(self.root, text="Old password", bg="DarkSeaGreen", fg="black", height="5", width="50").pack()
        self.old_pass_enter = Entry(self.root, textvariable=self.old_password, show='*')
        self.old_pass_enter.pack()
        Label(self.root, text="New password", bg="DarkSeaGreen", fg="black", height="5", width="50").pack()
        self.new_pass_enter = Entry(self.root, textvariable=self.new_password, show='*')
        self.new_pass_enter.pack()
        Label(self.root, text="", bg="DarkSeaGreen").pack()
        Button(self.root, text="Update password", bd=3, bg="PapayaWhip", fg="black", command=self.update_pass).pack()
        Label(self.root, text="", bg="DarkSeaGreen").pack()
        Button(self.root, text="Cancel", bd=3, bg="PapayaWhip", fg="black", command=self.back_to_prev).pack()

    def back_to_prev(self):
        self.root.destroy()
        screen = Tk()
        from admin import Admin
        a_screen = Admin(screen, self.row)
        screen.mainloop()

    def update_pass(self):
        if self.row[1] == self.old_password.get():

            with open(self.path, "r+") as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    if "ADMIN" not in line:
                        f.write(line)
                f.truncate()

            user_information = ["ADMIN", self.new_password.get(), len(self.new_password.get()), 0, 0]

            with open(self.path, 'a') as csvfile:
                writer = csv.writer(csvfile, delimiter=",")
                writer.writerow(user_information)
                Label(self.root, text="Update Successfully", fg="green",bg="PapayaWhip").pack()
        else:
            messagebox.showerror(title="Wrong password", message="Old password isn't valid")

        self.old_pass_enter.delete(0, END)
        self.new_pass_enter.delete(0, END)