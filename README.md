# hardware-check

Ein Python-Tool zur Überwachung von Hardware auf entfernten Computern (z.B. RaspberryPi).
Bislang funktioniert es leider nur auf Linux-PCs.

## Voraussetzungen

Folgende zusätzlichen Python-Module müssen installiert werden (mit `pip3 install ...`):

* pyspectator (CPU-Temperatur)
* PyYAML (für das config-file)
* python-crontab (für den Cronjob)
* requests (HTTPS Calls for Telegram API)

### Installation

Mit `python3 install.py` wird ein Cronjob für den lokalen User installiert, der gemäss Voreinstellungen
alle 10 Minuten das Skript `hardware-check.py` laufen lässt.

### Konfiguration

In der Konfigurationsdatei `config.yaml` lassen sich folgende Parameter festlegen:

* maxCpuTemp: Ab welcher CPU-Temperatur die Warnung gesendet werden soll (Dezimalzahl!)
* checkInterval: Wie regelmässig der Test laufen soll (in Minuten)
* telegramChatID: In welchen Telegramkanal die Warnung gesendet werden soll
* telegramApiUrl: Die Webseite der Telegram-API (sollte sich eigentlich nicht ändern...)
* telegramToken: Der Telegram-API-Token für den Bot (**inklusive 'bot' am Anfang!**)

Die Anleitung zur  Erstellung eines Telegram-Bots kann auf
[dieser Seite](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e)
nachgelesen werden.
