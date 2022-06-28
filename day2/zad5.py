database = {
    "adam" : "chleb",
    "lukasz" : "mroz",
    "lech" : "kowalski"
}

# tez dziala
# def auth(userInput, passwordInput, database) :
#     for user in database:
#         if userInput == user:
#             if passwordInput == database[user]:
#                 print("+")
#                 break
#             else:
#                 print("zle haslo")
#                 break
#         else:
#             print("zly user")
#             break

def auth(userInput, passwordInput, database):
    for user in database:
        if userInput == user and passwordInput == database[user]:
            return True
    return False

isFind = auth("adam", "chlep", database)
print(isFind)