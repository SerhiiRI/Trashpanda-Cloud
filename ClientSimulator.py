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

    def decorateList(self, functionToDecorate, items):
        nwlist = list()
        nwlist = map(functionToDecorate, items)
        return nwlist

    def __control_col(self, string, symbol="*" ):
        str = symbol+string
        while (len(str)+1 < self.lim_columns):
            str = str+" "
        str += symbol
        return str

"""


import npyscreen
class TestApp(npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F  = npyscreen.Form(name = "Welcome to Npyscreen",)
        t  = F.add(npyscreen.TitleText, name = "Text:",)
        fn = F.add(npyscreen.TitleFilename, name = "Filename:")
        fn2 = F.add(npyscreen.TitleFilenameCombo, name="Filename2:")
        dt = F.add(npyscreen.TitleDateCombo, name = "Date:")
        s  = F.add(npyscreen.TitleSlider, out_of=12, name = "Slider")
        ml = F.add(npyscreen.MultiLineEdit,
               value = """try typing here!\nMutiline text, press ^R to reformat.\n""",
               max_height=5, rely=9)
        ms = F.add(npyscreen.TitleSelectOne, max_height=4, value = [1,], name="Pick One",
                values = ["Option1","Option2","Option3"], scroll_exit=True)
        ms2= F.add(npyscreen.TitleMultiSelect, max_height =-2, value = [1,], name="Pick Several",
                values = ["Option1","Option2","Option3"], scroll_exit=True)

        # This lets the user interact with the Form.
        F.edit()

        print(ms.get_selected_objects())

if __name__ == "__main__":
    App = TestApp()
    App.run()