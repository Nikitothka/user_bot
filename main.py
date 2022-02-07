from pyrogram import Client, filters
from pyrogram.errors import FloodWait

import addons.heart_ad

from addons import efict_run_line

from pyrogram.types import ChatPermissions

from scrips_for_main.replase import Rep

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
    try:
        orig_text = msg.text.split(".heart ", maxsplit=1)[1]
    except:
        orig_text = 1
    print(orig_text)
    heart_bool = True
    # count = int(orig_text)
    tbp = ""  # to be printed
    heart = ''
    count= 0
    #heart = addons.heart_ad.Heart(heart)
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
    cnt_string = 0
    # while cnt_string < 3:
    #     try:
    #         if cnt_1 < 3:
    #             msg.edit(text + efict_run_line.Run_line())
    #             text = text + efict_run_line.Run_line()  # heart.split()[line]
    #             cnt_1 += 1
    #         else:
    #             #text_end = ''
    #             cnt_1 = 0
    #             cnt_string +=1
    #             text = Rep(cnt_string)
    #             #text_end += text
    #             msg.edit(text + '\n')
    #
    #         sleep(0.5)
    #         cnt_1 += 1
    #         line += 1
    #     except FloodWait as e:
    #         print(e.x)
    #         sleep(e.x)
    # print(heart_bool)
    while count < 20:

        try:
            sleep(0.1)
            msg.edit(addons.heart_ad.Heart(heart))
            sleep(0.5)
        except FloodWait as e:
            print(e.x)
            sleep(e.x)
        count +=1
        print(count)
@app.on_message(filters.command("stop", prefixes=".") & filters.me)
def types(_, msg):
    msg.edit('💩')
    try:
        print('False')
        heart_bool = False
        return heart_bool
    except:
        print(heart_bool)


if __name__ == '__main__':
    type
    types
    app.run()
