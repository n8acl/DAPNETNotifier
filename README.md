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
* 03/28/2022 - Release 03282022
  * Refined query to check destination channel versus the destination extension. When using a ring group, this helps to grab the missed call to the extension
  * Added the ability to check for and notify if a new voicemail has been left. Also lets the user know the number of voicemails sitting in the inbox for that extension. This is total number, not just new voicemails.

* 01/30/2022 - Release 01302022
  * Added more supported messaging services for notifications
  * Refined the SQL query that pulls the last call data
  * Refined the way the script parses the data for missed call
  * Added Installation steps document
  * Added startbot.sh as an example to allow for launch at startup.

* 01/29/2022 - Inital Release
