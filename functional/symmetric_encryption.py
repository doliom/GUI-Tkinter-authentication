from pathlib import Path
from arc4 import ARC4
import os
import hashlib
import csv
from config import CONFIG_PATH
import numpy as np

def arc4_encoder(key):
    path = Path(CONFIG_PATH)
    buffer = []
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            arc4 = ARC4(key)
            cipher = arc4.encrypt(str(row))
            buffer.append(cipher)
            print("шифруем ", cipher)
            print(type(cipher))
    with open('hash_user_information.csv', "wb") as f:
        for i in range(len(buffer)):
            f.write(buffer[i])

# arc4_encoder('aaac0be5998842c12c55ba06d45804e2')


def arc4_decoder(key):
    path = Path('hash_user_information.csv')
    buffer = []
    with open(path, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = csvfile.read()
        arc4 = ARC4(key)
        cipher = arc4.decrypt(data)
        buffer.append(str(cipher))
        print("расшифруем ", cipher)

    np.savetxt("user_information1.csv",
               buffer,
               delimiter=", ",
               fmt='% s')



def checking_hashfile():
    try:
        with open('hash_user_information.csv', 'a', encoding='utf-8') as f:
            pass
        path = Path('hash_user_information.csv')
        if os.stat(path).st_size == 0:
            return False
        else:
            return True
    except FileNotFoundError:
        print("file not found")

