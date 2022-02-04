from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from addons import heart_ad
from addons import stickers_All

from addons import efict_run_line

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
def type(_, msg, heart, addons=None):
    orig_text = msg.text.split(".heart ", maxsplit=1)[1]
    print(orig_text)
    # count = int(orig_text)
    tbp = ""  # to be printed
    heart = ''
    heart = addons.heart_ad.Heart(heart)
    # # heart =\
    #                 '🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥'+'\n' \
    #                 '🔥🔥🔥💓💓🔥🔥🔥💓💓🔥🔥🔥'+'\n' \
    #                 '🔥🔥💓💓💓💓🔥💓💓💓💓🔥🔥'+'\n' \
    #                 '🔥💓💓💓💓💓💓💓💓💓💓💓🔥'+'\n' \
    #                 '🔥💓💓💓💓💓💓💓💓💓💓💓🔥' + '\n' \
    #                 '🔥🔥💓💓💓💓💓💓💓💓💓🔥🔥' + '\n' \
    #                 '🔥🔥🔥💓💓💓💓💓💓💓🔥🔥🔥' + '\n'\
    #                 '🔥🔥🔥🔥💓💓💓💓💓🔥🔥🔥🔥' + '\n' \
    #                 '🔥🔥🔥🔥🔥💓💓💓🔥🔥🔥🔥🔥' + '\n'\
    #                 '🔥🔥🔥🔥🔥🔥💓🔥🔥🔥🔥🔥🔥' + '\n' \
    #                 '🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥' + '\n'
    #     #"💓💓"
    cnt_1 = 0
    text = ''
    line = 0
    while line < 143:
        try:
            if cnt_1 < 13:
                msg.edit(text + efict_run_line.Run_line())
                text = text + efict_run_line.Run_line()  # heart.split()[line]
                cnt_1 += 1
            else:
                cnt_1 = 0
                text = efict_run_line.Rename_text()
                msg.edit(text + '\n')
            sleep(0.05)
            cnt_1 += 1
            line += 1
        except FloodWait as e:
            sleep(e.x)
    try:
        msg.edit(heart)
        text = heart
    except FloodWait as e:
        sleep(e.x)


app.run()
