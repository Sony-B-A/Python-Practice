# Mini Project 3 — Calculator with lambda
# Use lambdas for:
# add
# sub
# mul
# div
# Use match-case to select.
sum = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b

x = 4
y = 5
print("Sum =", sum(x, y))
print("difference =", sub(x, y))
print("Product =", mul(x, y))
print("Division =", div(x, y))

# Mini Project 2 — Student Report Generator
# Function that takes:
# name
# 5 subject marks
# Returns:
# avg
# percentage
# grade

def stu_rep(name, m1, m2, m3, m4, m5, m6):
    avg = (m1 + m2 + m3 + m4 + m5 + m6)/6
    perc = ((m1 + m2 + m3 + m4 + m5 + m6)/600) * 100
    if (perc >= 85 and perc <= 100):
        grade = 'A'
    elif (perc >= 75 and perc < 85):
        grade = 'B'   
    elif (perc >= 60 and perc < 75):
        grade = 'C'
    elif (perc >= 35 and perc < 60):
        grade = 'D'
    elif (perc >= 0 and perc < 35):
        grade = 'F'  
    else:
        grade = "Invalid marks" 
    print(f"name: {name}\nAverage: {avg}\nPercentage: {perc}\nGrade: {grade}")
name = "Sangeeta"
m1 = 93
m2 = 87
m3 = 99
m4 = 96
m5 = 91 
m6 = 96
stu_rep(name, m1, m2, m3, m4, m5, m6)
'''' 
name, avg, perc, grade = stu_rep(name, m1, m2, m3, m4,m5)    
print(f"name: {name}\nAverage: {avg}\nPercentage: {perc}\nGrade: {grade}")
I dont know How to access returned values
I dont even know how to unpact this so gotta print in the function only'''

# Mini Project 1 — Simple ATM (Functions Only)
# Functions:
# check_balance()
# deposit()
# withdraw()
# exit()
# Use a loop + match-case.


def check_balance():
    print("Balance =",bal)
def deposite():
    amt = int(input("Enter the amount: "))
    global bal
    bal += amt

def withdraw():
    global bal
    wd = int(input(("Enter the amount to withdraw: ")))
    if (wd <= bal):
        bal -= wd
    else:
        print("Insufficient amount for the current balance!!!")
bal = 0
while (True):
    print("1.Check Balance\n2.Deposite\n3.Withdraw\n4.Exit")
    choice = int(input("Enter the choice number: "))
    match choice:
        case 1:check_balance()
        case 2:
            deposite()
        case 3:
            withdraw()
        case 4:
            print("Tata bay bay")
            break
        case _:print("Invalid")
