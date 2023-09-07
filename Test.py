import os
import shutil

def main():
    #your code here
    print("your code here")

file = os.path.realpath("AI.exe")

StartUp = os.getenv('APPDATA') + r"\Microsoft\Windows\Start Menu\Programs\Startup"

#print(StartUp)

if os.path.exists("AI.exe"):
    if not os.path.exists(StartUp+r"\AI.exe"):

        shutil.move(file,StartUp)

    main()
