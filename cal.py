
import os , time
class prem():
    def __init__(self):
        print("\n\033[1;37m    PLEASE FELLOW ME \033[1;32m")
        print("\n\033[1;37m    IT SIMPLE USEING A CALCULTER \033[1;32m ")
        print("")
        print("PLEASE SECLECT A NUMBER")
        print("")
        print("[1] = adding a number")
        print("[2] = sub a number")
        print("[3] = multi a number")
        print("[4] = divide a number")
        print("[E] = exit")
        print("")
        userss =input("  choise==> \n\033[1;37m ")
        if userss in ["" , " "]:
            exit()
        elif userss in ("5" , " 05"):
            print("    Thanks♥️")
            exit()
        if userss in ("1" , "01"):
            addii()
        if userss in ("2", "02"):
            sub()
        if userss in ("3", "03"):
            multi()
        if userss in ("4", "04"):
            divs()
        else:
            print("Select a any correct no")
            os.system("xdg-open https://www.facebook.com/suuny.sachan.777")
            print("")

            time.sleep(2.0)
            print("\033[1;33m    Type Your Fb id name")
            print("")
            input("\n\033[1;32m  Type Name ==> \033[1;36m")
            time.sleep(2.1)
            print("")
            print("\033[1;32m Successful Bro")
            time.sleep(2.0)
def sub():
    print("\033[1;92m      WELCOME TO SUBSTRATION NUMBERS     ")
    a = float(input("ENTER A 1ST NUMBER:- "))
    b = float(input("ENTER A 1ST NUMBER:-  "))
    c = a - b
    print("YOUR RESULT:- ", c)
    exit()

def multi():
    print("\033[1;92m      WELCOME TO MULIFICTION NUMBERS     ")
    a = float(input("ENTER A 1ST NUMBER:- "))
    b = float(input("ENTER A 1ST NUMBER:-  "))
    c = a * b
    print("YOUR RESULT:- ", c)
    exit()

def devs():
    print("\033[1;92m      WELCOME TO DIVISION NUMBERS     ")
    a = float(input("ENTER A 1ST NUMBER:- "))
    b = float(input("ENTER A 1ST NUMBER:-  "))
    c = a / b
    print("YOUR RESULT:- ", c)
    exit()


prem()
