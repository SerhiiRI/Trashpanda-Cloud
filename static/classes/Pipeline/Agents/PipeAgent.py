from static.classes.Pipeline.PipeBuilder import PipeBuilder
from static.classes.Pipeline.Controller import ControllerServer

import socket
import threading
import pickle
import codecs
import random


class Agent:

    def __init__(self, dictionary, host: str="0.0.0.0", port: int=9999):

        self.manager = PipeBuilder(port, "/home/serhii/Projects/llapCloudFlask/static/tool/Binary/cpuController")
        self.CPUserver = ControllerServer("/home/serhii/Projects/llapCloudFlask/static/tool/Binary/cpuController" )
        self.CPUserver.start()
        self.Lock = threading.RLock

        self.AgentDictionary = dictionary
        # ip and port to listening
        self.bind_ip = host
        self.bind_port = port

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.bind_ip, self.bind_port))
        try:
            self.server.listen(6)
        except:
            self.server.close()

    def __handle_client(self, client_socket: socket):
        request = client_socket.recv(1024)
        selfproto, data = str(request, encoding="unicode-escape").split("|")
        #print(data)
        if(selfproto == "order"):
            data = pickle.loads(codecs.decode(data.encode(), "base64"))
            responce = bytearray(self.compatible(data)+self.generate_price(), encoding="unicode-escape")
        elif(selfproto == "accept"):
            data = pickle.loads(codecs.decode(data.encode(), "base64"))
            responce = bytearray("{}|{}".format(self.bind_ip, self.bind_port), encoding="unicode-escape")
            ### test function value
            for _ in range(data["function"]["factorial"]):
                self.manager.addProcess("factorial", 5)
            for _ in range(data["function"]["bublesort"]):
                self.manager.addProcess("bublesort", list(range(random.randint(1,10))))
            for _ in range(data["function"]["searching"]):
                self.manager.addProcess("searching", [random.choice("qwertyusdfghjklxcvbnm") for _ in range(random.randint(5, 10))], random.choice("qwertyusdfghjklxcvbnm"))
            #self.manager.addProcess("bublesort", list(range(random.randint(1,10))))
            #self.manager.addProcess("searching", ["a", "d", "f"], "dasf")
            self.manager.buildQueue(mechanic_of_cpu=self.CPUserver.get_cpu, cpu_percent=self.generate_critical_cpu(data=data))
            self.run()
        else:
            responce = bytearray("[!] EMPTY REQUEST")
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
        self.Machine_price=((self.AgentDictionary["machine"]["cpu"] + self.AgentDictionary["machine"]["disk"] + self.AgentDictionary["machine"]["ram"]) / 3)
        self.User_price = ((dictionary["function"]["factorial"]+ dictionary["function"]["bublesort"]+ dictionary["function"]["searching"] / 3))
        return "{}|{:.2f}|{:.2f}|".format(self.bind_port, machine,  function)

    def generate_price(self):
        price = random.randint(1, 11) / 10 * ((self.Machine_price + self.User_price) / 2)
        return "{:.2f}".format(price)

    def generate_critical_cpu(self, data):
        return lambda: int(data["machine"]["cpu"])

    def listening(self):
        print("[INFO] address [ {}:{} ] Start-up Agent-server ".format(self.bind_ip, self.bind_port))
        while True:
            try:
                client, addr = self.server.accept()
                print("[!] get connect from agent.IP:[ {}:{} ]".format(addr[0], addr[1]))
                client_handler = threading.Thread(target=self.__handle_client, args=(client,))
                client_handler.start()
            except KeyboardInterrupt:
                print("[!] Server keyboard interrupt, stoping listening")
                self.CPUserver.TThread.do_run = False
                self.manager.deleteTable()
                self.CPUserver.join()
                self.server.close()
                del (self.manager)
                del (self.CPUserver)
                del (self.server)
                del (self.Lock)
                break
            except RuntimeError as re:
                self.CPUserver.TThread.do_run = False
                self.manager.deleteTable()
                self.CPUserver.join()
                self.server.close()
                del (self.manager)
                del (self.CPUserver)
                del (self.server)
                break

    # ------------{PIPE-MANAGER}-------------#

    def run(self) -> int:
        if self.CPUserver.CPU > 0 and self.CPUserver.CPU < 90:
            for _ in range(0,  self.manager.queue.__len__()):
                try:
                    container = self.manager.queue.pop()
                    container.start()
                except Exception as e:
                    break
        return 0
