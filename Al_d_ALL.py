import os
from cryptography.fernet import Fernet

def decrypt_files(key):
    f = Fernet(key)
    for drive in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        drive_path = f'{drive}:\\'
        if os.path.exists(drive_path):
            for root, dirs, files in os.walk(drive_path):
                for file in files:
                    if file.endswith('.enc'):
                        file_path = os.path.join(root, file)
                        with open(file_path, 'rb') as f1:
                            data = f1.read()
                        decrypted_data = f.decrypt(data)
                        with open(file_path[:-4], 'wb') as f2:
                            f2.write(decrypted_data)
                        # print(file_path[:-4])  # print the name of the decrypted file
                        os.remove(file_path)

key = b'gQHAjOvQ8tUkqHqrfwXs8uVwdsgLmItRH4JZ2xz18l0='

decrypt_files(key)
