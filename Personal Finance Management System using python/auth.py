from task101 import *


def register():
    print("----------------------------------------\n\t\tRegister")
    username = input("Please input your username :- ")
    password = input("Please input your desired password :- ")
    file = open("username.txt", "a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    login()


def login():
    print("----------------------------------------\n\t\tLogin")
    username = input("Please enter your username :- ")
    password = input("Please enter your password :- ")
    lis=open("username.txt", "r").readlines()
    for line in lis:
        login_info = line.split()
        if username == login_info[0] and password == login_info[1]:
            print("Correct credentials!")
            val()
            main()
        elif username != login_info[0] and password != login_info[1]:
            continue
    print("Incorrect credentials.")
    main()

def main():
    print("--------------------------------------\n\t\t1) Register\n\t\t2) Login")
    a = input("Enter a Number:- ")
    if a.isdigit():
        if a == '1':
            register()

        elif a == '2':
            login()
        else:
            print("Plz Enter above option only")

    else:
         print("Enter only number\n")
         main()

main()