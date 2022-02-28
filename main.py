from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from scrips_for_main.log_pr import Log
import addons.heart_ad

from time import sleep
import random

app = Client("my_account")

@app.on_message(filters.private & ~filters.me & filters.text)
async def bot(client, message):
    count = 0
    if str(message.chat.id) == '1149270898':
        try:

            if count < 1:
                Log(message)
                count += 1
                string_const = message.text
            else:
                pass
        except UnicodeEncodeError:
            print(UnicodeEncodeError)
    else:
        print(message.chat.id)
        print(message.date,message.chat.first_name, ':', message.text)
    # await message.reply(message.text)

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
    cnt_1 = 0
    text = ''
    line = 0
    cnt_string = 0

    while count < 20:

        try:
            sleep(0.1)
            msg.edit(addons.heart_ad.Heart(heart))
            sleep(0.5)
        except FloodWait as e:
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
