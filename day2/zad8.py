import datetime

logs = []

def collectUserData():
    global logs

    userData = input("wprowadz dane: ")
    now = datetime.datetime.now()
    completeLog = f"{now.day}.{now.month}.{now.year} :: {now.hour}.{now.minute}.{now.second} ==> {userData}"
    logs.append(completeLog)

def showCollectionData():
    global logs
    for log in logs:
        print(log)

def main():
    while True:
        print(
            "do wyboru:\n"
            "1 wprowdz logi \n"
            "2 wyswietl logi \n"
            "3 wyjdz"
        )
        userInput = input("co chcialbys zrobic? ")
        if userInput == "1":
            collectUserData()
        elif userInput == "2":
            showCollectionData()
        elif userInput == "3":
            break
        else:
            print("co ty robisz!?!?!?!??!?!?!")

if __name__ == '__main__':
    main()


