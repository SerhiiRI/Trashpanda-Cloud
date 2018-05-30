#!/usr/bin/python3
from os import environ as ENV
"""
ENV['TRASHPANDA_HOST'] = "trashpanda.pwsz.nysa.pl"
ENV['CLOUD_MAX_FILE_SIZE'] = '1MB'
ENV['CLOUD_DOWNLOAND_DAMP'] = '/srv/DUMP/'
ENV['CLOUD_TRASHBOX'] = '/srv/Data/'
ENV['TRASHPANDA_LOGIN'] = ENV['TRASHPANDA_LOGIN'] if 'TRASHPANDA_LOGIN' in ENV else "sergiy1998"
ENV['TRASHPANDA_PASSWD'] = ENV['TRASHPANDA_PASSWD'] if 'TRASHPANDA_PASSWD' in ENV else "hspybxeR98>"
"""

import os
import static.configs.EnvConf
from static.controllers.Permission import Permission
from static.classes.datacontroller.SQLController import SQLCloud

rows, columns = os.popen('stty size', 'r').read().split()

los = lambda : "".join(("_" for x in range(0, int(columns))))

costam = SQLCloud.getInstance()
print(costam.DBRepr)
print(los())
print(costam.insert('banns'))
print(los())
print(costam.update('banns'))
print(los())
print(costam.select('banns'))
print(los())
print(costam.delete('banns'))
print(los())
print(costam.merge())
print(los())
print(costam.merge(*("tab_A", "idAB", "tab_B", "idBC", "tab_C")))
print(los())
print(costam.merge(*("tab_A", "idAB", "tab_B", "idBC", "tab_C"), where={"name" : "suka", "nazwisko" : "bliat"}))
print(los())

def costam_z_selectem():
    print("dane, króre pobralem z selecta")
    SQLCloud.insert_user()

print(merge.__annotations__)
