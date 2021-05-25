import requests

def get_emoji(emojiName):
    emoji = ""
    
    if emojiName == "grinning":
        emoji = '\U0001F601'
    if emojiName == "hot":
        emoji = '\U0001F525'
    if emojiName == "cold":
        emoji = '\U0001F976'                                 
    if emojiName == "sunglasses":
        emoji = '\U0001F60E'    
    
    return emoji

def telegram_bot_sendtext(bot_message):
    
    bot_token = '1842158365:AAGWo3CqoVYYTBRN7uETQ8axicrgSF4ipFU'
    bot_chatID = '-559789286'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

test = telegram_bot_sendtext("Testing Telegram Bot " + get_emoji("grinning") + get_emoji("hot") + get_emoji("cold") + get_emoji("sunglasses"))
print(test)