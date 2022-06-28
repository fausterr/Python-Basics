while True:
    if Intro() == "1":
        Clear()
        user = input("Please Enter Your Username\n==> ")
        pswd = input("Please Enter Your Password\n==> ")
        if Auth(user, pswd) == True:
            print("Welcome", user)
            break
        else:
            print("Wrong Login")
    elif Intro() == "2":
        Clear()
        Reg()
    elif Intro() == "3":
        print("ByeBye")
        break
    else:
        print("Wrong Pick")
adb = {
    "user": "password",
    "Admin": "Admin",
}


def Intro():
    intro = "Welcome to Messy CLI\n" \
            "Please Register OR Login\n" \
            "1.Login\n" \
            "2.Register\n" \
            "3.Quit\n"
    print(intro)
    return input("")


if __name__ == '__main__':
    def Clear():
        i = 0
        while i < 30:
            print("\n")
            i = i + 1


    def Auth(user, pswd):
        global adb
        for key in adb:
            if key == user and adb[key] == pswd:
                return True
        return False


    def Reg():
        global adb
        user = input("Please Enter username\n==>")
        try:
            if Auth(user, adb[user]) == True:
                print("user is already exists")
        except:
            pswd = input("Please Enter The password\n==>")
            adb[user] = pswd
            print("Registered")