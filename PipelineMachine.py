#!/usr/bin/python3
import static.configs.EnvConf

from static.classes.Pipeline.dictionary.agent import agent
from static.classes.Pipeline.Agents.PipeAgent import Agent
import argparse

parser = argparse.ArgumentParser(description="Create PipeLine-agent")
parser.add_argument("-i", '--ip', action="store", dest="host", default='0.0.0.0', help="choose HOST-address to your agent")
parser.add_argument("-p", "--port", action="store", dest="port", default=9999, type=int, help="chose PORT to you ")

if __name__ == '__main__':
    args = parser.parse_args()
    if not vars(args):
        print("Zle parametry")
    else:
        ServerAgent = Agent(agent, host=args.host, port=args.port)
        ServerAgent.listening()
