import os
from cryptography.fernet import Fernet

def decrypt_files(path, key):
    f = Fernet(key)
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.enc'):
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f1:
                    data = f1.read()
                decrypted_data = f.decrypt(data)
                with open(file_path[:-4], 'wb') as f2:
                    f2.write(decrypted_data)
                os.remove(file_path)

path = r'C:\share C\vscode\Pass\test'
key = b'gQHAjOvQ8tUkqHqrfwXs8uVwdsgLmItRH4JZ2xz18l0='

decrypt_files(path, key)
