from random import choice
from addons.stickers_All import stickers_all as stick

# A = ['๐', '๐ค', '๐ฉ', 'โค', '๐', '๐', '๐', '๐', '๐', '๐งก', '๐', '๐', 'โช', '๐', '๐ฒ', '๐ง']
# Stikers_bg = ['๐', 'โช', '๐ฒ', '๐ง']
# Stickers_heart = ['๐ค', 'โค', '๐', '๐', '๐', '๐', '๐', '๐งก', '๐', '๐', '๐']
# def Stickers_mas(stick_all.All:
def Heart(heart):
    stickers_heart = choice(stick.Stickers_heart)
    stickers_bg = choice(stick.Stickers_bg)
    for i in range(13):  # bg '๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ'
        heart += stickers_bg
    heart += '\n'       # 1end
    for i in range(3):  # 2_start bg '๐ฅ๐ฅ๐ฅ๐๐๐ฅ๐ฅ๐ฅ๐๐๐ฅ๐ฅ๐ฅ'
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
        heart += stickers_bg  # '๐ฅ๐ฅ๐๐๐๐๐ฅ๐๐๐๐๐ฅ๐ฅ'
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
        heart += stickers_bg  # ๐ฅ๐๐๐๐๐๐๐๐๐๐๐๐ฅ
    for i in range(11):
        heart += stickers_heart
    for i in range(1):  # bg
        heart += stickers_bg
    heart += '\n'  # 4 end

    #-----------------------------------------
    for i in range(1):  # 5_start bg
        heart += stickers_bg  # ๐ฅ๐๐๐๐๐๐๐๐๐๐๐๐ฅ
    for i in range(11):
        heart += stickers_heart
    for i in range(1):  # bg
        heart += stickers_bg
    heart += '\n'  # 5 end

    for i in range(2):  # 6_start bg
        heart += stickers_bg  #๐ฅ๐ฅ๐๐๐๐๐๐๐๐๐๐ฅ๐ฅ
    for i in range(9):
        heart += stickers_heart
    for i in range(2):  # bg
        heart += stickers_bg
    heart += '\n'  # 6 end

    for i in range(3):  # 7_start bg
        heart += stickers_bg  #๐ฅ๐ฅ๐ฅ๐๐๐๐๐๐๐๐ฅ๐ฅ๐ฅ
    for i in range(7):
        heart += stickers_heart
    for i in range(3):  # bg
        heart += stickers_bg
    heart += '\n'  # 7 end

    for i in range(4):  # 8_start bg
        heart += stickers_bg  #๐ฅ๐ฅ๐ฅ๐ฅ๐๐๐๐๐๐ฅ๐ฅ๐ฅ๐ฅ
    for i in range(5):
        heart += stickers_heart
    for i in range(4):  # bg
        heart += stickers_bg
    heart += '\n'  # 8 end

    for i in range(5):  # 9_start bg
        heart += stickers_bg  #๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐๐๐๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ
    for i in range(3):
        heart += stickers_heart
    for i in range(5):  # bg
        heart += stickers_bg
    heart += '\n'  # 9 end

    for i in range(6):  # 10_start bg
        heart += stickers_bg  #๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ
    for i in range(1):
        heart += stickers_heart
    for i in range(6):  # bg
        heart += stickers_bg
    heart += '\n'  # 10 end

    for i in range(13):  # 11_start bg
        heart += stickers_bg  #๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ
    heart += '\n'  # 11 end

    #print(heart)
    return heart

#
# typing_symbol = '๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ'+'\n' \
#                   '๐ฅ๐ฅ๐ฅ๐๐๐ฅ๐ฅ๐ฅ๐๐๐ฅ๐ฅ๐ฅ'+'\n' \
#                   '๐ฅ๐ฅ๐๐๐๐๐ฅ๐๐๐๐๐ฅ๐ฅ'+'\n' \3
#                   '๐ฅ๐๐๐๐๐๐๐๐๐๐๐๐ฅ'+'\n' \4
#                   '๐ฅ๐๐๐๐๐๐๐๐๐๐๐๐ฅ' + '\n' \5
#                   '๐ฅ๐ฅ๐๐๐๐๐๐๐๐๐๐ฅ๐ฅ' + '\n' \6
#                   '๐ฅ๐ฅ๐ฅ๐๐๐๐๐๐๐๐ฅ๐ฅ๐ฅ' + '\n'\7
#                   '๐ฅ๐ฅ๐ฅ๐ฅ๐๐๐๐๐๐ฅ๐ฅ๐ฅ๐ฅ' + '\n' \8
#                   '๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐๐๐๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ' + '\n'\9
#                   '๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ' + '\n' \10
#                   '๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ' + '\n11
