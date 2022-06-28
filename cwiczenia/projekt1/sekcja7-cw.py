#81
# firstRow = 1
# lastRow = 31
# currentRow = firstRow
#
# while currentRow <= lastRow:
#     print("Row number", currentRow)
#     currentRow+=1
#
# i=1
# while i<=13:
#     print("i=", i, "i^2=", i*i, "i^3=", i**3)
#     i+=1
#
# i=0
# while i<17:
#     print("2 do potegi",i,"=",2**i)
#     i+=1
#
# i=1
# row="x"
# while i<11:
#     print(row*i)
#     i+=1

#84
# numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
#
# i=0
# while i < len(numbers):
#     x = numbers[i-1]
#     y = numbers[i]
#     if(y==x*x):
#        print(x,y)
#     i+=1
#
# i=0
# while i < len(numbers):
#     x = numbers[i]
#     y = numbers[i-1]
#     z = numbers[i-2]
#     if(z*z==y and y*y==x):
#         print(z,y,x)
#     i+=1
#
# texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# i = 1
# while i < len(texts):
#     x = texts[i]
#     y = texts[i-1]
#     if(len(x)==len(y)):
#         print(x,y)
#     i+=1

#87
# i = 1
# while i<51:
#     print(i,"+",i+1,"=",i+i+1)
#     i+=1
#
# import random
# my_number = random.randint(0,1)
# trials = 1
# while True:
#     guess = int(input())
#     if guess==my_number:
#         print("Udalo ci sie za",trials,"razem")
#         break
#     else:
#         trials+=1

#90
# data = ['Error:File cannot be open',
#         'Error:No free space on disk',
#         'Error:File missing',
#         'Warning:Internet connection lost',
#         'Error:Access denied']
#
# i = 0
# while i<len(data):
#     elements = data[i].split(":")
#     print(elements[0].upper(), elements[1])
#     i+=1
#
# i=0
# while i<len(data):
#     elements = data[i].split(":")
#     if elements[0] == "Error":
#         print(elements[0].upper(), elements[1])
#     else:
#         print(elements[0], elements[1])
#     i+=1

#93
# string_A = '+---+---+---+---+'
# string_B = '|   |   |   |   |'
#
# for i in range(0,10):
#     print(string_A)
#
# print(string_A)
# for i in range(0, 4):
#     print(string_B)
#     print(string_A)
#
# for i in range(1, 10):
#     print("x"*i)

#96
# n = 4
# silnia = 1
# for i in range(1, n+1):
#     silnia*=i
#     print(silnia)
#
# n = 10
# silnia = 1
# for i in range(1, n+1):
#     silnia*=i
#     print("silnia z ",i,"=",silnia)
#
# list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
# list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']
#
# for i in range(0, len(list_noun)):
#     print(list_noun[i], list_adj[i])
#
# x = 3
#
# for i in range(1, x + 1):
#
#     result = 1
#
#     for j in range(1, i + 1):
#         result *= j
#         print("i = ", i, "j = ", j, "result = ", result)
#
#     print(i, result)

#99
# text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.'
#
# words = text.split(" ")
# short_text = ""
# counter = 0
# for text in words:
#     short_text=short_text+text+" "
#     counter+=1
#     if counter > 18:
#         break
#
# print(short_text)
#
# definitions = [
#     'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.',
#     'Ein Kraftwandler ist eine mechanische Anordnung zur Veränderung einer Kraft in Bezug auf ihren Angriffspunkt, ihre Richtung oder ihren Betrag. Die einfachsten Kraftwandler sind Seile, Stangen, Rollen, schiefe Ebenen und Hebel. Dies sind gleichzeitig die grundlegenden einfachen Maschinen.',
#     'La ventaja mecánica es una magnitud adimensional que indica cuánto se amplifica la fuerza aplicada usando un mecanismo (ya sea una máquina simple, una herramienta o un dispositivo mecánico más complejo) para contrarrestar una carga de resistencia.',
#     'Cette notion s\'applique de manière évidente dans les systèmes de poulies et de leviers. Elle est centrale dans les systèmes de freinage : on applique une petite force sur un parcours important et l\'on obtient une force importante transmise au système de freinage pour une course de faible distance.'
# ]
#
# for d in definitions:
#     words = d.split(" ")
#     short_text = ""
#     counter = 0
#     for text in words:
#         short_text+=text+" "
#         counter+=1
#         if counter > 18:
#             break
#     print(short_text)


