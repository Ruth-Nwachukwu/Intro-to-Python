#puRpose of this project is to practice nesting if statements and Boolean variables

print("Please use a rating of 1-7 for the following questions:")

loan_size = int(input("How large is your loan? "))
credit_history = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))

grant_loan = False

if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        grant_loan = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            grant_loan = True
        else:
            grant_loan = False
else:
    if credit_history < 4:
        grant_loan = False
    else:
        if income >= 7 or down_payment >= 7:
            grant_loan = True
        elif income >= 4 and down_payment >= 7:
            grant_loan = True
        else:
            grant_loan = False

if grant_loan:
    print("The decision to grant loan is Yes!")       
else:
    print("The decision to grant loan is No")



