#!/usr/bin/python3

# ******************************
# ******************************
# **                          **
# **    ENV variable init.    **
# **                          **
# ******************************
# ******************************
import os
from os import environ as ENV

ENV['CLOUD_MAX_FILE_SIZE'] = '5GB'
ENV['CLOUD_DOWNLOAND_DAMP'] = '/home/Download/temp/'
ENV['CLOUD_PROJECT_PATH'] = os.getcwd()
ENV['CLOUD_USERSPACE'] = '/srv/users/'
