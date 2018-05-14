from static.classes.datacontroller.SQLController import SQLCloud
from static.classes.datacontroller.TableParsers import TableTypeParser


class TableFillController(SQLCloud, TableTypeParser):

    def __init__(self, database : str = "test_cloud", tablename: str="users"):
        SQLCloud.__init__(self, database)
        self.table = tablename
        self._getTableMeta(table_name=tablename)
        TableTypeParser.__init__(self, self._getTableMeta(table_name=tablename))
        print(self.Meta_FieldList)
        print(self.Lambda_FieldList)
        # self._DBTypeDICT = list(self._DBTypeDICT[1:])

    def fill(self, record_count : str = 3) -> None:
        InsertFunction = self.insert(self.table)
        GeneratorFuncion = [ temp[0] for temp in self.Lambda_FieldList ]
        for x in range(int(record_count)):
            keylist = list(map(lambda f: f(), GeneratorFuncion))
            #print(keylist)
            #a1, *a2 = keylist

            #print(a1, "-----", x)
            #InsertFunction(x+1, *a2)
            InsertFunction(keylist)

