import socket
import random
import pickle
import codecs


class Agent:
    def __init__(self, client_set : dict,  price : int = 100):
        """
        Creating ID to client, and wainting for love... waiting for love... tu-tu-tu
        :var ClientID
        """
        self.critical_price = 100
        self.pref_price = price
        self.ClientID = str(random.randint(0, 100))
        self.resources = client_set
        self.count_of_function = ( "factorial", str(random.randint(0, 5000)) )
        self.PAGENT = list()

    def hand_shacking(self, type_hs, target_port: int, target_host: str="0.0.0.0"):
        host = target_host
        port = target_port
        data = self.sendTo(host, port, self.generateDictOrder(type_hs)).split("|")
        print("\n<<<<<<<<<<<<<<<<<<")
        if len(data) == 4:
            print("port:{}\nhardware:{}%\nfunction:{}%\nprice:{}zl".format(*data))
        elif len(data) == 2:
            print("[GET] from\nAgent host:{}\nPort:{}".format(*data))
        else:
            print("[ERROR]")
        return data

    def accept(self):
        """
        self.PAGENT - <class type(dict)>
        self.PAGENT - [[port, hardware%, function%, price]...]
        :return:
        """
        waga = 1
        for x in range(len(self.PAGENT)):
            finalna_waga = float(self.PAGENT[x][1]) / 1000 + waga
            finalna_waga = finalna_waga + float(self.PAGENT[x][2]) / 1000
            #print(self.PAGENT[x])
            if float(self.PAGENT[x][3]) < float(self.pref_price*finalna_waga):
                return self.PAGENT[x][0]
            waga += 0.1
        return self.PAGENT[len(self.PAGENT)-1][0]

    def generateDictOrder(self, req_type: str):
        print(self.resources)
        return req_type+'|' + codecs.encode(pickle.dumps(self.resources), "base64").decode()

    def sendTo(self, host, port, requst):
        client = socket.socket
        try:
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
                client.connect((host, int(port)))
            except ConnectionError as socketConnectionError:
                print(socketConnectionError, " the host {} can not be reached".format(host))
                raise IOError
            client.send(bytearray(requst, encoding="unicode-escape"))
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
