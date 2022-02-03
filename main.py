from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions

import time
from time import sleep
import random

app = Client("my_account")

async def main():
    await app.start()
    await app.send_message("me", "Hi!")
    await app.stop(

app.run()