#! /usr/bin/env python3

import sys
import subprocess
from crontab import CronTab
from pathlib import Path

# constants
dependencies = ["requests",
 "PyYAML",
 "python-crontab",
 "pyspectator"]

# install module
def inst_mod(mod_name: str):
    subprocess.call(["pip3", "install", mod_name])

# check dependencies
for dep in dependencies:
  if dep not in sys.modules:
    inst_mod(dep)

my_path = str(Path.cwd().absolute())

my_cron = CronTab(user=True)
my_job = my_cron.new(command=my_path + '/hardware-check.py 2>> ' +
                     my_path + '/error', comment='hardwareCheck')
# my_job = my_cron.new(command='echo "Hello World!" >> ' + my_path + '/log', comment='test')
my_job.minute.every(10)
my_cron.write()
