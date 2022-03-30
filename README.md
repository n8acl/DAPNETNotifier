# DAPNETNotifier
Forward DAPNET messages to notification services

---

###### Forked from [KR0SIV/DAPNET2APRS](https://github.com/KR0SIV/DAPNET2APRS) and modified.

This Python script will scrape your PI-Star Dashboard and forward any new DAPNET Messages you the nofication service of your choice (from the one listed below of course).

The original script scraped the dashboard and forwarded any messages to APRS for notitfication as a message there. I modified the script to send it to services that could be used on a phone.

This script does require you to have a Pi-Star Hotspot/repeater setup and configured as a transmitter for DAPNET. Otherwise there is nothing to scrape. Future versions will hopefully use the DAPNET API to pull calls from. This should NOT be run on your hotpost, but can be run on a Linux Server or a Raspberry Pi.

---

## Supported Services

This script will push a notification to the following services:

- Discord
- Telegram
- Slack
- Mattermost
- Pushover

---

## Installation/Setup Instructions

[Click here to see the installation and setup steps](https://github.com/n8acl/freepbx_call_monitor/blob/main/Installation-Setup.md). Then come back here. This is a bit of a long document, so read it all carefully.

---
## Contact
If you have questions, please feel free to reach out to me. You can reach me in one of the following ways:

- Twitter: @n8acl
- Discord: Ravendos#7364
- Mastodon: @n8acl@mastodon.radio
- E-mail: n8acl@qsl.net

Or open an issue on Github. I will respond to it, and of course you, when I can. 

If you reach out to me and have an error, please include what error you are getting and what you were doing. I may also ask you to send me certain files to look at. Otherwise just reach out to me :).

---

## Change Log
* 03/28/2022 - Inital Release
