def converter(temp):
    tempF = temp * 1.8 + 32
    return tempF

print("temperatura wynosi" , converter(200) , "st F")
print("temperatura wynosi " + str(converter(200)) + " st F") # musi byc rzutowanie