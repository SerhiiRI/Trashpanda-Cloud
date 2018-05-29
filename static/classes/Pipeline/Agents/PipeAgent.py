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
        self.server.listen(5)

    def __handle_client(self, client_socket: socket):
        request = client_socket.recv(1024)
        # print("[#] Odebrano : ", str(request, encoding="unicode-escape"))
        selfproto, data = str(request, encoding="unicode-escape").split("|")

        if(selfproto == "connect"):
            data = pickle.loads(codecs.decode(data.encode(), "base64"))
            responce = bytearray(self.compatible(data),encoding="unicode-escape")
        elif(selfproto == "get"):
            data = pickle.loads(codecs.decode(data.encode(), "base64"))
            responce = bytearray(self.generate_price(data), encoding="unicode-escape")
        else:
            responce = bytearray("[!] EMPTY REQUEST")

        print("[^] Wysylania packeta z powrotem")
        client_socket.send(responce)
        client_socket.close()


    def compatible(self, dictionary):
        """
        :name compatible

        Agent testing, dictionary set,
        sended by client, for persent
        of compatibility to client --
        agent neededs

        :param dictionary:
        :return: persents in format {}|{}
                 where <|> is a spliter char

        @Serhii Riznychuk
        """
        cpu = self.AgentDictionary["machine"]["cpu"] / dictionary["cpu"]* 100
        disk = self.AgentDictionary["machine"]["disk"] / dictionary["disk"]* 100
        ram = self.AgentDictionary["machine"]["ram"] / dictionary["ram"]* 100
        factorial = self.AgentDictionary["function"]["factorial"] / dictionary["function"]["factorial"]
        bublesort = self.AgentDictionary["function"]["bublesort"] / dictionary["function"]["bublesort"]
        searching = self.AgentDictionary["function"]["searching"] / dictionary["function"]["searching"]
        final = "Compat(c={}=d{}r={}) : {}".format(cpu, disk, ram, str((cpu + disk + ram) / 3))
        return "{}|{}".format(((cpu+disk+ ram) / 3), (factorial + bublesort+ searching)/3)

    def generate_price(self, dictionary):
        price = int(dictionary[1]) * random.randint(0, 100) * self.AgentDictionary["function"][dictionary[0]]
        return "Price for order {}.00 zl".format(price)

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

"""

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

    def _bind

"""