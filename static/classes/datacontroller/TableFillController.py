from static.classes.datacontroller.SQLController import SQLCloud
import re


class TableFillController(SQLCloud):

    def __init__(self, database : str = "test_cloud", tablename:str="user"):
        super(TableFillController, self).__init__(database)
        self._table__with__type(table_name=tablename)

    def printting(self):
        print(self._DBTypeDICT)

    def type_parsing(self):
        self.slownik = dict()
        for key, *_ in self._DBTypeDICT:
            self.slownik[key] = re.split(r'[()]', data[1])[0:-1] if re.search(r'\([0-9]{1,4}\)',data[1]) else [data[1],]


