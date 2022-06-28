#109
# percent = [2.606255012, 1.222935044, 1.283079391, 3.628708901, 6.856455493, 4.911788292,
#            2.886928629, 0.781876504, 0.962309543, 2.265437049, 6.816359262, 3.688853248,
#            3.468323978, 5.633520449, 4.530874098, 1.984763432, 0.922213312, 3.327987169,
#            4.190056135, 5.493183641, 1.864474739, 10.60545309, 2.425821973, 2.726543705,
#            8.740978348, 6.174819567]
#
# countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
#              'Norway', 'Portugal', 'United Kingdom', 'Serbia', 'Germany', 'Albania',
#              'France', 'Czech Republic', 'Denmark', 'Australia', 'Finland', 'Bulgaria',
#              'Moldova', 'Sweden', 'Hungary', 'Israel', 'Netherlands', 'Ireland',
#              'Cyprus', 'Italy']
# sumOfPoints = 4988
#
# print(max(percent))
# print(min(percent))
#
# for i in range(0, len(countries)):
#     print(percent[i], int(percent[i]), round(percent[i]))
# sum_a = 0
# for i in range(0, len(countries)):
#     a = percent[i]*sumOfPoints/100
#     print(countries[i],":", a)

#112
# percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
#            2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
#            3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
#            4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
#            8.740978348,6.174819567]
# percent.sort()
# print(percent)
# import statistics
# print(statistics.median(percent)) # to samo co (statistics.median_low(percent)+statistics.median_high(percent))/2
# print(statistics.median_low(percent))
# print(statistics.median_high(percent))
# print((statistics.median_low(percent)+statistics.median_high(percent))/2)

#115
# import math
# degree = 360
# print(degree, math.pi*degree/180)
# degree = 45
# print(degree, math.pi*degree/180)
#
# small_r = 22
# big_r = 27
# family_r = 38
# #Tu na szybko
# print(math.pi*math.pow(small_r/100, 2))
# print("cena m^2:", 11.5/(math.pi*math.pow(small_r/100, 2)))
# print(math.pi*math.pow(big_r/100, 2))
# print(math.pi*math.pow(family_r/100, 2))
#
# math_ls = dir(math)
# print(math_ls)

#118
# import random
# for i in range(0, 10):
#     print(random.randint(0,10))
#
# number1 = random.randint(1,100)
# number2 = random.randint(1,100)
# counter = 0
# print("wylosowano:", number1)
# while number1!=number2:
#     counter += 1
#     number2 = random.randint(1, 100)
#     print(number2)
# print("udalo sie za", counter,"razem")
#
# countries = [
#     'Uruguay',
#     'Russia',
#     'Saudi Arabia',
#     'Egypt',
#     'Spain',
#     'Portugal',
#     'Iran',
#     'Morocco',
#     'France',
#     'Denmark',
#     'Peru',
#     'Australia',
#     'Croatia',
#     'Argentina',
#     'Nigeria',
#     'Iceland',
#     'Brazil',
#     'Switzerland',
#     'Serbia',
#     'Costa Rica',
#     'Sweden',
#     'Mexico',
#     'Korea Republic',
#     'Germany',
#     'Belgium',
#     'England',
#     'Tunisia',
#     'Panama',
#     'Colombia',
#     'Japan',
#     'Senegal',
#     'Poland'
# ]
# import random
# random.shuffle(countries)
# groupNumber = 0
# print(countries)
# for i in range(0, len(countries)):
#     if (i+1)%4==0:
#         groupNumber+=1
#         print("---grupa X---")
#         print(countries[i])

#121
# import random
# dice = random.randint(1,6)
# #print(dice)
# dices = []
# for i in range(0,5):
#     dices.append(random.randint(1, 6))
# dices.sort()
# print(dices)

#124
# poem = '''1.Runą i w łunach spłoną pożarnych
# Krzyże kościołów, krzyże ofiarne
# I w bezpowrotnym zgubi się szlaku
# W lechickiej ziemi Orzeł Polaków.
# 2.O, jasne słońce- wodzu Stalinie!
# Niech sława twoja nigdy nie zginie
# Niechaj jak orły powiedzie z gniazda
# Rosja i z Kremla płonąca gwiazda.
# 3.Na ziemskim globie flagi czerwone
# Będą na wiatrach grały jak dzwony
# Czerwona Armia i wódz jej Stalin
# Odwiecznych wrogów na zawsze obali!
# 4.Zaćmisz się rychło w czarnej godzinie
# Polsko- Twe córy i syny,
# Wiara i każdy krzyż na mogile,
# U stóp am legą w prochu i pyle! '''
# lines = poem.split("\n")
# print(lines)
# a=1
# print(len(lines))
# for i in range(len(lines)-8):
#     print(lines[i])
#     print(lines[i+8])


#131
# import math
# inputdata = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# factortable = [0, 0.01, 0.02, 0.03, 0.05, 0.08, 0.13, 0.21, 0.34, 0.55, 0.89]
# print(len(inputdata), len(factortable))
#
# if len(inputdata)==len(factortable):
#     print("OK")
# else:
#     print("input data nad factorable need to have equal number of elements")
#
# minvalue = 0
# maxvalue = 0
# for i in  range(0, len(inputdata)):
#     minvalue = inputdata[i] - factortable[i] * inputdata[i]
#     maxvalue = inputdata[i] + factortable[i] * inputdata[i]
# print(minvalue, maxvalue)
#
# mininteger = math.floor(minvalue)
# maxinteger = math.ceil(maxvalue)
# print(mininteger, maxinteger)
#
#drugie zadanie praktycznie to samo

#134
# import random
# colors = ['Hearts','Diamonds','Clubs','Spades']
# figures = ['Ace','King','Queen','Jack','10','9']
# allCards = []
# for f in figures:
#     for c in colors:
#         allCards.append(f+"-"+c)
#
# print(allCards)
# random.shuffle(allCards) # TO CIEKAWE
# print(allCards)
#
# player1 = []
# player2 = []
# max = len(allCards)
# for i in range(0, max-1):
#     if i%2==0:
#         player1.append(allCards[i])
#     else:
#         player2.append(allCards[i])
# print("karty gracza 1: ", player1)
# print("karty gracza 2: ", player2)
#drugi sposob jest nudny :)

#137
colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = [
    {'Figure': 'Ace', 'Power': 14},
    {'Figure': 'King', 'Power': 13},
    {'Figure': 'Queen', 'Power': 12},
    {'Figure': 'Jack', 'Power': 11},
    {'Figure': '10', 'Power': 10},
    {'Figure': '9', 'Power': 9}]

allCards = []
for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard['Color'] = c
        allCards.append(aCard)

import random

random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []

player1 = allCards[:12]
player2 = allCards[12:]

print('-------PLAYER 1--------')
print(player1)

print('-------PLAYER 1--------')
print(player2)

while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    if card1["Power"] == card2["Power"]:
        player1.append(card1)
        player2.append(card2)
        print('=EQUAL \t %d \t %d \t' % (card1["Power"], card2["Power"]))
    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]))
    else:
        player2.append(card2)
        player2.append(card1)
        print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]))

if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
else:
    print('PLAYER 2 WON!!!!')