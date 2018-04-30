#!/usr/bin/python3
"""
               Logs
Describe:
Module stwożony z calem realizacji systemu
uwiadomien dla servera z różnych żródl da-
nych, które będą rozeslane po różnych pli-
kach w systemie zmontowanej przez dockeria
Glówne żrdla konfiguracji są takie ścieżki
------------------------------------------
Dependent Path:
 static/config/configurations.py - gdzie
jest zawarte pliki logów do w slowniku o
nazwie "Files"
 static/config/statuscode.py - w pliku je-
st jeden Slownik z przeliczeniam dla każd-
ej sytuacji odpowiedniego systemowego uwi-
adomienia
------------------------------------------
How to:
Używania klasy decoratora Log:
TODO: dopisz wszystko co jest na używania logów, taki maly poradnik, kopie go dodaj do środka LOG
1. Log
author: Serhii Riznychuk
"""

# DateTime - klasa importowania dla fiksowania czasu w pewny okres czasu, korzystając z metody .now()
from datetime import datetime
# Importowania ścieżek plikowych do potrzeb klasy "log"
from static.configs.configurations import FILES
# Importowania status kodów
# TODO:  wyjebać tabele z BazyDach "system_logs"
from static.configs.statuscode import STATUSCODE
# decorator for renaming function
from functools import wraps

class LogType(object):
    '''
           LogType
     Klasa stworzona po to żebym
    przekazywać objekt bledu na
    server i dockladnie określić
    go dzialania po wykonywaniu
    zależnej od dekoratora funk-
    cyj.
     Klasa zawiera atrybuty, kt-
    óre pobierają caly set danych
    do konfiuguracji w poszczeg-
    ólnych dzialaniach w klasie

    author: Serhii Riznychuk
    '''
    ERROR = None
    INFO = None
    WARNING = None
    CRITICAL = None
    PRINTONLY = None

    def __init__(self):
        self.ERROR = self._ret_tuple(FILES["logs"]["system_error_file"], codeCategory="01")
        self.INFO = self._ret_tuple(FILES["logs"]["system_messg_file"], codeCategory="03")
        self.WARNING = self._ret_tuple(FILES["logs"]["system_alert_file"], codeCategory="04")
        self.CRITICAL = self._ret_tuple(FILES["logs"]["system_error_file"], codeCategory="02")
        self.PRINTONLY = self._ret_tuple()

    def _ret_tuple(self, pathFilePath=FILES["logs"]["server_file"], printToConsole=1, codeCategory="00"):
        """
        Metoda zbiera przekazane konfiguracyjne
        parametry do jednego Tupla i przekazuje
        ich returnem
        :param pathFilePath: ścieżka do chronienia log-a na serverze fizycznym
        :param printToConsole: jeżęli param ma 0 - wiadomość log-a nie będzie wyświetlona w konsoli
        :param codeCategory: wybiera ze slównika potrzebny typ log-a
        :return: zwracane są upakowane dane w postaci Tuple-objecta
        """
        list_ = (pathFilePath, printToConsole, codeCategory, STATUSCODE[codeCategory])
        return list_


class Log(object):
    # setap list function for map collision in
    _func_pipeline = list()
    _DATA_SET = dict()
    # TODO: toEmail | creation a tuple list in constructor for function | add function to create  a file with spesioal extention 
    def __init__(self, logtype: tuple, statusCode : int, message : str,  toEmail="",  ServerFile=FILES["logs"]["server_file"]):
        # a, b, c, d = tuple()
        self.SystemFilePath, self.printToConsole, self.codeCategory, self.CODES = logtype
        # a, b, c, d = 1, 2, 3, 4
        self.message, self.statusCode, self.ServerFile = message, statusCode, ServerFile


    def __call__(self, func):
        """
             Log Decorator
        :param func: function to change
        """
        @wraps(func)
        def decorator(*argv,**kwargs):
            self._makeDataSET(func.__name__, argv, kwargs)
            with open(self.SystemFilePath, "a") as file:
                file.write(self._createLine())
            func(argv, kwargs)

    def _makeDataSET(self, fname: str, *args, **kwargs):
        def metadata(func):
            # Używam karringu tylko dla przezroczystości wykorzystywania
            self._DATA_SET["functionname"] = func.__name__
            self._DATA_SET["arguments"] = func.__code__.co_varnames
        self._DATA_SET["filename"] = fname
        self._DATA_SET["datetime"] = str(datetime.now())
        self._DATA_SET["logtype"] = self.CODES["type"]
        self._DATA_SET["message"] = self.message
        self._DATA_SET["globalcodenumber"] = self.codeCategory+"x"+str(self.statusCode)
        self._DATA_SET["codenumber"] = str(self.statusCode)
        self._DATA_SET["code"] = self.CODES
        self._DATA_SET["arguments_list"] = self._getArgument(args, kwargs)
        return metadata

    def _getArgument(self, *args, **kwargs) -> list:
        list_temp =  zip(self._DATA_SET["arguments"], args)
        arguments = list(list_temp)
        kwargumets = list()
        for kwrg, _ in kwargs.items():
            temp = (str(kwrg)+"*", str(kwargs[kwrg]))
            kwargumets.append(temp)
        return arguments + kwargumets

    def _createLine(self) -> str:
        Log = "FUN:"+self._DATA_SET["functionname"]\
              +" TIME:"+self._DATA_SET["datetime"]\
              +" CODE:"+self._DATA_SET["globalcodenumber"]\
              + "SMES: "+self._DATA_SET["code"][ int(self._DATA_SET["codenumber"]) ]\
              +" MES:"+self._DATA_SET["message"]
        return Log

    # TODO: quick converter <dict()> type to XML
    def _createDataXML(self):
        raise NotImplementedError

    # TODO: quick converter <dict()> type to JSON
    def _createDataJSON(self):
        raise NotImplementedError

    # TODO: quick converter <dict()> to compress string line No more 200 symbols
    def _createKeyValue(self):
        raise NotImplementedError

    # TODO: Only for console represents view readable <dict()> type
    def _createReadable(self):
        raise NotImplementedError

    def backParser(self, oneOfFormat):
        raise NotImplementedError
