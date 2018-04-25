import getpass
from os import environ as ENV
from static.tool.console.ConsoleTemplate import ConsoleTemplate as templates

print(templates.TrashPandpa())

if(ENV["TRASHPANDA_USER"] == ""):
    print("Please login to (DB)system")
    login = input("Login:")
    print("Password")
    passwd = getpass.getpass()


login()


