#! /usr/bin/env python3
#
# Authors: Severin Hasler, Melvin Tas, Jonas Tochtermann
# ©2021

from datetime import datetime
import os.path
import psutil
import yaml

CONFIG_FILE = 'config.yaml'
MAX_CPU_TEMP = 'maxCpuTemp'
CHECK_INTERVAL = 'checkInterval'
TELEGRAM_ADDRESS = 'telegramAddress'

# start log entry with time, prepare error list
log = [datetime.now()]
errors = []

if os.path.isfile(CONFIG_FILE):
    # read config file
    with open(CONFIG_FILE, 'r') as yamlFile:
        config = yaml.load(yamlFile, Loader=yaml.CLoader)
    if MAX_CPU_TEMP in config:
        maxCpuTemp = config[MAX_CPU_TEMP]
    if CHECK_INTERVAL in config:
        checkInterval = config[CHECK_INTERVAL]
    if TELEGRAM_ADDRESS in config:
        telegramAddress = config[TELEGRAM_ADDRESS]

# In case something went wrong, assign default values
if maxCpuTemp == None:
    maxCpuTemp = 90.0
if checkInterval == None:
    checkInterval = 10
if telegramAddress == None:
    telegramAddress = 'M122'

# install / update cronjob
# TODO: implement (see https://code.tutsplus.com/tutorials/managing-cron-jobs-using-python--cms-28231)

# read cpu-temperature
sensor = psutil.sensors_temperatures()
temperature = next(iter(sensor.values()))[0][1]
log.append('cpu-temp: ' + temperature)

# check if cpu-temperature exceeds max
if temperature > maxCpuTemp:
    warning = True
    errors.append('Temperature is too high: ' + temperature + ' (max: ' + maxCpuTemp + ')')

# save data to logfile
# TODO: implement (@Melvin?)

# write telegram message
# TODO: implement (@Severin?)