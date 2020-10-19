from tkinter import *
from encryption import encryption_main
from functional.symmetric_encryption import checking_hashfile

def main():
    encryption_main()
    checking_hashfile()


    root = Tk()
    from authentication import Authentication
    my_gui = Authentication(root)
    root.mainloop()

if __name__ == '__main__':
    main()