#################################################################################

# DAPNET Notifier
# Developed by: Jeff Lehman, N8ACL
# Current Version: 09132022
# https://github.com/n8acl/DAPNETNotifier

# Questions? Comments? Suggestions? Contact me one of the following ways:
# E-mail: n8acl@qsl.net
# Twitter: @n8acl
# Discord: Ravendos#7364
# Mastodon: @n8acl@mastodon.radio
# Website: https://www.qsl.net/n8acl
# Blog: https://n8acl.github.io

###################   DO NOT CHANGE BELOW   #########################

#############################
##### Import Libraries
import config as cfg
import json
import re
import requests
import time
import http.client, urllib
import os
import sys
import sqlite3 as sql
from requests.auth import HTTPBasicAuth
from os import system, name
from time import sleep
from sqlite3 import Error

# libary only needed if Discord is configured in config.py
if cfg.discord:
    from discord_webhook import DiscordWebhook, DiscordEmbed

# libraries only needed if Telegram is configured in config.py
if cfg.telegram:
    import telegram

#############################
##### Define Variables
first_run = True
linefeed = "\r\n"
dapnet_url = 'http://www.hampager.de:8080/calls?ownerName=' + cfg.dapnet_username
database = os.path.dirname(os.path.abspath(__file__)) +  "/dapnet.db"

#############################
##### Define Functions

##### Define SQL Functions
def create_connection(db_file):
    # Creates connection to dapnet.db SQLlite3 Database
    conn = None
    try:
        conn = sql.connect(db_file)
    except Error as e:
        print(e)
    return conn

def exec_sql(conn,sql):
    # Executes SQL for Updates, inserts and deletes
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def select_sql(conn,sql):
    # Executes SQL for Selects
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

def new(conn):
# Create new database if not exists

    create_message_table = """ create table if not exists messages (
text text, 
timestamp text
); """

    exec_sql(conn, create_message_table)

    data = get_api_data()

    for i in range(0,len(data)):
        text = data[i]['text']
        timestamp = data[i]['timestamp']

        sql = "insert into messages (text, timestamp) "
        sql = sql + "values('" + text + "','" + timestamp + "');"

        exec_sql(conn, sql)


##### Get API Data
def get_api_data():
    return requests.get(dapnet_url, auth=HTTPBasicAuth(cfg.dapnet_username,cfg.dapnet_password)).json()

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

# check to see if the database exists. If not create it. Otherwise create a connection to it for the rest of the script
if not os.path.exists(database):
    conn = create_connection(database)
    new(conn)
else:
    conn = create_connection(database) 

# Check API and if the last message was not already sent, send it... else ignore it.
try:
    while True:
        if first_run: # If this is the first run, don't send anything
            first_run = False
        else:
            # Wait the check time to not pound the API and get rate Limited
            if cfg.wait_time < 60:
                sleep(60)
            else:
                sleep(cfg.wait_time) 

            # get the data from the API
            data = get_api_data()

            for i in range(0,len(data)):
                text = data[i]['text']
                timestamp = data[i]['timestamp']

                sql = "select count(text) as text_cnt from messages where text = '" + text + "' and timestamp = '" + timestamp + "';"
                result = select_sql(conn, sql)

                for row in result:
                    text_cnt = row[0]

                if text_cnt == 0:

                    sql = "insert into messages (text, timestamp) "
                    sql = sql + "values('" + text + "','" + timestamp + "');"

                    exec_sql(conn,sql)
                    
                    # Send the message 
                    if cfg.discord:
                        send_discord(text)
                    if cfg.telegram:
                        send_telegram(text)
                    if cfg.mattermost:
                        post_to_webhook({'text': text}, cfg.mattermost_wh)
                    if cfg.slack:
                        post_to_webhook({'text': text}, cfg.slack_wh)
                    if cfg.pushover:
                        send_pushover(text)

                    break

except Exception as e:
    print(str(e))
