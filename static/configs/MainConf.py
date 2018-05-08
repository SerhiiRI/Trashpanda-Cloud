import os
from os import environ as ENV

"""
               Configuration Standart  

Configuration file use "Snake case" syntax: cos_tam_jest
For dictionary standart of name is UPPERCASE.
  
Autor: Serhii Riznychuk 
"""

DATABASE = {
    'cloud': {
        'host': ENV['TRASHPANDA_HOST'],
        'user': ENV['TRASHPANDA_LOGIN'],
        'password': ENV['TRASHPANDA_PASSWD'],
        'database': "cloud",
    },
    'test_cloud': {
        'host': ENV['TRASHPANDA_HOST'],
        'user': ENV['TRASHPANDA_LOGIN'],
        'password': ENV['TRASHPANDA_PASSWD'],
        'database': "test_cloud"
    },
    'system_logs': {
        'host': ENV['TRASHPANDA_HOST'],
        'user': ENV['TRASHPANDA_LOGIN'],
        'password': ENV['TRASHPANDA_PASSWD'],
        'database': "system_logs",
    },
    'pipeline': {
        'host': ENV['TRASHPANDA_HOST'],
        'user': ENV['TRASHPANDA_LOGIN'],
        'password': ENV['TRASHPANDA_PASSWD'],
        'database': "pipeline",
    }
}

FILES = {
    'logs': {
        'server_file' : os.getcwd(),
        'system_path' : '/var/log/trashpanda/',
        'system_error_file': '/var/log/trashpanda/error.log',
        'system_alert_file': '/var/log/trashpanda/allert.log',
        'system_messg_file': '/var/log/trashpanda/message.log'
    }
}


DEPENDED_VALUES = {

}