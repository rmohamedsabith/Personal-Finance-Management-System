def summary():
    print("\t\tSummary of income and expense\n\t====================================\n")
    sum_inc=0
    no_inc=0
    sum_exp=0
    no_exp=0


    with open("income.txt","r") as f_in:
        for inc in f_in:
            inc=inc.strip()
            sum_inc=sum_inc+float(inc)
            no_inc=no_inc+1

    avg_inc=sum_inc/no_inc
    with open("expense.txt","r") as f_exp:
        for exp in f_exp:
            exp = exp.strip()
            sum_exp = sum_exp + float(exp)
            no_exp = no_exp + 1

    avg_exp = sum_exp/ no_exp
    print("\tIncome Details\n")
    print("\t\tNumber of Records in Income file - ",no_inc)
    print("\t\tTotal Income                     - ",sum_inc)
    print("\t\tAverage Income                   - ",avg_inc)
    print("\n\n\tExpense Details\n")
    print("\t\tNumber of Records in Expense file - ",no_exp)
    print("\t\tTotal Expense                     - ",sum_exp)
    print("\t\tAverage Expense                   - ",avg_exp)
    print("\n\tDifference between income and expense   -  ",sum_inc-sum_exp)