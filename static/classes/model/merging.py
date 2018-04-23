#!/usr/bin/python3
import MySQLdb, random

class Merge(object):
    def __init__(self, host='trashpanda.pwsz.nysa.pl', login='sergiy1998', passwd='hspybxeR98>', db_name='test_cloud'):
        self.__connector = MySQLdb.connect(host, login, passwd, db_name)
        self.__cursor = self.__connector.cursor()
        self.__table = self.__cursor.execute("SHOW TABLES")

    def __table__Constract(self):
        __cursor = self.__connector.cursor()
        __cursor.execute("SHOW TABLES")
        tabels = __cursor.fetchall()
        data = dict()
        for tabel in tabels:
            __cursor.execute("SHOW COLUMNS FROM "+tabel[0])
            data.update({ tabel[0] : tuple([x[0] for x in __cursor.fetchall()]) })
            self.DBRepr = data


    def merge(self, *args):
        columns  = list()
        columns = [self.DBRepr(tableN) for tableN in args]
        idS = [columns[0] for __ in columns]
        outTable = set()
        for _id in idS:
            for col_list in columns:
                if (_id in col_list[:1] and col_list[0] != _id):
                    self.__merging(args[idS.index(_id)], args[columns.index(col_list)], col_list.index(_id))


    def __merging( table1: list, table2 : list, table2_id: int) -> list:
                """ mering of two table in one """
                """
                newTable = list()
                for colmns2 for table2:
                        newTable.add(colmns2,
                """
                return list()
 
