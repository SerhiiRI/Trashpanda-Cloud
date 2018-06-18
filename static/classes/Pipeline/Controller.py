from static.tool.FileManager import FileManager
from subprocess import Popen, PIPE
from functools import wraps
from threading import Thread
from threading import current_thread
import os


class Controller(object):

    def __init__(self, path):
        self.__PathToSystemCommand = path
        
    @property
    def PathToSystemCommand(self) -> str:
        """
              PathToSystemCommand
        -----------------------------------------
        zbierania danych o pliku i podciąga
        META-informacje dla interpretacji w
        system dla liczenia przez PipeBuilder-a

        @Serhii Riznychuk
        """
        return self.__PathToSystemCommand

    @PathToSystemCommand.setter
    def PathToSystemCommand(self, path: str):
        """
                PathToSystemCommand
        -----------------------------------------
        zbierania danych o pliku i podciąga
        META-informacje dla interpretacji w
        system dla liczenia przez PipeBuilder-a

        @Serhii Riznychuk
        """
        if(FileManager.testExistFile(path)):
            self.__PathToSystemCommand = path

    def verify(self, lambda_cmpr) -> bool:
        loadProcent = 0
        try:
            controllerProcess = Popen((self.__PathToSystemCommand), shell=True, stdout=PIPE)
            controllerProcess.wait()
            output = str(controllerProcess.communicate()[0], encoding="unicode-escape")
            loadProcent = float(output.lstrip())
        except BrokenPipeError as message:
            print(message)
        except Exception as message:
            print(message)
        return True if lambda_cmpr(float(loadProcent)) else False

    def proc_stat(self) -> float:
        loadProcent = 0
        try:
            controllerProcess = Popen((self.__PathToSystemCommand), shell=True, stdout=PIPE)
            controllerProcess.wait()
            output = str(controllerProcess.communicate()[0], encoding="unicode-escape")
            loadProcent = float(output.lstrip())
        except BrokenPipeError as message:
            print(message)
        except Exception as message:
            print(message)
        return loadProcent

    def VerifyDecorator(self, lambda_cmpr):
        def FunctionLogic(function):
            error = lambda: print("[!] Process Obciążenia procesora zbyt wysoke")

            @wraps(function)
            def wraper(*args, **kwargs):
                loadProcent = 0
                try:
                    controllerProcess = Popen((self.__PathToSystemCommand), shell=True, stdout=PIPE)
                    controllerProcess.wait()
                    output = str(controllerProcess.communicate()[0], encoding="unicode-escape")
                    loadProcent = float(output.lstrip())
                    print("[CPU]: {}%".format(loadProcent))
                except BrokenPipeError as message:
                    print(message)
                except Exception as message:
                    print(message)
                return function(*args, **kwargs) if lambda_cmpr(float(loadProcent)) else error()
            return wraper
        return FunctionLogic


class ControllerCPU(object):

    def __init__(self, active_cpu, percent):
        self.active_cpu = active_cpu
        self.percent = percent

    def verify(self) -> bool:
        print("{:>{size}}".format("Loading {}%, Critical {}%".format(self.active_cpu(), self.percent()), size=os.popen("stty size", mode='r').read().split()[1]))
        return True if self.active_cpu() > self.percent() else False


class ControllerServer(Thread):

    def __init__(self, path):
        self.controller = Controller(path)
        self.CPU = 0
        self.TThread = current_thread()
        Thread.__init__(self)

    def run(self):
        while getattr(self.TThread, "do_run", True):
            self.CPU = self.controller.proc_stat()

    def get_cpu(self):
        return self.CPU
