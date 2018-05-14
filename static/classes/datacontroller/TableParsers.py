import re, random
from copy import deepcopy


class TableTypeParser(object):

    def __init__(self, MetaTable : list):
        self.__DataBaseTableField = MetaTable[1:]
        self.Meta_FieldList = self._CreateMeta()
        print(MetaTable)
        self.Lambda_FieldList = self.__addLambdasToList(self.Meta_FieldList)

    def _CreateMeta(self):
        temp = list()
        for column, typeof in self.__DataBaseTableField:
            temp.append([column, *((re.split(r'[()]', typeof)[0:-1]))] if re.search(r'\([0-9]{1,4}\)', typeof) else [column, typeof, "100"] )
        return temp

    def __lambda__radomizator(self, typ : str, limiter : int = 20, Prefix = "", StringSet : str =" qwertyuiopasdfghjklzxcbvbnm", NumberSet : str ="1234567890", SymbolSet : str ="./,_-+()"):
        String = StringSet + NumberSet
        if (typ == "varchar" or typ == "text"):
            return lambda pre="": '{}{}'.format(pre if(len(pre) > 1) else Prefix,\
                "".join([random.choice(String) for _ in range(int(limiter) - 2 - len(pre if(len(pre) > 1) else Prefix))]))
        elif (typ == "int"):
            return lambda x = 0 : random.choice(range(int(limiter)+1))
        else:
            return lambda x = 0 : 0

    def __addLambdasToList(self, listToChange : list):
        temp = list()
        for meta in listToChange:
            meta_column, meta_type, meta_type_len = deepcopy(meta)
            temp.append((self.__lambda__radomizator(typ=meta_type, limiter=meta_type_len), meta_type_len, meta_column, meta_type))
        return temp
