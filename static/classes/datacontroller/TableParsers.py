import re, random
from copy import deepcopy
from static.tool.console.vt1000 import BackGround as bg, FormatCode as cd, ForeGround as fg
import datetime

class TableTypeParser(object):

    def __init__(self, MetaTable : list):
        self.__DataBaseTableField = MetaTable[1:]
        self.Meta_FieldList = self._CreateMeta()
        self.Lambda_FieldList = self.__addLambdasToList(self.Meta_FieldList)

    def _CreateMeta(self):
        temp = list()
        for column, typeof in self.__DataBaseTableField:
            temp.append([column, *((re.split(r'[()]', typeof)[0:-1]))] if re.search(r'\([0-9]{1,4}\)', typeof) else [column, typeof, "100"] )
        return temp

    def __lambda__radomizator(self, typ : str, limiter : int = 150, Prefix = "", StringSet : str ="qwertyuiopasdfghjklzxcbvbnm", NumberSet : str ="1234567890", SymbolSet : str ="./,_-+()"):
        String = StringSet + NumberSet
        if (typ == "varchar" or typ == "text"):
            return lambda x = 0: "{}".format("".join([random.choice(String) for _ in range(int(limiter) - 3)]))
        elif (typ == "int"):
            return lambda x = 0 : random.choice(range(int(500)))+1
            #return lambda x = 0 : x
        elif (typ == "datetime"):
            return lambda x = 0 : datetime.datetime.now()
        elif (typ == "date"):
            return lambda x = 0 : datetime.date.today()
        else:
            return lambda x = 0 : 0

    def __addLambdasToList(self, listToChange : list):
        temp = list()
        for meta in listToChange:
            meta_column, meta_type, meta_type_len = deepcopy(meta)
            temp.append((self.__lambda__radomizator(typ=meta_type, limiter=meta_type_len), meta_type_len, meta_column, meta_type))
        return temp

    def printLambdaColumnTemplate(self):
        print(fg.cyan+cd.bold+"{:^150}".format("LAMBDA field")+cd.reset)
        for x in self.Lambda_FieldList:
            func, *cost = x
            print(bg.green+fg.black+cd.underline+str(func)+cd.reset+" -> LIMITER:"+bg.lightgrey+fg.black+cd.bold+"{:>5}".format(str(cost[0]))+cd.reset+" -> COLUMN:"+bg.black+fg.white+"{:^18}".format(str(cost[1]))+cd.reset)

    def printMetaColumnTemplate(self):
        print(fg.cyan + cd.bold + "{:^50}".format("META field") + cd.reset)
        column = lambda x : cd.bold+fg.black+bg.white+"{:^18}".format(str(x))+cd.reset
        meta = lambda x : fg.white+bg.black+"{:^12}".format(str(x))+cd.reset
        print("\n".join([ column(x[0])+" : "+meta(x[1])+" : "+meta(x[2]) for x in self.Meta_FieldList]))