import configparser
import requests


# READ CONFIG FILE
config = configparser.ConfigParser()
config.read("logger.cfg")

bot_token = config["alarm_settings"]["bot_token"]
bot_chatID = config["alarm_settings"]["bot_chatID"]

class TelegramBot():

    def __init__(self):
        self.bot_token = bot_token
        self.bot_chatID = bot_chatID


    def sendAlert(self, textalert=None):
        send_text = 'https://api.telegram.org/bot' + self.bot_token + '/sendMessage?chat_id=' + self.bot_chatID + '&parse_mode=Markdown&text=' + '`' + textalert + '`'
        response = requests.get(send_text)
        return response.json()
