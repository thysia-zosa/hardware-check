#! /usr/bin/env python3
#
# Authors: Severin Hasler, Melvin Tas, Jonas Tochtermann
# ©2021

from datetime import datetime
import os.path
import requests
import yaml
from pyspectator.processor import Cpu
from crontab import CronTab

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
log = [datetime.now()]
errors = []
warningMessage = ''

if os.path.isfile(CONFIG_FILE):
    # read config file
    with open(CONFIG_FILE, 'r') as yamlFile:
        config = yaml.load(yamlFile, Loader=yaml.CLoader)
    if MAX_CPU_TEMP in config:
        maxCpuTemp = config[MAX_CPU_TEMP]
    if CHECK_INTERVAL in config:
        checkInterval = config[CHECK_INTERVAL]
    if TELEGRAM_CHAT in config:
        telegramChatID = config[TELEGRAM_CHAT]
    if TELEGRAM_TOKEN in config:
        telegramToken = config[TELEGRAM_TOKEN]

# In case something went wrong, assign default values
if maxCpuTemp == None or isinstance(maxCpuTemp, float) != True:
    maxCpuTemp = 80.0
if checkInterval == None or isinstance(checkInterval, int) != True:
    checkInterval = 10
# TODO: if one of the folowing is amiss, abort with error message 'ChatID/Token not provided'
if telegramChatID == None or isinstance(telegramChatID, str) != True:
    telegramChatID = '-559789286'
if telegramToken == None or isinstance(telegramToken, str) != True:
    telegramToken = 'bot1842158365:AAGWo3CqoVYYTBRN7uETQ8axicrgSF4ipFU'

# update cronjob
myCron = CronTab(user=True)
for job in myCron:
    if job.comment == 'hardwareCheck' and str(job.minute) != ('*/' + str(checkInterval)):
        job.minute.every(checkInterval)

# read cpu-temperature
cpu = Cpu(monitoring_latency=1)
temperature = cpu.temperature
log.append('cpu-temp: ' + temperature)

# check if cpu-temperature exceeds max
if temperature > maxCpuTemp:
    errors.append('Temperature is too high: ' + temperature + ' (max: ' + maxCpuTemp + ')')

# save data to logfile
# TODO: implement (@Melvin?)

# write telegram message
if len(errors) > 0:
    send_text = 'https://api.telegram.org/' + telegramToken + \
        '/sendMessage?chat_id=' + telegramChatID + \
        '&parse_mode=Markdown&text=' + warningMessage
    response = requests.get(send_text)
