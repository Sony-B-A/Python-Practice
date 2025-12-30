# Simple Calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter the operation symbol to compute: ")

if (op == "+"):
    print("Sum of", a, "and", b, "is:", a + b)
elif (op == "-"):
    print("difference of", a, "and", b, "is:", a - b)
elif (op == "*"):
    print("product of", a, "and", b, "is:", a * b)
elif (op == "/"):
    print("division of", a, "and", b, "is:", a / b)
elif (op == "**"):
    print("power of", a, "and", b, "is:", a ** b)
# add else



# Student marks grade
marks = int(input("Enter student's marks: "))

if (marks >= 85 and marks <= 100):
    print("Grade: A")
elif (marks >= 60 and marks < 85):
    print("Grade: B")
elif (marks >= 35 and marks < 60):
    print("Grade: C")
elif (marks >= 0 and marks < 35):
    print("Fail!!")
else:
    print("Invalid")




# Guess the number game
secret_num = 47
guess = int(input("Guess the secret number: "))
while (guess != secret_num):
    print("Wrong guess!!!")
    guess = int(input("Guess the secret number: "))
    if (guess == secret_num):
        break # even without using break the output or logic remains the same
    #I made use of break cause You mentioned it int he question
print("You guessed it...")


#password validation
password = input("Enter password: ")
len = len(password) #storing the length
#checking if its working or not
#print(len) #print(len(password)) Why did I get an error with this
 
# I don't know how to check if it contains digits and uppercase letters so I am not gonna check that

if (len > 8):
    print("strong password")
else:
    print("weak password")



#Simple menu using match case
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while True:
    
    print("Menu\n1.Add\n2.Subtract\n3.Multiply\n4.divide\n5.exit")

    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print(a + b)
        case 2:
            print(a - b)
        case 3:
            print(a * b)
        case 4:
            print(a / b)
        case 5:
            break
        case _:
            print("Invalid choice!!!")