import os
import shutil

def main():
    #your code here
    print("your code here")

file_name = "AI.py"
file_content = """
a = 10
print(a)
""" # محتوای دلخواه شما

with open(file_name, "w") as f:
    f.write(file_content.strip())


file = os.path.realpath("AI.exe")

#StartUp = r"C:\Users\Arka\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

StartUp = os.getenv('APPDATA') + r"\Microsoft\Windows\Start Menu\Programs\Startup"

#print(StartUp)

if os.path.exists("AI.exe"):
    if not os.path.exists(StartUp+r"\AI.exe"):

        shutil.move(file,StartUp)

    main()
