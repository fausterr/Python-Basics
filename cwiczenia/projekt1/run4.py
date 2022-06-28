# x = 4
# y = True
# z = False
#
# if x>4:
#     print("hello")
# else:
#     if y != True:
#         print("+")
#     else:
#         if z == False:
#             print("-")

# x = 4
# y = True
# z = False
# if x>4:
#     print("hello")
# elif y != True:
#     print("+")
# elif z == False:
#     print("-")
#
# i=2
# i+=2
# print(i)
# i=1
# imax=4
# while i<= imax:
#     print("+")
#     i+=1
# else:
#     print("-")
#
# values=[10,2,32,43,3,7,12,99,2,14,23,32,42,8]
# i = 0
# max = len(values)

# while i<max:
#     if i<10:
#         print(i, ")", "", values[i])
#     else:
#         print(i, ")", values[i])
#     i+=1
#
# while i<max:
#     print(values[i])
#     if values[i] < values[i+1] and values[i+1]<values[i+2]:
#         print(values[i], "", values[i+1], "", values[i+2], "", )
#     i+=1
#
# cargo=[10,2,32,4,21,43,3,7,12,99,2,14,23,32,42,8]
# print(cargo)
# cargo.sort()
# print(cargo)
# boxCapacity = 90
# box = []
# i = 0
#
# while sum(box) + cargo[i] < boxCapacity and i<len(cargo):
#     box.append(cargo[i])
#     i+=1
#
# print("suma boxa: ", sum(box))
# print("elementy boxa: ", box)

# cargo=[10,2,32,4,21,43,3,7,12,99,2,14,23,32,42,8]
# for i in cargo:
#     print(i)
# else:
#     print("skonczylem!")
#
# for n in range(5):
#     print(n) # of 0 do 4
#
# for m in range(0, 21): # trzeci parametr oznacza, ze co druga
#     if m %2 == 0:
#         print('number %2d is %s' % (m, 'even')) #%2d czyli maksymalnie dwucyfrowa liczba
#     else:
#         print('number %2d is %s' % (m, 'no even'))

# for x in range(1,6):
#     for y in range(1,6):
#         print(x,'*',y,'=',x*y)

#1sposob
# for candidate in range(2, 31):
#     isPrime = True
#     for divider in range(2, candidate):
#         if candidate % divider == 0:
#             print('%2d is not a prime number - divider is %2d' % (candidate, divider))
#             break
#     if isPrime:
#         print('%2d is prime!' % (candidate))
#2sposob
# for candidate in range(2, 31):
#
#     for divider in range(2, candidate):
#         if candidate % divider == 0:
#             print('%2d is not a prime number - divider is %2d' % (candidate, divider))
#             break
#     else:
#         print('%2d is prime!' % (candidate))

# persons = ['Eliza', 'steb@mycompany.com','Seba','Magda','oszkas@mycompany.eu','okk']
# domain = 'mycompany.com'
# emails = []
# for p in persons:
#     if '@' in p:
#         emails.append(p)
#     else:
#         email = p + '@' + domain
#         emails.append(email)
# for email in emails:
#    print(email)

# persons = ['Eliza', 'steb@mycompany.com','Seba','Magda','oszkas@mycompany.eu','okk']
# domain = 'mycompany.com'
# emails = []
# for p in persons:
#     if '@' in p:
#         emails.append(p)
#         continue
#     email = p + '@' + domain
#     emails.append(email)
# for email in emails:
#     print(email)