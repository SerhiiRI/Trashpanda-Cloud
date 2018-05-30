#!/usr/bin/python3

"""


testing to create template data in
trashpanda database
@Serhii Riznychuk

"""
import static.configs.EnvConf
from static.classes.datacontroller.TableFillController import TableFillController
from static.classes.datacontroller.SQLController import SQLCloud
from static.tool.console.vt1000 import getTerminalSize as gts
from static.tool.console.vt1000 import ForeGround as fg, FormatCode as cd, BackGround as bg
import sys
from os import system
# get terminal column size
_ , _columns = gts()

sqlController = SQLCloud.getInstance()
tables = [key for key in sqlController.DBRepr]
toChose = list(zip([x for x in range(len(tables))], tables))
cursorUsers = TableFillController(database="test_cloud", tablename="users")
# cursorUsers.fill(record_count=1000)
while(True):

    system("clear")
    print(bg.green + fg.white + "{:^{x}}".format("", x=_columns) + cd.reset)
    print(bg.green+cd.bold+fg.white+"{:^{x}}".format(" Field Pole ", x=_columns)+cd.reset)
    print(bg.green + fg.white + "{:^{x}}".format("", x=_columns) + cd.reset)
    print("")
    second = int(int(_columns) / 2)
    first = int(_columns) - second
    column = lambda text: bg.black+fg.white+str(text)+cd.reset
    print("\n\n".join([ ("{:>{x}} | {:<{a}}".format( "Item: "+str(number), column(tablename), x=first, a=second)) for number, tablename in toChose]))
    print()
    print( "{:-^{x}}".format("", x=_columns))
    num = 0
    try:
        num = input("Please write column NUMER >> ")
    except KeyboardInterrupt:
        print("\nbye!")
        exit(0)
    except:
        print("\nbye!")
        exit(0)
    cursor = TableFillController(database="test_cloud", tablename=toChose[int(num)][1])
    print("{:^{x}}".format(" META ", x=_columns))
    print()
    print(cursor.printMetaColumnTemplate())
    print()
    print("{:^{x}}".format(" LAMBDA ", x=_columns))
    print()
    cursor.printLambdaColumnTemplate()
    print()
    print("{:^{x}}".format(" SQL-FILL ", x=_columns))
    count = 0
    try:
        count = input("Please write count of fils >> ")
    except KeyboardInterrupt:
        print("\nbye!")
        break
    if count == 0:
        break
    cursor.fill(record_count=int(count))
    input(">> PRESS ANY KEY <<")

