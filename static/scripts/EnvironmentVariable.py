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

ENV['CLOUD_MAX_FILE_SIZE'] = '1MB'
ENV['CLOUD_DOWNLOAND_DAMP'] = '/srv/Dump/'
ENV['CLOUD_PROJECT_PATH'] = os.getcwd()
ENV['CLOUD_TRASHBOX'] = '/srv/Data/'
