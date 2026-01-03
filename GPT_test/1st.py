#November 26, 2025
# 1.
num1 = 1 #int(input("Enter first number: "))
num2 = 2 #int(input("Enter second number: "))
print("The sum of", num1, "and", num2, "is:", num1 + num2)

# Q2: I have done even or a lot of times so I am gonna be lil lazy with this

# Q3
text = "Hi" #input("Enter a string (word or phrase): ")
for i in range(1, 11):
    print(i, text)

# Q4 
password = "python123" #input("Enter password: ")
while (password != "python123"):
    print("Wrong password!!!")
    password = input("Enter the correct password: ")
print("The password is correct...")

# Q5
for i in range(0, 21):
    # i += 1
    if (i % 3 == 0):
        continue
    print(i)