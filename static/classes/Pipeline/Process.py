from subprocess import Popen, PIPE
import pickle
import threading

class Process():
    """ Process is one serialized element to interpreting """

    def __init__(self, func, values, controller):
        self.function = func
        self.parameter = values
        self.controller = controller


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
