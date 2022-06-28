#34
# s = 'A good programmer is someone who always looks both ways before crossing a one-way street'
# print(s.upper())
# print(s.lower())
# print(s.endswith('street'))
# print(s.isupper())
# print(s.upper().isupper())
# print(s.find('one'))
# print(s.replace('one','1'))
# print(s.replace('one','1').replace('both','1'))
# print(s.split(' '))
# print(s.isdigit())
# print(s.isdecimal())
# print(s.isalpha())
# print(s.isalnum())

#37
# firstName = 'Kasia'
# familyName = 'Sowa'
# lastName = 'Mrugała'
# newName = firstName + ' ' + familyName + ' ' + lastName
# print(newName)
#
# music = '"Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I\'m a Man" Steve Winwood'
# print(music)
#
# music2 = '"Universal Fanfare" Jerry Goldsmith\n"Happy Together" Garry Bonner\n"I\'m a Man" Steve Winwood\a'
# print(music2)
#
# print('(\\(\\\n( -.-)\nO_(\'\')(\'\')')

#40
# print('to print the \\ you need to put \\ twice in your text \nlike this: \\\\')
# print('The best hits of \'80s!!!')
# print("The best hits of '80s!!!")
#
# amountPLN = 234
# print('cur','\t', 'exchange', 'amount')
# print('USD', '\t', 3.65, '\t', amountPLN/3.65)
# print('EUR', '\t', 4.23, '\t', amountPLN/4.23)
# print('tu wersja z kursu:')
# print('cur','\texchange','amount')
# print('USD',"\t",3.65,"\t",amountPLN/3.65)
# print('EUR','\t',4.23,"\t",amountPLN/4.23)
#
# ValueAsText = '123.45'
# factor = 1.23
# print('value is ',ValueAsText, ' factor is', factor, 'value*factor=', float(ValueAsText)*factor)

#43
# helloMessage = "Hello %s!"
# print(helloMessage % ('Kate'))
# helloMessage2 = "Hello {0:s}"
# print(helloMessage2.format("Kate i Chris"))
# helloMessage3 = "%s has %d %s"
# print(helloMessage3 %('Kate', 1, 'animal'))
# helloMessage4 = "{0:s} has {1:d} {2:s}"
# print(helloMessage4.format('Kate', 1, 'animal'))
#
# line = "{0:20s} costs {1:6d} €"
# print(line.format("ICE CREAM", 3))
# print(line.format("TRIP TO VENICE", 119))
# print(line.format("PIZZA HAWAII", 6))

#46
# name = 'Jan'
# age = 26
# daysInYear = 365
# message = "{0:s} is {1:d} years old, so is about {2:d} days old"
# print(message.format(name, age, age*daysInYear))
#
# a = 1234567890
# b = 12345
# c = a//b
# d = a%b
# result = '{0:d} divided by {1:d} is {2:d} and the rest is {3:d}'
# print(result.format(a, b, c, d))

#49
# isAutomaticMode = False
# is80PercentLight = True
# isDirectLight = True
# isRainy = True
# turnLightsOn = isAutomaticMode and (not isAutomaticMode or isDirectLight or isRainy)
# print("Automatic mode:   ", isAutomaticMode)
# print("Is the light good:", is80PercentLight)
# print("Is sun low:       ", isDirectLight)
# print("Is it rainy:      ", isRainy)
# print("TURN LIGHTS ON:   ", turnLightsOn)

#52
# v1 = 126
# v2 = '126'
# v3 = 126.0
# v4 = '126.0'
# print(v1 + v3, type(v1 + v3))
# print(v2 + v4, type(v2 + v4))
#
# print(7 - 1 * 0 + 3 + 3)
# print(4**5/2**3)
# print(99+9/9)

#55
# q = "THE EYES"
# print(q[0]+q[1]+q[2]+q[5]+q[3]+q[7]+q[4]+q[6])
#
# q2 = 'a gentleman'
# print(q2[3]+q2[6]+q2[7]+q2[2]+q2[0]+q2[4]+q2[5]+q2[1]+q2[8:])
#
# line = 'Program "Kropka nad i" nadamy o: 22:00'
# find = line.find(':') #31
# time = line[31+2:]
# print(time)
# find = line.find('"')
# print(find) #8
# tmp = line[8:]
# print(tmp)
# find =  tmp[1:].find('"') #12
# title = tmp[:12+2]
# print(title)

#57
result = (43*5 + 50)*20 + 1020 - 1993
print(result)

result = (3*2 + 10)/2 - 3
print(result)

obecnosc = 77
srednia = 5.0
praca_semestralna = True
zaliczone = (obecnosc>=80 and srednia >= 3.0) or praca_semestralna==True
print(zaliczone)