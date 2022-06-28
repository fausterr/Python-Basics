import random

randomnumber = 0;
numberOfTries = 0;

def defineRandomNumber():
    global randomnumber
    randomnumber = random.randint(1,100)

def checkUserPrediction(userInput):
    global randomnumber
    global numberOfTries

    numberOfTries += 1

    if userInput == randomnumber:
        print("zgadles")
        return 1
    elif abs(userInput - randomnumber) <= 5:
        print("bardzo goraco!")
        return 0
    elif abs(userInput - randomnumber) <= 10:
        print("goraco!")
        return 0
    elif abs(userInput - randomnumber) <= 20:
        print("letnio!")
        return 0
    elif abs(userInput - randomnumber) <= 40:
        print("zimno!")
        return 0

def main():
    global randomnumber
    global numberOfTries

    print("witaj przyjacielu")

    defineRandomNumber()
    print(randomnumber)
    isFind = 0
    while isFind == 0:
        userNumber = int(input("zgaduj liczbe: "))
        isFind = checkUserPrediction(userNumber)
    print("ilosc prob: " + str(numberOfTries))

if __name__ == "__main__":
    main()