#!/usr/bin/python3

# ******************************
# ******************************
# **                          **
# **    ENV variable init.    **
# **                          **
# ******************************
# ******************************
import os
from static.tool.console.ConsoleTemplate import ConsoleTemplate as tmp
from os import environ as ENV


def createFolder(path: str):
    try:
        '''Sprawdzanie istnienia ścieżki'''
        if not os.path.exists(path):
            os.makedirs(path)
            print("Directory Successfully Created")
        else:
            print("Directory Already Exists")

    except:
        print("Błąd createFolder")
        return False

    return True

def variableconfig():
    ENV['TRASHPANDA_HOST'] = "trashpanda.pwsz.nysa.pl"
    ENV['CLOUD_MAX_FILE_SIZE'] = '1MB'
    ENV['CLOUD_PROJECT_PATH'] = os.getcwd()
    ENV['CLOUD_TRASHBOX'] = '/srv/Data/'
    ENV['CLOUD_DUMP'] = "/srv/Data/DUMP/" if createFolder('/srv/Data/DUMP/') else "jebudu"
    ENV['TRASHPANDA_LOGIN'] = ENV.get('TRASHPANDA_LOGIN') if 'TRASHPANDA_LOGIN' in ENV else "sergiy1998"
    ENV['TRASHPANDA_PASSWD'] = ENV.get('TRASHPANDA_PASSWD') if 'TRASHPANDA_PASSWD' in ENV else "hspybxeR98>"
    print("[*]Configure Variables...")


variableconfig()
print(tmp.TrashPandpa())


