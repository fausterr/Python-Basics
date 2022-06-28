allLetters = ""
counter = 0

def counterLetters(userInput):
    global allLetters
    global counter

    # for letter in userInput:
    #     counter += 1

    counter += len(userInput)
    allLetters += userInput
while True:
    userInput = input("napisz cos: ")
    if userInput.lower() == "exit":
        break
    counterLetters(userInput)

    print(f"podano lacnzie: {str(counter)} znaków") # inny sposob wyswietlania
    print("podano lacznie: " + str(counter) + " znakow")
    print("napisano dotychczas: \n", allLetters)
