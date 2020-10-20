from tkinter import *
from encryption import encryption_main
from functional.symmetric_encryption import checking_hashfile, arc4_encoder, arc4_decoder
from config import HASH_KEY

def main():
    encryption_main()
    if checking_hashfile():
        arc4_decoder(HASH_KEY)

    root = Tk()
    from authentication import Authentication
    my_gui = Authentication(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    arc4_encoder(HASH_KEY)
