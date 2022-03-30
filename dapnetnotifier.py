#############################
##### Import Libraries
import config as cfg
import re
import requests
import time
import http.client, urllib
from time import sleep

# libary only needed if Discord is configured in config.py
if cfg.discord:
    from discord_webhook import DiscordWebhook, DiscordEmbed

# libraries only needed if Telegram is configured in config.py
if cfg.telegram:
    import telegram

#############################
##### Define Variables
value = ''
first_run = True

#############################
##### Define Functions

def checkMSG():

    r = requests.get(cfg.mmdvm_ip)

    strip1 = re.findall("!important;.>\w{4,9}:\s[\w\s]{2,69}", str(r.content))
    try:
        message_content = re.sub('!important;.>', '', str(strip1[0]))
        return message_content
    except:
        return 'Error'


##### Define Service Functions
def send_discord(msg):
    webhook = DiscordWebhook(url=cfg.discord_wh)

    embed = DiscordEmbed(title="New DAPNET Message", description=msg)
    webhook.add_embed(embed)

    response = webhook.execute() 

def send_pushover(msg):
    connn = http.client.HTTPSConnection("api.pushover.net:443")
    connn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
        "token": cfg.pushover_token,
        "user": cfg.pushover_userkey,
        "message": msg,
        }), { "Content-type": "application/x-www-form-urlencoded" })
    connn.getresponse()

def post_to_webhook(msg, wh_url):
    # used for Slack and Mattermost
    response = requests.post(
        wh_url, data=json.dumps(msg),
        headers={'Content-Type': 'application/json'}
    )

def send_telegram(msg):
    bot = telegram.Bot(token=cfg.telegram_bot_token)
    bot.sendMessage(chat_id=cfg.telegram_chat_id, text=msg)


#############################
##### Main Program

try:
    while True:
        if first_run:
            first_run = False
            old_value = checkMSG()

        else:
            sleep(cfg.wait_time)

            old_value, value = value, checkMSG()
            
            if value != 'Error':
                if value != old_value:
                    if cfg.discord:
                        send_discord(value)
                    if cfg.telegram:
                        send_telegram(value)
                    if cfg.mattermost:
                        post_to_webhook({'text': value}, cfg.mattermost_wh)
                    if cfg.slack:
                        post_to_webhook({'text': value}, cfg.slack_wh)
                    if cfg.pushover:
                        send_pushover(value)

except Exception as e:
    print(str(e))
