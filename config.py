import os
import hashlib
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

CONFIG_PATH = os.path.join(ROOT_DIR, 'user_information.csv')

def get_hash_key():
    with open('hash_key.txt', 'a', encoding='utf-8') as f:
        pass
    path = Path('hash_key.txt')
    if os.stat(path).st_size == 0:
        hash_key = hashlib.md5(b'defaultstartstring')
        with open(path, 'w') as hashfile:
            hashfile.write(hash_key.hexdigest())

    with open(path, 'rb') as file:
        file_data = file.read()

    return file_data

HASH_KEY = get_hash_key()

HASH_KEY_PATH = os.path.join(ROOT_DIR, 'hash_key.txt')