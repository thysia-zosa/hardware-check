# hardware-check

Ein Python-Tool zur Überwachung von Hardware auf entfernten Computern (z.B. RaspberryPi).

## Voraussetzungen

Python-Module:

* pyspectator (CPU-Temperatur)
* pyyaml (für das config-file)
* python-crontab (für den Cronjob)
* requests (HTTPS Calls for Telegram API)

für Mac notwendig (zusätzliches Programm, kein Python-Modul): 

* osx-cpu-temp (https://github.com/lavoiesl/osx-cpu-temp.git)
