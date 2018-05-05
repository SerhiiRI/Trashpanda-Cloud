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
from static.tool.Logs import Log, LogType
from os import environ as ENV
# TODO: hackerman-style init script: dużo hakowania....
# rows, columns = os.popen('stty size', 'r').read().split()


@Log(LogType.INFO, 1, " Main TRASHPANDA config", printToConsole=False)
def variableconfig():
    ENV['TRASHPANDA_HOST'] = "trashpanda.pwsz.nysa.pl"
    ENV['CLOUD_MAX_FILE_SIZE'] = '1MB'
    ENV['CLOUD_DOWNLOAND_DAMP'] = '/srv/Dump/'
    ENV['CLOUD_PROJECT_PATH'] = os.getcwd()
    ENV['CLOUD_TRASHBOX'] = '/srv/Data/'
    ENV['TRASHPANDA_LOGIN'] = ENV['TRASHPANDA_LOGIN'] if 'TRASHPANDA_LOGIN' in ENV  else ""
    ENV['TRASHPANDA_PASSWD'] = ENV['TRASHPANDA_PASSWD'] if 'TRASHPANDA_PASSWD' in ENV else ""
    print("[*]Configurate Variables...")

variableconfig()
print(tmp.TrashPandpa())

