from random import choice
from addons.stickers_All import stickers_all as stick

# A = ['😀', '🖤', '💩', '❤', '💘', '💗', '💖', '💙', '💚', '🧡', '💛', '💜', '⚪', '💝', '🎲', '💧']
# Stikers_bg = ['😀', '⚪', '🎲', '💧']
# Stickers_heart = ['🖤', '❤', '💘', '💗', '💖', '💙', '💚', '🧡', '💛', '💜', '💝']
# def Stickers_mas(stick_all.All:
def Heart(heart):
    stickers_heart = choice(stick.Stickers_heart)
    stickers_bg = choice(stick.Stickers_bg)
    for i in range(13):  # bg '🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥'
        heart += stickers_bg
    heart += '\n'       # 1end
    for i in range(3):  # 2_start bg '🔥🔥🔥💓💓🔥🔥🔥💓💓🔥🔥🔥'
        heart += stickers_bg
    for i in range(2):
        heart += stickers_heart
    for i in range(3):  # bg
        heart += stickers_bg
    for i in range(2):
        heart += stickers_heart
    for i in range(3):  # bg
        heart += stickers_bg
    heart += '\n'  # 2 end

    for i in range(2):  # 3_start bg
        heart += stickers_bg  # '🔥🔥💓💓💓💓🔥💓💓💓💓🔥🔥'
    for i in range(4):
        heart += stickers_heart
    for i in range(1):  # bg
        heart += stickers_bg
    for i in range(4):
        heart += stickers_heart
    for i in range(2):  # bg
        heart += stickers_bg
    heart += '\n'  # 3 end

    for i in range(1):  # 4_start bg
        heart += stickers_bg  # 🔥💓💓💓💓💓💓💓💓💓💓💓🔥
    for i in range(11):
        heart += stickers_heart
    for i in range(1):  # bg
        heart += stickers_bg
    heart += '\n'  # 4 end

    #-----------------------------------------
    for i in range(13):  # 5_start bg
        heart += stickers_bg  # 🔥💓💓💓💓💓💓💓💓💓💓💓🔥
    heart += '\n'  # 5 end
    for i in range(13):  # 6_start bg
        heart += stickers_bg  # 🔥💓💓💓💓💓💓💓💓💓💓💓🔥
    heart += '\n'  # 5 end
    for i in range(13):  # 7_start bg
        heart += stickers_bg  # 🔥💓💓💓💓💓💓💓💓💓💓💓🔥
    heart += '\n'  # 5 end
    for i in range(13):  # 8_start bg
        heart += stickers_bg  # 🔥💓💓💓💓💓💓💓💓💓💓💓🔥
    heart += '\n'  # 5 end
    for i in range(13):  # 9_start bg
        heart += stickers_bg  # 🔥💓💓💓💓💓💓💓💓💓💓💓🔥
    heart += '\n'  # 5 end
    for i in range(13):  # 10_start bg
        heart += stickers_bg  # 🔥💓💓💓💓💓💓💓💓💓💓💓🔥
    heart += '\n'  # 5 end

    #print(heart)
    return heart
heart = ''
Heart(heart)
#
# typing_symbol = '🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥'+'\n' \
#                   '🔥🔥🔥💓💓🔥🔥🔥💓💓🔥🔥🔥'+'\n' \
#                   '🔥🔥💓💓💓💓🔥💓💓💓💓🔥🔥'+'\n' \3
#                   '🔥💓💓💓💓💓💓💓💓💓💓💓🔥'+'\n' \4
#                   '🔥💓💓💓💓💓💓💓💓💓💓💓🔥' + '\n' \5
#                   '🔥🔥💓💓💓💓💓💓💓💓💓🔥🔥' + '\n' \6
#                   '🔥🔥🔥💓💓💓💓💓💓💓🔥🔥🔥' + '\n'\
#                   '🔥🔥🔥🔥💓💓💓💓💓🔥🔥🔥🔥' + '\n' \
#                   '🔥🔥🔥🔥🔥💓💓💓🔥🔥🔥🔥🔥' + '\n'\
#                   '🔥🔥🔥🔥🔥🔥💓🔥🔥🔥🔥🔥🔥' + '\n' \
#                   '🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥' + '\n
