# f_smaller = 3.141592659732
# f_bigger = 3.877569237492
#
# print(f_smaller, f_bigger)
# print(int(f_smaller), int(f_bigger))
# print(abs(f_smaller), abs(-f_bigger))
# print(round(f_smaller, 2), round(f_bigger, 2), round(f_bigger,4))
# print(min(f_smaller, f_bigger), max(f_smaller, f_bigger))
#
# list=[1,2,3,4,5,4,4,5,4]
# print(sum(list), len(list))
# print(sum(list)/len(list))
# print(round(2.675,2))

# import math
# print(math.pi)
# print(math.floor(math.pi))
# from math import *
# print(pi)
# print(floor(pi))

# import random
# print(random.randint(1,100))
# print(random.choice(range(1,100)))
# print(random.randrange(1, 100))
# list=['abc','ad','vcd','asdsa','wwert']
# random.shuffle(list)
# print(list)
# print(random.random()) #losuje od 0 do 1, z miejscami po przecinku

# for i in range(32, 127): ##wyswietlanie ASCII
#     print(i, chr(i))
# import random
# ints = range(33,127)
# password = ''
# for i in range(8):
#     password += chr(random.choice(ints))
# print(password)
#
# line = 'this IS a very STRANGE text'
# print(line)
# print(line.capitalize())
# print(line.title())
# print(line.lower())
# print(line.upper())
#
# print(line.count('e'))
# print(line.rfind('e')) #od prawej liczac
# print(line.index('e'))
# if 'e' in line:
#     print("coo")
#
# print(line.startswith("this"))
# print(line.startswith("THIS"))
#
# import string
# print(string.ascii_letters)
# print(string.digits)
#
# line = 'this is the end of lesson'
# list = line.split(' ')
# print(list)
# print(' '.join(list))
# print('*'.join(list))

# import time
# print(time.time())
# print(time.localtime(time.time()))
# print(time.asctime(time.localtime(time.time())))
#print(time.localtime(time.clock())) ZAMIAST CLOCK DAJEMY TERAZ perf_counter()
# import calendar
# print(calendar.month(2020, 5, w=5, l=2))
# print(calendar.month(2020, 9))
# print('week day is',calendar.weekday(2020,5,8)) #liczy od zera
# print(calendar.isleap(2020)) # czy przestepny
# print(calendar.leapdays(2000, 2050)) # dni przestepene miedzy okreslonymi latami
# print(calendar.calendar(2020))

# import datetime
# print('minimum and maximum', datetime.MINYEAR, datetime.MAXYEAR)
# d1 = datetime.timedelta(days=1, hours=2, minutes=-30)
# print(d1)
# d2 = datetime.timedelta(days=-1,hours=-2,minutes=-3)
# print(d2)
# print('timedelta sum:', d1+d2)
# print('********')
# print('today is',datetime.date.today())
# today = datetime.date.today()
# daysToPay = datetime.timedelta(days=7)
# print('today is', today)
# print('bills dhould be paid within', daysToPay, "days")
# print('the bill should be paid till:', today + daysToPay)
# import datetime
# endOfTheWorld = datetime.date.max
# print('koniec swiata', endOfTheWorld)
# print(endOfTheWorld.weekday())
#
# bornDate= datetime.date(2000,8,15)
# today = datetime.date.today()
# print(today - bornDate)
# import datetime
# print(datetime.datetime.now())
# print(datetime.datetime.today())
# print(datetime.datetime.utcnow()) #strefa czasowa inna
# print(datetime.datetime.today().weekday())
#
# import random
# myNumbers = []
# while len(myNumbers) <7:
#     newMyNumber = random.randint(1,15)
#     if newMyNumber in myNumbers:
#         print('eliminated:', newMyNumber)
#         continue
#     myNumbers.append(newMyNumber)
#
# print('numbers:', myNumbers)
#
#trojkat pascala:
# numbers = [1]
# print(numbers)
# for i in range(5):
#     newNumbers = [1]
#     position = 0
#     while position < len(numbers)-1:
#         newNumbers.append(numbers[position] + numbers[position+1])
#         position+=1
#     newNumbers.append(1)
#     numbers = newNumbers.copy()
#     print(numbers)
#
# numbers = [1]
# print(numbers)
# for i in range(5):
#     position=0
#     newNumbers = [1]
#     while position<len(numbers) - 1:
#         newNumbers.append(numbers[position] + numbers[position+1])
#         position+=1
#     newNumbers.append(1)
#     numbers = newNumbers.copy()
#     print(numbers)
    











