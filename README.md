# DAPNETNotifier
Forward DAPNET messages to notification services

---

This Python script will poll the DAPNET API and forward any new DAPNET Messages you receive to the notification service of your choice (from the one listed below of course).

The original script this was based off of scraped the Pi-Star dashboard and forwarded any messages to APRS for notitfication as a message there. I modified the script to send it to services that could be used on a phone and instead of scraping the dashboard, it utilizes the DAPNET API.

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

[Click here to see the installation and setup steps](https://github.com/n8acl/DAPNETNotifier/blob/master/Installation-Setup.md). Then come back here. This is a bit of a long document, so read it all carefully.

---
## Contact
If you have questions, please feel free to reach out to me. You can reach me in one of the following ways:

- Discord: Ravendos
- Mastodon: @n8acl@mastodon.radio
- E-mail: n8acl@qsl.net

Or open an issue on Github. I will respond to it, and of course you, when I can. 

If you reach out to me and have an error, please include what error you are getting and what you were doing. I may also ask you to send me certain files to look at. Otherwise just reach out to me :).

---
## Credits

Thanks go to [Leroy, KD8BXP](https://github.com/kd8bxp) for pointing out a DAPNET API endpoint I missed in my research that would let me pull this data directly from there.

---

## Change Log

* 09/13/2022 - Updated Script to pull from the DAPNET API versus Scrapeing the Pi-Star Dashboard

* 05/30/2022 - Fixed some README.md spelling errors.

* 03/28/2022 - Inital Release
