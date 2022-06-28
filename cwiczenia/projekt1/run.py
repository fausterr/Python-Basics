# x = "Witam was kotki"
# y = x[-4]
#*******************************
# x=10
# print(bool(x))
# if bool(x):
#     print("AAAA")
# else:
#     print("BBBB")
#*******************************
# produkty = ["mleko", "ser", "jajka"]
# produkty.count("mleko")
# print(produkty.count("mleko"))
#
# produkty2 = ["prod1", "prod2"]
# produkty.extend(produkty2)
# produkty.insert(2, "chleb")
# produkty.pop(1)
# print(produkty)

# person = {"wiek":20, "imie": "johnson", "naziwsko": "aleksandovic"}
# print(person)
# print(person["wiek"])
# print(type(person))
#*******************************
# while True:
#     print("daj liczbe")
#     x = input()
#     a = int(x)
#     print(a*a)

# list = ["a", "b", "c", "d", "e", "f"]
# for litera in list:
#     print(litera)
#     if litera =="e":
#         print("+++")

# for i in range(20, 25):
#     print(i)

# for x in range(0, 15, 2):
#     print(x)
#*******************************
# fruits = ['apple', 'orange', 'pear', 'banana', 'apple']
#
# for x, fruit in enumerate(fruits):
#     if x==3:
#        break
#     print(x)
#     print(fruit)

# x="hello {}"
# print(x)
# y=x.format("my","world")
# print(y)
# i=2
# fruits = ['apple', 'orange', 'pear', 'banana', 'apple']
# print(x.format(fruits[i]))
#*******************************
# fruits = ['apple', 'orange', 'pear', 'banana', 'apple']
# for fruit in fruits:
#     if fruit == "orange":
#         continue
#     if fruit == "banana":
#         break
#     print(fruit)

# fruits = ['apple', 'orange', 'pear', 'banana', 'apple', 'strawberry', 'apple']
#
# if "orange" in fruits:
#     print("jee")
# else:   # else + if = elif
#     if "aaa"  in fruits:
#         print("+")
#     else:
#         print("-")
#*******************************
# liczba = int(input())
#
# if liczba !=2 and liczba < 5: # or, and
#     print("+")
# else:
#     print("-")
#
# lista = [1,2,3,4,5]
# if not 5 in lista:
#     print("+")
# else:
#     print("-")
#*******************************
# import time
# print("start")
# time.sleep(1)
# print("raz")
# time.sleep(1)
# print("dwa")
# time.sleep(1)
# print("stop")
import time
# timer = time.time()
# while True:
#     if time.time() - timer >1:
#         print("1 sekundy")
#         timer = time.time()

# while True:  ta petla jest inna!!
#     print("2 sekundy")
#     time.sleep(2)

# timer = time.time()
# timer2 = time.time()
# while True:
#     if time.time() - timer >1:
#         print("1 sekundy")
#         timer = time.time()
#     if time.time() - timer2>2:
#         print("2")
#         timer2 = time.time()

