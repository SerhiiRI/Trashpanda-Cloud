from static.classes.datacontroller.SQLController import SQLCloud
from static.classes.datacontroller.TableParsers import TableTypeParser
from MySQLdb import MySQLError


class TableFillController(SQLCloud, TableTypeParser):

    def __init__(self, database : str = "test_cloud", tablename: str="users"):
        SQLCloud.__init__(self, database)
        self.table = tablename
        TableTypeParser.__init__(self, self._getTableMeta(table_name=tablename))

    def fill(self, record_count : int = 1) -> None:
        InsertFunction = self.insert(self.table)
        GeneratorFuncion = [ temp[0] for temp in self.Lambda_FieldList ]
        for x in range(record_count):
            keylist = list(map(lambda f: f(x), GeneratorFuncion))
            print(end="\n")
            print("Insert Keylist : \t", keylist)
            try:
                InsertFunction(*keylist)
            except MySQLError:
                print("\nTHIS COLUMN NOT HAVE INDEX")







