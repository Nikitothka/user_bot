from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions

import time
from time import sleep
import random

app = Client("my_account")

'''@app.on_message(filters.text & filters.private)
def echo(client, message):
    message.reply(message.text)
    app.send_message("me", ":heart:")
'''

@app.on_message(filters.command("heart", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".heart ", maxsplit=1)[1]
    print(orig_text)
    #count = int(orig_text)
    tbp = ""  # to be printed

    typing_symbol = '🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥'+'\n' \
                    '🔥🔥🔥💓💓🔥🔥🔥💓💓🔥🔥🔥'+'\n' \
                    '🔥🔥💓💓💓💓🔥💓💓💓💓🔥🔥'+'\n' \
                    '🔥💓💓💓💓💓💓💓💓💓💓💓🔥'+'\n' \
                    '🔥💓💓💓💓💓💓💓💓💓💓💓🔥' + '\n' \
                    '🔥🔥💓💓💓💓💓💓💓💓💓🔥🔥' + '\n' \
                    '🔥🔥🔥💓💓💓💓💓💓💓🔥🔥🔥' + '\n'\
                    '🔥🔥🔥🔥💓💓💓💓💓🔥🔥🔥🔥' + '\n' \
                    '🔥🔥🔥🔥🔥💓💓💓🔥🔥🔥🔥🔥' + '\n'\
                    '🔥🔥🔥🔥🔥🔥💓🔥🔥🔥🔥🔥🔥' + '\n' \
                    '🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥' + '\n'
        #"💓💓"
    cnt_1 =0
    text = ''
    line = 0
    while line<10:
        try:
            #text =  #мэйн текс
            msg.edit(text + typing_symbol.split()[line])
            text = text + typing_symbol.split()[line]
            sleep(0.05)
            cnt_1 +=1
            line+=1
        except FloodWait as e:
            sleep(e.x)
    try:
        # text =  #мэйн текс
        msg.edit(typing_symbol)
        text = text + typing_symbol
    except FloodWait as e:
        sleep(e.x)




app.run()

