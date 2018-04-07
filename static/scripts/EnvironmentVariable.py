#!/usr/bin/python3

# ******************************
# ******************************
# **                          **
# **    ENV variable init.    **
# **                          **
# ******************************
# ******************************

from os import environ as ENV

ENV['CLOUD_MAX_FILE_SIZE'] = '5GB'
ENV['CLOUD_DOWNLOAND_DATA_PATH'] = '/usr/'
ENV['CLOUD_DOWNLOAND_DAMP'] = '/home/Download/temp'
ENV['CLOUD_PROJECT_PATH'] = os.getcwd()
