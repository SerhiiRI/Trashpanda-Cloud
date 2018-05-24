from os import environ as ENV
from subprocess import Popen, PIPE
from os import popen
serverpath = ENV['CLOUD_PROJECT_PATH']

def createProcess(*args):

    output = popen("python3 "+serverpath+"/admin.py "+" ".join(args), mode="r",).read()
    print(output)
