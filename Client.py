#!/usr/bin/python3
# from os import popen
# from static.tool.console.vt1000 import ForeGround as fg, BackGround as bg, FormatCode as cd
# import npyscreen
import static.configs.EnvConf
from static.classes.Pipeline.Agents.ClientAgent import Agent
import argparse
import random

client = {
    # Przy poprawnej realizacji wartość tego pola musi definiować
    # progama automatycznie, zależąć od tego, o jakiej specyfika-
    # cji wymagań agenta byla zrobiono. Tzn, zrozumienie proceśów
    # wykonwczych.
    # Np. jeżeli agent jest uzależniony węwnątrz od czasu, to wt-
    # edy musi sie wyliczyć odpowiednią wagę wychodzącą, obojętne
    # jaka ta waga będzie miala znaczenia.
    # W programie te wartośći wypelnia mega-inteligentna funkcja
    # random((range(0,101, 1)))
    "id": random.randint(0, 10000),
    "machine": {
        "cpu": 16,
        "disk": 10,
        "ram": 10,
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
"""
import os
os.system("clear")
z, b = os.popen("stty size", mode="r").read().split()
print("{:-^{x}}".format("MAIN", x=b))
print("{:^{x}}".format("Szukamy wirtualną maczyne:", x=b))
print("Obciążania procesora: \n(1)high\n(2)middle\n(3)low\n")
cpu = input(">")
client["machine"]["cpu"] = select[cpu]
print("Potrzebujesz zużycia dysku? \n(1)high\n(2)middle\n(3)low\n(4)Operacje wylącznie liczbowe\n")
cpu = input(">")
client["machine"]["disk"] = select[cpu]
print("Potrzebujesz zużycia pamięci operacyjnej?\n(1)high\n(2)middle\n(3)low\n(4)Operacje wylącznie liczbowe\n")
cpu = input(">")
client["machine"]["ram"] = select[cpu]
print("Niesty nie zdążylem napisać Input dla \nfunkcyj, to poprostu określi poszczególą \nilość operacyj dla każdej z funkcji\n")
print("(1-100) bądż grzecznym i nie\n pisz nic zpoza zakresu bo mi sie \nlieni robić na to obsluge")
client["function"]["factorial"] = int(input("Silnia:"))
client["function"]["bublesort"] = int(input("Sortowanie:"))
client["function"]["searching"] = int(input("Search:"))
print("Preferowana cena(200 zl max)")
cena = int(input(":"))

"""



parser = argparse.ArgumentParser(description="Create agent")
parser.add_argument("-i", '--ip', action="store", dest="host", help="choose HOST-address  agent")
parser.add_argument("-p", "--port", action="store", dest="ports", help="chose PORT-s to connect")
if __name__ == '__main__':
    args = parser.parse_args()
    if not vars(args):
        print("Zle parametry")
    else:
        ports = args.ports.split(",")
        client = Agent(client, 40)
        for port in ports:
            client.PAGENT.append(client.hand_shacking(target_host=args.host, target_port=int(port), type_hs="order"))
        client.hand_shacking(target_host=args.host, target_port=client.accept(), type_hs="accept")


"""

ten skrypt genteruje symulacje użytkowników 
dla systemy wieloagentowej. dla twożenia 
kolejek zadan na innych wirtualnych mazsyn-
ach, pod docker-systemem

"""
