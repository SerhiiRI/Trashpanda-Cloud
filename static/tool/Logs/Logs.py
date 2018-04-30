#!/usr/bin/python3
"""
               Logs
Module stwożony z calem realizacji systemu
uwiadomien dla servera z różnych żródl da-
nych, które będą rozeslane po różnych pli-
kach w systemie zmontowanej przez dockeria
Glówne żrdla konfiguracji są takie ścieżki
------------------------------------------
 static/config/configurations.py - gdzie
jest zawarte pliki logów do w slowniku o
nazwie "Files"
------------------------------------------
 static/config/statuscode.py - w pliku je-
st jeden Slownik z przeliczeniam dla każd-
ej sytuacji odpowiedniego systemowego uwi-
adomienia

author: Serhii Riznychuk
"""


from static.configs.configurations import FILES
from static.configs.statuscode import STATUSCODE


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
        list_ = (pathFilePath, printToConsole, STATUSCODE[codeCategory])
        return list_


class Log(object):

    _DATA_SET = dict()
    # TODO: toEmail |
    def __init__(self, logtype: tuple, statusCode : int, message : str,  toEmail="",  ServerFile=FILES["logs"]["server_file"]):
        self.ServerFile = ServerFile
        self.SystemFilePath, self.printToConsole, self.CODES = logtype

    def __call__(self, func):
        createStringLog = func.__name__ +

    def _createDataSET(self, fname: str):
        self._DATA_SET["filename"] = fname
        self._DATA_SET["datatime"]
        self._DATA_SET["logtype"]
        self._DATA_SET["message"]
        self._DATA_SET["code"]
        self._DATA_SET["arguments"]
        
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
