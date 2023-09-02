import os
import shutil

def main():
    #your code here
    print("your code here")

file = os.path.realpath("AI.exe")

StartUp = r"C:\Users\Arka\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

if os.path.exists("AI.exe"):
    if not os.path.exists(StartUp+r"\AI.exe"):

        shutil.move(file,StartUp)

    main()