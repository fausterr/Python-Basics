# def PrintHello():
#     print("Hello")
#     return
#
# PrintHello()
# from datetime import date
# from datetime import timedelta
# def GiveWorkingDay():

#
#     #day = date.today()
#     day = date(2020,5,16)
#
#     if day.weekday() == 5:
#         workingday = day + timedelta(days=2)
#     elif day.weekday() == 6:
#         workingday = day + timedelta(days=1)
#     else:
#         workingday = day
#
#     print('workng day for',day,'is',workingday)
#     return
#
# GiveWorkingDay()
###################################

# from datetime import date
# from datetime import timedelta

# def GiveWorkingDay(y, m, d):
#
#     day = date(y,m,d)
#
#     if day.weekday() == 5:
#         workingday = day + timedelta(days=2)
#     elif day.weekday() == 6:
#         workingday = day + timedelta(days=1)
#     else:
#         workingday = day
#
#     print('workng day for', day,'is', workingday)
#     return
# #rozne sposoby wywolania:
# GiveWorkingDay(2020, 5, 13)
# GiveWorkingDay(y=2020, m=5, d=16)
# GiveWorkingDay(d=17, m=5, y=2020)
###################################

# from datetime import date
# from datetime import timedelta
#
# def GiveWorkingDay(y, m=1, d=1): # dla day wartosc domyslna
#
#     day = date(y,m,d)
#
#     if day.weekday() == 5:
#         workingday = day + timedelta(days=2)
#     elif day.weekday() == 6:
#         workingday = day + timedelta(days=1)
#     else:
#         workingday = day
#
#     print('workng day for', day,'is', workingday)
#     return
#
# GiveWorkingDay(2020, 5)
# GiveWorkingDay(2020, 5, 5)
# GiveWorkingDay(2017)
###################################

# from datetime import date
# from datetime import timedelta
#
# def giveWorkingDay(y=date.today().year,
#                    m=date.today().month,
#                    d=date.today().day):
#
#     day = date(y, m, d)
#
#     if day.weekday() == 5:
#         workingday = day + timedelta(days=2)
#     elif day.weekday() == 6:
#         workingday = day + timedelta(days=1)
#     else:
#         workingday = day
#
#     print('workng day for', day, 'is', workingday)
#     return
#
# giveWorkingDay(2020)
# giveWorkingDay(2020, 5, 5)
# giveWorkingDay()
###################################
#
# from datetime import date
# from datetime import timedelta
#
# def giveWorkingDay(y=date.today().year,
#                    m=date.today().month,
#                    d=date.today().day):
#
#     day = date(y, m, d)
#
#     if day.weekday() == 5:
#         workingday = day + timedelta(days=2)
#     elif day.weekday() == 6:
#         workingday = day + timedelta(days=1)
#     else:
#         workingday = day
#
#     return workingday
#
# nextWorkingDay = giveWorkingDay(2020)
# print(nextWorkingDay)
# nextWorkingDay = giveWorkingDay(2020, 5, 5)
# print(nextWorkingDay)
# nextWorkingDay = giveWorkingDay()
# print(nextWorkingDay)
#
# print(giveWorkingDay(2020, 5, 16))
###################################
#
# def DoAction(action, parameter):
#     print("action:", action)
#     print("parameter:", parameter)
#     return
#
# DoAction("buy", "shoes")
# print("***********")
#
# def DoAction2(action, *parameter): # * to touple
#     print("action:", action)
#     print("parameter:", parameter)
#     for element in parameter:
#         print("element is:", element)
#     return
#
# DoAction2("buy", "shoes", "socks")
# print("***********")
#
# def DoAction3(action, what, **parameter): # ** to dictionary
#     print("action:", action)
#     print("what:", what)
#     print("parameter:", parameter)
#     for element in parameter:
#         print(element, "=", parameter[element])
#     return
#
# DoAction3("buy", "shoes", size=45, color="brown", type="sport")
# print("***********")
# ###################################

def WeekDayFrench(dayNumber):

    names = {
        0: 'a',
        1: 'b',
        2: 'c',
        3: 'd',
        4: 'e',
        5: 'f'
    }

    return names.get(dayNumber, "error")
    #error to domyslna

print(WeekDayFrench(4))
print(WeekDayFrench(23))



