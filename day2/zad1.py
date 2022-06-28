def fun():
    while True:
        userInput = input("daj")
        if userInput == "exit":
            break
        userInput += "ish"
        print(userInput)

fun()