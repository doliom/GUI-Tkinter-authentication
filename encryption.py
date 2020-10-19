from cryptography.fernet import Fernet
from pathlib import Path
from sys_info import write_sys_info

def write_key(): # створюємо ключ і зберігаємо в файл
    key = Fernet.generate_key()

    with open('crypto.key', 'wb') as key_file:
        key_file.write(key)

def load_key(): # завантажуємо 'crypto.key'
    return open('crypto.key', 'rb').read()

def encrypt(filename, key): # шифруємо файл
    f = Fernet(key)
    print(f)
    with open(filename, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)

    with open(filename, 'wb') as file:
        file.write(encrypted_data)

def decrypt(filename, key):# дешифруємо файл
    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, 'wb') as file:
        file.write(decrypted_data)

def encryption_main():
    #роскоментувати наступний рядок, якщо запускаєте вперше
    write_key()
    key = load_key()
    write_sys_info()
    file = Path('sys_info.txt')
    encrypt(file, key) #шифруємо файл