#105
# initialCapital = 20000
# percent = 0.03
# maxTimeYears = 10
# newInitialCapital = 20000
# totalEarn = 0
#
# for i in range(1, maxTimeYears+1):
#     earn = newInitialCapital*percent
#     newInitialCapital+=newInitialCapital*percent
#     totalEarn+=earn
#     print(newInitialCapital, earn, totalEarn)
#

# number = 20730906
# newNumber = str(number)
# newNumber.split(" ")
# sum = 0
# for i in range(0, len(newNumber)):
#     sum+=int(newNumber[i])
# print(sum, type(sum))
#
# number=20730906
# tmpnumber = number
# sumOfDigits = 0
# while tmpnumber >0:
#     digit = tmpnumber % 10
#     sumOfDigits += digit
#     tmpnumber = tmpnumber//10
# else:
#     print('the sum of digits of ', number, ' is',sumOfDigits)
#
# tekst = "United Space Alliance: This company provides major support to NASA for various projects, such as the space shuttle. One of its projects is to create Workflow Automation System (WAS), an application designed to manage NASA and other third-party projects. The setup uses a central Oracle database as a repository for information. Python was chosen over languages such as Java and C++ because it provides dynamic typing and pseudo-code–like syntax and it has an interpreter. The result is that the application is developed faster, and unit testing each piece is easier."
#
# counter = 0
# tekstTab = tekst.split(" ")
# for word in tekstTab:
#     if len(word)>6:
#         if word.isalpha():
#             counter += 1
# #            print(word)
#
# print(counter)
#
# text = '''
# United Space Alliance: This company provides major support to NASA for
# various projects, such as the space shuttle. One of its projects is to
# create Workflow Automation System (WAS), an application designed to
# manage NASA and other third-party projects. The setup uses a central
# Oracle database as a repository for information. Python was chosen over
# languages such as Java and C++ because it provides dynamic typing and
# pseudo-code–like syntax and it has an interpreter. The result is that
# the application is developed faster, and unit testing each piece is easier.
# '''
# listOfWords = text.replace('\n', ' ').split(' ')
# wordLength = 6
# i = 0
# shortWords = 0
# longWords = 0
# while i < len(listOfWords):
#     if len(listOfWords[i]) > wordLength:
#         longWords += 1
# #        print(listOfWords[i])
#     else:
#         shortWords += 1
#
#     i += 1
# print("Words shorter than ", wordLength, ":", shortWords)
# print("Words longer than ", wordLength, ":", longWords)

# 106
# fibonacciIterations=20
# a = 0
# b = 1
# c = 0
# for i in range(0, fibonacciIterations):
#     print(c)
#     a = b
#     b = c
#     c = a + b
#     i+=1
#
# text = """Industrial Light & Magic: In this case, you find Python
#     used in the production process for scripting complex,
#     computer graphic-intensive films. Originally, Industrial
#     Light & Magic relied on Unix shell scripting, but it was
#     found that this solution just couldn’t do the job. Python
#     was compared to other languages, such as Tcl and Perl, and
#     chosen because it’s an easier-to-learn language that the
#     organization can implement incrementally. In addition, Python
#     can be embedded within a larger software system as a scripting
#     language, even if the system is written in a language such as
#     C/C++. It turns out that Python can successfully interact with
#     these other languages in situations in which some languages can’t. """
#
# text2 = text.replace("\n", "").split(" ")
# i = 0
# for t in text2:
#     if t.lower().find("p")>=0:
#         print(t)
#     i+=1
#
# dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less then 50%'}
#
# for key in dictionary.keys():
#     print(key, "-", dictionary[key])

text = """Industrial Light & Magic: In this case, you find Python
    used in the production process for scripting complex,
    computer graphic-intensive films. Originally, Industrial
    Light & Magic relied on Unix shell scripting, but it was
    found that this solution just couldn’t do the job. Python
    was compared to other languages, such as Tcl and Perl, and
    chosen because it’s an easier-to-learn language that the
    organization can implement incrementally. In addition, Python
    can be embedded within a larger software system as a scripting
    language, even if the system is written in a language such as
    C/C++. It turns out that Python can successfully interact with
    these other languages in situations in which some languages can’t. """


