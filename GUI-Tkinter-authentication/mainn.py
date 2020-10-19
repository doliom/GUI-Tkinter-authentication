from tkinter import *
from encryption import encryption_main

def main():
    encryption_main()
    root = Tk()
    from authentication import Authentication
    my_gui = Authentication(root)
    root.mainloop()

if __name__ == '__main__':
    main()