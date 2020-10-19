from pathlib import Path
from arc4 import ARC4
import os
import hashlib
import csv

def arc4_encoder():
    path = Path('C:\\Users\\Darina\\ozi\\user_information.csv')
    arc4 = ARC4('57322b895038a0cbe6670a392dcd5501')
    buf = []
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            cipher = arc4.encrypt(str(row))
            print(cipher)
            print(arc4.decrypt(cipher))
    #         buf.append(cipher)
    # print(buf)
    # bufd = []
    # for i in buf:
    #     v = arc4.decrypt(i)
    #     bufd.append(v)
    # print(bufd)

arc4_encoder()


    # arc4 = ARC4('key')
    # cipher = arc4.encrypt('some plain text to encrypt')
#
# def arc4_decoder(key):
#     path = Path('hash_user_information.csv')
#     with open(path, newline='') as csvfile:
#         reader = csv.reader(csvfile, delimiter=',')
#         for row in reader:
#             if row[0] == username and row[1] == password:
#                 if username == 'ADMIN':
#                     successfully_access = 1
#                     self.call_admin(row)
#                 else:
#                     successfully_access = 1
#                     self.call_user(row)
#     arc4 = ARC4(key)
#     arc4.decrypt(cipher)

    # arc4 = ARC4('key')
    # arc4.decrypt(cipher)

def checking_hashfile():
    try:
        with open('hash_key.txt', 'a', encoding='utf-8') as f:
            pass
        path = Path('hash_key.txt')
        if os.stat(path).st_size == 0:
            hash_key = hashlib.md5(b'defaultstartstring')
            with open(path, 'w') as hashfile:
                hashfile.write(hash_key.hexdigest())

        # else:


    except FileNotFoundError:
        print("file not found")

