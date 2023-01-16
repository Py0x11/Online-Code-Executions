# Online Code Execution Model in Python via Pastebin by @Py0x11
import requests
from os import system
# Defining Users and Passwords is done in pastebin
# Check this Paste https://pastebin.com/4HZPS5d7 for Reference

# Syntax of Pastebin must be user = [username/email]; password = [pass]

Data = 'https://pastebin.com/raw/4HZPS5d7'  # Pastebin URL

precode = requests.get(Data)  # Getting Username:Password as Str

# Converting Fetched Data to Text Format as Exec() only accepts string values as Source
code = precode.text

exec(code)  # Executing the Code to Make User as Password Variable
print(user)
print(password)

# Fetching and Processing of Other Code from Internet


def main():
    print("Login Test With Online Credentials")

    dat1 = input("Enter Your Username : ")  # Taking User Input for Username

    dat2 = input("Enter Your Password : ")  # Taking User Input for Password

    if dat1 == user and dat2 == password:  # Checking Username and Password i know its not secure ill make a Hash matching Version Soon !

        system("cls")  # Just Clearing the Dirty Screen

        print("Login Succesfull")

        print("Welcome to Your Code !")

    else:
        print("Login Unsucessfull ! Try Again ")

        system("cls")  # Just Clearing the Dirty Screen

        main()  # Restarting the Login


main()  # Calling the Login Function
