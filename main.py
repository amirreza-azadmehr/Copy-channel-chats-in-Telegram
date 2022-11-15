from pyrogram import Client,filters
from telethon import TelegramClient, events
import re
from functools import reduce

api_id = 1 #enter your telegram api_id from telegram.org
api_hash ="1" # enter your telegram api_hash telegram.org
client = TelegramClient('session_name', api_id, api_hash)
client.start()

@client.on(events.NewMessage(chats= -1  )) #from channel chat_id or channel name STR into (-1)
async def my_event_handler(event):
    message=(event.raw_text)
    finally_text=re.sub('@test1','@test2',message) # if your channel1 have tag , you can replace with test2
    await client.send_message(-1  , finally_text) #to channel chat_id or channel name STR into (-1)

client.run_until_disconnected()    
