from subprocess import Popen, PIPE
from static.classes.Pipeline.Controller import Controller

import pickle
import threading

class Process():


    def __init__(self, func, values: tuple, controllers: str):
        self.function = func
        self.parameter = values
        self.controller = controllers


    def run(self):
        try:
            controllerProcess = Popen((self.controller), shell=True, stdout=PIPE)
            controllerProcess.wait()
            controllerProcess.communicate()
            if controllerProcess.returncode:
                raise IOError
            output = controllerProcess.communicate()
            loadProcent = output[1]
            try:
                if (float(loadProcent) < 20):
                    self.function(self.parameter)
                else:
                    raise BufferError
            except BufferError:
                print("[*] Your process load processor")
            except Exception:
                print("[*] Bad` converting value - LoadProcent")
            "construct and deconstruct object"
        except:
            print("Dobra jest mocno późna godzina i ja nie rozumiem po jakiego ****** to nie dziala")
