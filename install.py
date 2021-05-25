#! /usr/bin/env python3

from crontab import CronTab
from pathlib import Path

my_path = str(Path.cwd().absolute())

my_cron = CronTab(user=True)
my_job = my_cron.new(command='python ' + my_path + '/hardware-check.py', comment='hardwareCheck')
# my_job = my_cron.new(command='echo "Hello World!" >> ' + my_path + '/log', comment='test')
my_job.minute.every(10)
my_cron.write()