from ..BrainClient import Brain
from ..Threading import ThreadWithReturnValue
import socket
import random
import pickle
import codecs
import copy


class Agent:#(ThreadWithReturnValue):

    def __init__(self, client_set : dict,  price: int = 100, host="0.0.0.0", ports=list()):
        """
        Creating ID to client, and wainting for love... waiting for love... tu-tu-tu
        :var ClientID
        """

        # Clinet Logic
        self.Brain = Brain(pref_price=price)

        self.ports = ports
        self.host = host


        self.pref_price = price
        self.resources = client_set
        self.resources["id"] = random.randint(1, 100000)
        self.ClientID = str(random.randint(0, 100))
        self.count_of_function = ( "factorial", str(random.randint(0, 5000)))
        self.PAGENT = list()
        #super(Agent, self).__init__()

    def run(self):
        print(self.resources)
        def iterator(LIMIT=None):
            LIMIT = len(self.ports)
            float_range = lambda Iterator: Iterator % LIMIT
            i = 0
            while (1):
                yield self.ports[i] if not LIMIT else self.ports[random.randint(0, LIMIT-1)]
                i += 1
        counter = iterator()
        for port in counter:
            print("------------ID CLIENTA > "+str(self.resources["id"]))
            Switch = self.hand_shacking(target_host=self.host, target_port=port, type_hs=self.Brain.GetHandShackingType(port=port))
            if Switch[0]:
                return tuple((self.host, port, Switch[1], Switch[2]))

    def hand_shacking(self, type_hs, target_port: int, target_host: str="0.0.0.0"):
        host = target_host
        port = target_port
        data = self.sendTo(host, port, self.generateDictOrder(type_hs, port)).split("|")
        if len(data) == 2:
            self.Brain.update(port=int(data[0]), price=int(float(data[1])))
            print("[  GET  ]> Port: {}; Price: {}zl ".format(*data))
        elif len(data) == 3:
            print("[ACCEPT ]> Host: {}:{}, status:{}".format(*data))
        elif len(data) == 4:
            print("[ Finalize ] {}:{} cena{} status: {}".format(*data))
        else:
            print("[  ERR  ]> Please count of data ")
        return (True, data[2], data[3]) if type_hs == "finalize" else (False, 0)

    def generateDictOrder(self, req_type: str, port: int):
        #print(self.resources)
        port = int(port)
        if port in self.Brain.PortCollection:
            self.resources["price"] = self.Brain.PortCollection[port][-1]
        return req_type+'|' + codecs.encode(pickle.dumps(self.resources), "base64").decode()

    def sendTo(self, host, port, requst):
        client = socket.socket
        try:
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect((host, int(port)))
                client.send(bytearray(requst, encoding="unicode-escape"))
            except ConnectionError as socketConnectionError:
                print(socketConnectionError, " the host {} can not be reached".format(host))
                raise IOError
            responce = client.recv(2048)
            return str(responce, encoding="unicode-escape")
        except IOError as socketError:
            print(socketError, " problem with sending message to server")
            client.close()
        except Exception as othertype:
            print("Problem innego typu ", othertype)
        except KeyboardInterrupt:
            print("[k] Keyboard stop")
        return None
