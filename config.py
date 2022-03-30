##### Main Variables
mmdvm_ip = 'FQDN or full IP Address for pi-star hotspot' # EX: http://pistar.local or http://10.0.0.100
wait_time = 60 #Your delay in seconds between message checks, let's not hammer the crap out of the MMDVM hum?

##### Notification Services Variables
# Pushover configuration
pushover = False # Enable or disable notifications via Pushover
pushover_token = "1234567890" # Your Pushover API token
pushover_user = "abcdefghijklm" # Your Pushover user key

# Configure Telegram
telegram = False # Enable. On = True, Off = False
telgram_bot_token = 'YOUR TELEGRAM BOT TOKEN HERE'
telegram_chat_id = 'YOUR TELEGRAM CHAT ID HERE'

# Configure Mattermost
mattermost = False # Enable. On = True, Off = False
mattermost_wh = 'YOUR MATTERMOST WEBHOOK URL HERE'

# Configure Slack
slack = False # Enable. On = True, Off = False
slack_wh = 'YOUR SLACK WEBHOOK URL HERE'

# Discord Configuration
discord = False # Enable. On = True, Off = False
discord_wh = 'DISCORD CHANNEL WEBHOOK HERE'