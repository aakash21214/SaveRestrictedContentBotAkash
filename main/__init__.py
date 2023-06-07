#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", 12916125, cast=int)
API_HASH = config("API_HASH", "dfebf9cc52b859771cf8a1d447e751a5")
BOT_TOKEN = config("BOT_TOKEN", "5785101195:AAHbWMBDku6q9tWJdMIJtJvhEl3ajmC0spQ")
SESSION = config("SESSION", "BQCu4-U3pkQyeTpFy8uiGjMgwmlTOFKF8_f7XpwMjSC3pVBvGqk8Uo6L3HqIZJ7yFb1dUOrZ7-bSKjWWG_pciwHliG6HgQbE3Gwhfz-cN9lceKuQ9NHAecdVoAciniV75jPSUCJdXpHEkH7jVMoCYoL_yu87Xv7vWV0713CETERaSQ2m7ewaOb0JYmX19riKX0n5djmoqg-wqtV_gVfvytzow91KFzNCCbzojOOloNK-QZYxisln1vQsd40q7nuGfG-U8syOr3TW5ifU8l1I_xv4977wkF0k8oGMxMqXYXRTFo0aCqsJ1xstB0yeKr6QxkNFOkNSfDqwXcWvQ7vtmOocYnOlYQA")
FORCESUB = config("FORCESUB", "erensupportgroup")
AUTH = config("AUTH", 1651746145, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
