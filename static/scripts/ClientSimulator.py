#!/usr/bin/python3
from os import popen
from static.tool.console.vt1000 import ForeGround as fg, BackGround as bg, FormatCode as cd
import npyscreen

"""
ten skrypt genteruje symulacje użytkowników 
dla systemy wieloagentowej. dla twożenia 
kolejek zadan na innych wirtualnych mazsyn-
ach, pod docker-systemem

"""



class MyView(object):
    min_columns = 100


    def __int__(self):
        self.lim_rows, self.lim_columns = popen("stty size", "r").read().split()

    def createWindows(self, functionToDecorate,  ValueItems : list,  symbol="*"):
        self.__maxElementInList(ValueItems)
        def function():
            header = "".join((symbol for x in range(self.columns)))
            header = fg.cyan + header + cd.reset
            functionToDecorate()
            footer = "".join((symbol for x in range(self.columns)))
            footer = fg.cyan + header + cd.reset
        return function()

    def decorateList(self, functionToDecorate):
        nwlist = list()
        map ()
        return

    def __maxElementInList(self, items: list):
        Fmax = self.min_columns
        comparing = lambda x, m: x if x > m else m
        for x in items:
            self.min_columns = comparing(x, self.min_columns)


    def __control_col(self, string, symbol="*" ):
        str = symbol+string
        while (len(str)+1 < self.lim_columns):
            str = str+" "
        str += symbol
        return str