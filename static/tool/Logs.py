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
 static/config/MainConf.py - gdzie
jest zawarte pliki logów do w slowniku o
nazwie "Files"
 static/config/StatusCode.py - w pliku je-
st jeden Slownik z przeliczeniam dla każd-
ej sytuacji odpowiedniego systemowego uwi-
adomienia








How to:
Używania klasy decoratora Log:

       [] - parameter nie obowiązkowy

       statuscode - pliki z status kodów

@Log(LogType.Error, 3, "message about action", ["mail@mail.com",] ["/home/user/cloud/.../"])
def function()....

      1. LogType.<ERROR | INFO | WARNING | CRITICAL | SYSTEM_ONLY> - typy blędów
      2. 3 - kod reakci Log-a
      3. "message to file..." - Nasztywno napisana wiadomość do użytkownika
      Kluczy:
      4. ["mail@mail.com",] - mail do odeslania logów.
      5.["/home/user/cloud/.../"] - ścieżka do drugiego pliku, przechowywanego na server

Examples:
      @Log(LogType.Error, 3, "message about action")

author: Serhii Riznychuk
"""

# DateTime - klasa importowania dla fiksowania czasu w pewny okres czasu, korzystając z metody .now()
from datetime import datetime
# Importowania ścieżek plikowych do potrzeb klasy "log"
from static.configs.MainConf import FILES
# imoprt vt1000 console code s
from static.tool.console.vt1000 import ForeGround as fg, FormatCode as cd, BackGround as bg
# Importowania status kodów
# TODO:  wyjebać tabele z BazyDach "system_logs"
from static.configs.StatusCode import STATUSCODE
# decorator for renaming function
from functools import wraps

class _LogType(object):
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
    def __init__(self):
        self.ERROR = self._ret_tuple(FILES["logs"]["system_error_file"], codeCategory="01")
        self.INFO = self._ret_tuple(FILES["logs"]["system_messg_file"], codeCategory="03")
        self.WARNING = self._ret_tuple(FILES["logs"]["system_alert_file"], codeCategory="04")
        self.CRITICAL = self._ret_tuple(FILES["logs"]["system_error_file"], codeCategory="02")
        self.SYSTEM_ONLY = self._ret_tuple()

    def _ret_tuple(self, pathFilePath=FILES["logs"]["server_file"], printToConsole=1, codeCategory="01"):
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


class LogType(object):
    ERROR = _LogType().ERROR
    INFO = _LogType().INFO
    WARNING = _LogType().WARNING
    CRITICAL = _LogType().CRITICAL
    SYSTEM_ONLY = _LogType().SYSTEM_ONLY

class Log(object):
    # setap list function for map collision in
    _func_pipeline = list()
    _DATA_SET = dict()

    # TODO: toEmail
    # TODO: creation a tuple list in constructor for function
    # TODO: add function to create  a file with spesioal extention

    def __init__(self, logtype: tuple, statusCode : int, message : str, printToConsole=False,  toEmail="",  ServerFile=FILES["logs"]["server_file"]):
        # a, b, c, d = tuple()
        self.SystemFilePath, self.printToConsole, self.codeCategory, self.CODES = logtype
        # a, b, c, d = 1, 2, 3, 4
        self.message, self.statusCode, self.ServerFile = message, statusCode, ServerFile
        self.printToConsole = printToConsole

    def __call__(self, func):
        """
             Log Decorator
        :param func: function to change
        """
        @wraps(func)
        def decorator(*argv,**kwargs):
            self._makeDataSET(func)(func.__name__, *argv, **kwargs)
            with open(self.SystemFilePath, "a+") as file:
                file.write(self._createLine())
            # opcja zapisywania do konsoli
            if(self.printToConsole):
                print(self._createLine(colorise=self.printToConsole))
            func(*argv, **kwargs)
        return decorator

    def _makeDataSET(self, func):
        self._DATA_SET["functionname"] = func.__name__
        self._DATA_SET["arguments"] = func.__code__.co_varnames

        def metadata(fname: str, *args, **kwargs):
            """ Używam karringu tylko dla przezroczystości wykorzystywania """
            # destination log-file path
            self._DATA_SET["filename"] = fname
            # current data and time
            self._DATA_SET["datetime"] = str(datetime.now())
            # types of log( error, critical, info, warning)
            self._DATA_SET["logtype"] = self.CODES["type"]
            # VT1000 colorize for console output
            self._DATA_SET["fcolor"] = self.CODES["fcolor"]
            # -//-
            self._DATA_SET["bcolor"] = self.CODES["bcolor"]
            # InScope Log() message to destination
            self._DATA_SET["message"] = self.message
            # GLOBAL CODE - not used
            self._DATA_SET["globalcodenumber"] = self.codeCategory + "x" + str(self.statusCode)
            # status code of category
            self._DATA_SET["codenumber"] = str(self.statusCode)
            # lista kodów przeslanych lącznie z ślownikeim
            self._DATA_SET["code"] = self.CODES
            # list of functoin arguments
            self._DATA_SET["arguments_list"] = self._getArgument(*args, **kwargs)
        return metadata

    def _getArgument(self, *args, **kwargs) -> list:
        list_temp =  zip(list(self._DATA_SET["arguments"]), list(args))
        arguments = list(list_temp)
        kwargumets = list()
        for kwrg, _ in kwargs.items():
            temp = (str(kwrg)+"*", str(kwargs[kwrg]))
            kwargumets.append(temp)
        return arguments + kwargumets

    def _createLine(self, colorise = False) -> str:
        color = lambda x : (self._DATA_SET["fcolor"]+self._DATA_SET["bcolor"]+x+cd.reset) if colorise==True else x
        Log = color("FUNCTION NAME ")+self._DATA_SET["functionname"]\
              +color(" TYPE ")+self._DATA_SET["logtype"]\
              +color(" TIME ")+self._DATA_SET["datetime"]\
              +color(" CODE ")+self._DATA_SET["globalcodenumber"]\
              +color(" SYSTEM MESSAGE ")+self._DATA_SET["code"][ int(self._DATA_SET["codenumber"]) ]\
              +color(" MESSAGE ")+self._DATA_SET["message"]\
              +color(" ARGUMENTS ")+" ".join(str(vname)+"='"+str(vvalue)+"'" for vname, vvalue in self._DATA_SET["arguments_list"])+"\n"
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

    def _backParser(self, oneOfFormat):
        raise NotImplementedError
