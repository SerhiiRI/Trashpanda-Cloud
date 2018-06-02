from static.classes.Pipeline.dictionary.agent import agent as clientSet
from static.classes.Pipeline.dictionary.ValueConfigurations import constant_values as comparator
from static.classes.Pipeline.PipeBuilder import PipeBuilder
from static.classes.Pipeline.Controller import ControllerServer
import time
import argparse
from static.classes.Pipeline.AvailableFunctions.FunctionList import factorial
from static.classes.Pipeline.Agents.PipeAgent import Agent
from static.classes.Pipeline.dictionary.agent import agent
from multiprocessing import Queue
from threading import current_thread
import socket
import random
import pickle
import codecs


class Agent:

    def __init__(self, price : int = 100):
        """
        Creating ID to client, and wainting for love... waiting for love... tu-tu-tu
        :var ClientID
        """
        self.critical_price = 100
        self.pref_price = price
        self.ClientID = str(random.randint(0, 100))
        self.resources = clientSet
        self.count_of_function = ( "factorial", str(random.randint(0, 5000)) )
        self.PAGENT = list()

    def hand_shacking(self, type_hs, target_port: int, target_host: str="0.0.0.0"):
        host = target_host
        port = target_port
        data = self.sendTo(host, port, self.generateDictOrder(type_hs)).split("|")
        print(data)
        return data

    def accept(self):
        vaga= 1
        for x in range(len(self.PAGENT) - 1):
            vaga +=0.1
            print(self.PAGENT[x])
            if(float(self.PAGENT[x][3]) < self.pref_price):
                return self.PAGENT[x][0]
        return self.PAGENT[len(self.PAGENT)-1][0]

    def generateDictOrder(self, req_type:str):
        return req_type+'|' + codecs.encode(pickle.dumps(self.resources), "base64").decode()

    def sendTo(self, host, port, requst):
        client = socket.socket
        try:
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect((host, int(port)))
            except ConnectionError as socketConnectionError:
                print(socketConnectionError, " the host {} can not be reached".format(host))
                raise IOError
            print(requst)
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
