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
#from static.tool.Logs import Log, LogType
from os import environ as ENV
from static.tool.FileManager import FileManager
# TODO: hackerman-style init script: dużo hakowania....
# rows, columns = os.popen('stty size', 'r').read().split()
# os.system("clear")

def variableconfig():
    ENV['TRASHPANDA_HOST'] = "trashpanda.pwsz.nysa.pl"
    ENV['CLOUD_MAX_FILE_SIZE'] = '1MB'
    ENV['CLOUD_PROJECT_PATH'] = os.getcwd()
    ENV['CLOUD_TRASHBOX'] = '/srv/Data/'
    ENV['CLOUD_DUMP'] = "/srv/Data/DUMP/" if FileManager.createFolder('/srv/Data/DUMP/') else "jebudu"
    ENV['TRASHPANDA_LOGIN'] = ENV['TRASHPANDA_LOGIN'] if 'TRASHPANDA_LOGIN' in ENV  else "sergiy1998"
    ENV['TRASHPANDA_PASSWD'] = ENV['TRASHPANDA_PASSWD'] if 'TRASHPANDA_PASSWD' in ENV else "hspybxeR98>"
    print("[*] Configurate Variables...")

variableconfig()
print(tmp.TrashPandpa())


