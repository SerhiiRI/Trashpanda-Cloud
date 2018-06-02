from multiprocessing import Queue
from static.classes.Pipeline.PipeBuilder import PipeBuilder
import socket
import threading
import pickle
import codecs
import random


class Agent:

    def __init__(self, dictionary, host: str="0.0.0.0", port: int=9999):
        self.AgentDictionary = dictionary
        self.MainQueue = Queue()
        # ip and port to listening
        self.bind_ip = host
        self.bind_port = port

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.bind_ip, self.bind_port))
        try:
            self.server.listen(5)
        except:
            self.server.close()

    def __handle_client(self, client_socket: socket):
        request = client_socket.recv(1024)
        # print("[#] Odebrano : ", str(request, encoding="unicode-escape"))
        selfproto, data = str(request, encoding="unicode-escape").split("|")
        print(data)
        if(selfproto == "order"):
            data = pickle.loads(codecs.decode(data.encode(), "base64"))
            responce = bytearray(self.compatible(data)+self.generate_price(data["fun"]),encoding="unicode-escape")
        elif(selfproto == "accept"):
            data = pickle.loads(codecs.decode(data.encode(), "base64"))
            responce = bytearray("{}|{}".format(self.bind_ip, self.bind_port), encoding="unicode-escape")
        else:
            responce = bytearray("[!] EMPTY REQUEST")
        print("[^] Wysylania packeta z powrotem")
        client_socket.send(responce)
        client_socket.close()

    def compatible(self, dictionary):
        """
        :name Сompatible

        Agent testing, dictionary set,
        sended by client, for persent
        of compatibility to client --
        agent neededs

        :param dictionary:
        :return: persents in format {}|{}
                 where <|> is a spliter char

        @Serhii Riznychuk
        """
        x = lambda z: 100 if z > 100 else z
        cpu = self.AgentDictionary["machine"]["cpu"] / dictionary["machine"]["cpu"] *100
        disk = self.AgentDictionary["machine"]["disk"] / dictionary["machine"]["disk"] *100
        ram = self.AgentDictionary["machine"]["ram"] / dictionary["machine"]["ram"]*100
        factorial = self.AgentDictionary["function"]["factorial"] / dictionary["function"]["factorial"]*100
        bublesort = self.AgentDictionary["function"]["bublesort"] / dictionary["function"]["bublesort"]*100
        searching = self.AgentDictionary["function"]["searching"] / dictionary["function"]["searching"]*100
        machine = ((x(cpu) + x(disk) + x(ram)) / 3)
        function = (x(factorial) + x(bublesort) + x(searching)) / 3
        return "{}|{:.2f}|{:.2f}|".format(self.bind_port, machine,  function)

    def generate_price(self, func):
        price = random.randint(6, 20) * self.AgentDictionary["function"][func] / 10

        return "{:.2f}".format(price)

    def listening(self):
        print("[INFO] address [ {}:{} ] Start-up Agent-server ".format(self.bind_ip, self.bind_port))
        while True:
            try:
                client, addr = self.server.accept()
                print("[!] get connect from agent.IP:[ {}:{} ]".format(addr[0], addr[1]))
                client_handler = threading.Thread(target=self.__handle_client, args=(client,))
                client_handler.start()
            except KeyboardInterrupt:
                print("[!] Server keyboard interrupt, starting listening")
                break

    # ------------{PIPE-MANAGER}-------------#

    def _defineFunctionality(self, function, pathToController): # self.PipeBuilder = PipeBuilder(factorial "/home/serhii/Projects/llapCloudFlask/static/tool/Binary/cpuController")
        del (self.MainQueue)
        self.Builder = PipeBuilder(function, pathToController)
        self.MainQueue = self.Builder.buildQueue()

    def _run(self) -> int:
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

    def _ObliczniaWykonywanejWagi(self):
        pass



