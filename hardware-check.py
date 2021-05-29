#! /usr/bin/env python3
#
# Authors: Severin Hasler, Melvin Tas, Jonas Tochtermann
# (c) 2021

from pathlib import Path
from datetime import datetime
import os.path
import requests
import yaml
import json
from pyspectator.processor import Cpu
from crontab import CronTab
import sys

# constants
CONFIG_FILE = 'config.yaml'
MAX_CPU_TEMP = 'maxCpuTemp'
CHECK_INTERVAL = 'checkInterval'
TELEGRAM_CHAT = 'telegramChatID'
TELEGRAM_API = 'telegramApiUrl'
TELEGRAM_TOKEN = 'telegramToken'

# initialize main variables
maxCpuTemp = None
checkInterval = None
telegramChatID = None
telegramToken = None
time = str(datetime.now())
log = {}
warnings = []
warningMessage = ''
codePath = str(Path(__file__).parent.absolute()) + '/'

if os.path.isfile(codePath + CONFIG_FILE):
    # read config file
    try:
        with open(codePath + CONFIG_FILE, 'r') as yamlFile:
            config = yaml.load(yamlFile, Loader=yaml.CLoader)
        if MAX_CPU_TEMP in config:
            maxCpuTemp = config[MAX_CPU_TEMP]
        if CHECK_INTERVAL in config:
            checkInterval = config[CHECK_INTERVAL]
        if TELEGRAM_CHAT in config:
            telegramChatID = config[TELEGRAM_CHAT]
        if TELEGRAM_TOKEN in config:
            telegramToken = config[TELEGRAM_TOKEN]
    except BaseException as err:
        print('Error:', err)
else:
    sys.exit('config file missing')

# In case something went wrong, assign default values
if maxCpuTemp == None or isinstance(maxCpuTemp, float) != True:
    maxCpuTemp = 80.0
if checkInterval == None or isinstance(checkInterval, int) != True:
    checkInterval = 10

# In case something telegrammy is missing, abort: Programm is not runnable
if telegramChatID == None or isinstance(telegramChatID, str) != True or \
    telegramToken == None or isinstance(telegramToken, str) != True:
        sys.exit('telegram config missing')

# update cronjob, if the user has changed interval time
myCron = CronTab(user=True)
intTime = '*/' + str(checkInterval)
for job in myCron:
    if job.comment == 'hardwareCheck' and str(job.minute) != intTime:
        job.minute.every(checkInterval)
        myCron.write()

# read cpu-temperature
cpu = Cpu(monitoring_latency=1)
temperature = cpu.temperature
log['cpu-temp'] = temperature

# check if cpu-temperature exceeds max
if temperature > maxCpuTemp:
    warnings.append('Temperature is too high: ' + \
        str(temperature) + ' (max: ' + str(maxCpuTemp) + ')')

# save data to logfile
try:
    with open(codePath + 'log.json', 'r+') as logFile:
        data = json.load(logFile)
        data.update({time: log})
        logFile.seek(0)
        json.dump(data, logFile, indent=2, ensure_ascii=False)
except BaseException as err:
    print('Error:', err)

# write telegram message
if len(warnings) > 0:
    warnings.insert(0, 'Your Computer has occurred a problem:')
    warningMessage = '\n'.join(warnings)
    send_text = 'https://api.telegram.org/' + telegramToken + \
        '/sendMessage?chat_id=' + telegramChatID + \
        '&parse_mode=Markdown&text=' + warningMessage
    try:
        response = requests.get(send_text)
    except requests.exceptions as err:
        print('Error:', err)
