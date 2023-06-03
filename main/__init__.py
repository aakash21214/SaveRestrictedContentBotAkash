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
BOT_TOKEN = config("BOT_TOKEN", "6014164542:AAGtFkU03BHqkjLPbiFj3rJMlByQqmdiHpA")
SESSION = config("SESSION", "BQA9AmKadvRIRyIFeL4WTOHbFgphUM0J8I2PBmXvzLfvCFwZc28-cBGBHAvK5KIrLmZK0TU76wMS_652N3W2pcNZ_Ukjyy5BROcQZgPd5ieakbgDIMdja5FVx42XdrrMtsJpTCgk5urn04aSxReAVenWw0jpMJMWbRXdZEWNQ0xVc4y2ewHIMJmSY5wcEFlHnNs2atoAt1UDf7VzIiAtvFE50xsEDIRLVtbK1DXbjqvLv-rIq_OCGDLsBHo4C525W7IruS-zO-jG-LzLGKRbhVFEaNAse5FkVKnQo8Bo9vEWqBA8R6vPdcjdcjQEqpeQZfODBY2lM0i8RzCyjBg1lymJYnOlYQA")
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
