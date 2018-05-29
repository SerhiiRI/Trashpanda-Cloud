from static.classes.Pipeline.dictionary.agent import agent as clientSet
import socket
import random
import pickle
import codecs


class Agent:

    def __init__(self):
        """
        Creating ID to client, and wainting for love... waiting for love... tu-tu-tu
        :var ClientID
        """
        self.ClientID = str(random.randint(0, 100))
        self.resources = clientSet["machine"]
        self.count_of_function = ( "factorial", str(random.randint(0, 5000)) )

    def hand_shacking(self, target_host: str="0.0.0.0", target_port: int=9999):
        host = target_host
        port = target_port
        #request = 'info|Hello, i am client with id [{:^4}]'.format(self.ClientID)
        #request = bytearray(request, encoding="unicode-escape")

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        request = 'machine|'+codecs.encode(pickle.dumps(self.resources), "base64").decode()
        client.send(bytearray(str(request), encoding="unicode-escape"))
        response = client.recv(4096)
        print("[+] Otrzymane parametry: {}".format(str(response, encoding="utf-8")))
        client.close()

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        request = 'order|' + codecs.encode(pickle.dumps(self.count_of_function), "base64").decode()
        client.send(bytearray(str(request), encoding="unicode-escape"))
        response = client.recv(4096)
        print("[+] Otrzymane parametry: {}".format(str(response, encoding="utf-8")))
        client.close()


        if(input("decyzja o przeslaniu ceny (y/n) ?") == 'n'):
            return