from summary import *



def val():

    while True:
        print( "---------------------------------------\n\t\t1) Enter Income value\n\t\t2) Enter Expense "
               "value\n\t\t3) Summary\n\t\t4) Exit")
        a = input("Enter a number :- ")
        if a.isdigit():
            if a == '1':
                value = input("Enter Income value :- ")
                if value.isdigit():
                    inp = open("income.txt", "a")
                    inp.write(value + '\n')
                    inp.close()
                else:
                    print("\n---Error plz enter only number value--\n")

            elif a == '2':
                value = input("Enter Outcome value :- ")
                if value.isdigit():
                    exp = open("expense.txt", "a")
                    exp.write(value + '\n')
                    exp.close()
                else:
                    print("\n---Error plz enter only number value--\n")

            elif a == '3':
                summary()
            elif a == '4':
                break
            else:
                print("Incorrect number \nPlease check your entered number.\n")

        else:
            print("\tplz Enter below option number only\n")
    print("Thank you ")




