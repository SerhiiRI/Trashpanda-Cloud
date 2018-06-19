#!/usr/bin/python3
# from os import popen
# from static.tool.console.vt1000 import ForeGround as fg, BackGround as bg, FormatCode as cd
# import npyscreen
import static.configs.EnvConf
from static.classes.Pipeline.Agents.ClientAgent import Agent
import argparse
from multiprocessing import Queue
import random
import os
import copy
clientD = {
    # Przy poprawnej realizacji wartość tego pola musi definiować
    # progama automatycznie, zależąć od tego, o jakiej specyfika-
    # cji wymagań agenta byla zrobiono. Tzn, zrozumienie proceśów
    # wykonwczych.
    # Np. jeżeli agent jest uzależniony węwnątrz od czasu, to wt-
    # edy musi sie wyliczyć odpowiednią wagę wychodzącą, obojętne
    # jaka ta waga będzie miala znaczenia.
    # W programie te wartośći wypelnia mega-inteligentna funkcja
    # random((range(0,101, 1)))
    "id": 0,
    "machine": {
        "cpu": 75,
        "disk": 99,
        "ram": 50,
    },
    "function": {
        "factorial": 2,
        "bublesort": 3,
        "searching": 4
    },
}
select = {
    "1": 80,
    "2": 50,
    "3": 25,
    "4": 1
}
cena = 123

def inp(fun):
    print("Podaj ilość wykonywanych funkcyj {}(1-100)".format(fun))
    x = 0
    try:
        x = int(input("> "))
    except:
        x = -1
    while x == -1 or x > 100 or x < 1:
        print("blad!")
        x =int(input("> "))
    return x

import os
os.system("clear")
z, b = os.popen("stty size", mode="r").read().split()
print("{:-^{x}}".format("MAIN", x=b))
print("{:^{x}}".format("Szukamy wirtualną maczyne:", x=b))
print("(1-100) bądż grzecznym i nie\n pisz nic zpoza zakresu bo mi sie \nlieni robić na to obsluge")
clientD["function"]["factorial"] = inp("silni")
clientD["function"]["bublesort"] = inp("sortownaia")
clientD["function"]["searching"] = inp("Wyszukiwania")
cena = 30
import sys
from static.classes.Pipeline.Threading import ThreadWithReturnValue

parser = argparse.ArgumentParser(description="Create agent")
parser.add_argument("-i", '--ip', action="store", dest="host", help="choose HOST-address  agent")
parser.add_argument("-p", "--port", action="store", dest="ports", help="chose PORT-s to connect")
parser.add_argument("-m", "--money", action="store", dest="money", default=50, type=int, help="Money to Client Agent")
parser.add_argument("-c", "--count-agent", action="store", dest="count", default=1, type=int, help="Count client agents")
if __name__ == '__main__':
    args = parser.parse_args()
    if not vars(args):
        print("Zle parametry")
    else:
        ports = args.ports.split(",")

        switch = dict()
        clients = list()
        threads = list()
        for count in range(args.count):
            clients.append(Agent(copy.deepcopy(clientD), cena, args.host, ports))

        for count in range(args.count):
            threads.append(ThreadWithReturnValue(target=clients[count].run))

        for count in range(args.count):
            threads[count].start()
        for count in range(args.count):
            switch[count] = threads[count].join()
        os.system("clear")
        #print(switch)
        print("Prosze wybierz Wirtualną maszyne do wykonywania polecenia:")
        print("----------------------------------------------------------")
        it = 0
        for key, data in switch.items():

            it += 1
            print(">{key:2}| {host}:{port}, in price{price} time: {time}".format(key=str(it), host=data[0], port=data[1], price=data[2], time=data[3]))
        print("----------------------------------------------------------")
        selected = int(input("Wybierz WM>").strip())
        while selected not in switch.keys():
            selected = int(input("Wybierz WM>").strip())
        print("Koniec")
        clients[selected].hand_shacking(target_host=switch[selected][0], target_port=switch[selected][1], type_hs="accept")



"""

ten skrypt genteruje symulacje użytkowników 
dla systemy wieloagentowej. dla twożenia 
kolejek zadan na innych wirtualnych mazsyn-
ach, pod docker-systemem

"""
