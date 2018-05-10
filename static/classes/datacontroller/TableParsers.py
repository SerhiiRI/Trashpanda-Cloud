import re, random
from copy import deepcopy

class TableTypeParser(object):

    def __init__(self, MetaTable : dict):
        self.Meta_FieldList = list()
        # Temp Talbe
        self.__DataBaseTableField = MetaTable
        self._CreateMeta()
        self.Lambda_FieldList = self.__addLambdasToList()

    def _CreateMeta(self):
        temp = list()
        for column, typeof in self.__DataBaseTableField:
            temp.append((column, *(re.split(r'[()]', typeof)[0:-1] if re.search(r'\([0-9]{1,4}\)', typeof) else [typeof, "1000"])))
        self.__DataBaseTableField = temp

    def __lambda__radomizator(self, typ : str, limiter : int = 20, Prefix = "", StringSet : str =" qwertyuiopasdfghjklzxcbvbnm", NumberSet : str ="1234567890", SymbolSet : str ="./,_-+()"):
        String = StringSet + NumberSet + SymbolSet
        if (typ == "varchar" or typ == "text"):
            return lambda pre="": '"{}:{}"'.format(pre if(len(pre) > 1) else Prefix,\
                "".join([random.choice(String) for _ in \
                         range(limiter - 1 - len(pre if(len(pre) > 1) else Prefix))]))
        elif (typ == "int"):
            return lambda x=0 : random.choice(range(limiter))
        else:
            return lambda x=0: 0


    def __addLambdasToList(self):
        self.Lambda_FieldList = list()
        for meta in self.__DataBaseTableField:
            meta_column, meta_type, meta_type_len = deepcopy(meta)
            self.Lambda_FieldList.append((self.__lambda__radomizator(meta_type, meta_type_len), meta_type_len, meta_column, meta_type))
        return 0
