from random import choice
from addons.stickers_All import stickers_all as stick

def Run_line():
    add_text= choice(stick.All)

    return add_text
def Rename_text():
    s = ''
    for i in range(13):
        s += choice(stick.All)
    return s
print(Rename_text())