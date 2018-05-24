from multiprocessing import Queue
from functools import wraps
from static.classes.Pipeline.AvailableFunctions.FunctionList import factorial
from static.classes.Pipeline.Container import Container
from static.classes.Pipeline.PipeBuilder import PipeBuilder

class Agent:

    def __init__(self, Dictionary):
        self.AgentDictionary = Dictionary
        self.MainQueue = Queue()

    def defineFunctionality(self, function, pathToController): # self.PipeBuilder = PipeBuilder(factorial, "/home/serhii/Projects/llapCloudFlask/static/tool/Binary/cpuController")
        del (self.MainQueue)
        self.Builder = PipeBuilder(function, pathToController)
        self.MainQueue = self.Builder.buildQueue()

    def run(self) -> int:
        if(self.MainQueue.qsize() == 0):
            return -1
        iteration = 0
        while(1):
            try:
                container = self.MainQueue.get(block=True)
                if container.start():
                    raise Exception("[*] Load")
                iteration += 1
            except Exception as e:
                print(e)
                del(self.MainQueue)
                break
        return iteration

    def ObliczniaWykonywanejWagi(self):
        pass