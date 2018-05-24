from subprocess import Popen, PIPE
from static.classes.Pipeline.Controller import Controller

import pickle
import threading


class Process(threading.Thread):

    def __init__(self, func, values: tuple):
        self.function = func
        self.parameter = values
        threading.Thread.__init__(self)

    def run(self):
        try:
            self.function(*self.parameter)
        except RuntimeError as message:
            print("[!] Bląd krytyczny")
            print(message)
        except Exception as message:
            print("[!] Wyjątek!")
            print(message)
