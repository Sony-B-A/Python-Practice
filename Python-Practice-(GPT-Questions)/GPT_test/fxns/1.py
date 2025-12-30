# Q1 Write a function that takes a name and prints:
#Hello <name>
def greet(name):
    return "Hello", name
name = "Sony"
print(greet(name))
# ('Hello', 'Sony') Why the output is like this

def greet(name):
    return "Hello " + name
name = "Sony"
print(greet(name))
# o/p: Hello Sony

#why the output is different for the above ones although both are the similar codes

def greet(person_name):
    print("Hello", name)
name = "Sony"
greet(name)
# o/p: Hello Sony This is understandable

#Test 2
#Write a function that returns the square of a number.
def Square(num = 2): #I added default value here hehe
    print(num ** 2)
Square(4)

#Test 3
#Write a function with default parameter:
#def greet(name="Guest")
def greet(name = "Friends"):
    print("Hello", name)
person = "Sony"
greet(person)
greet()

# Test 4
# Write a function to return:
# sum
# average
# max
# of 3 numbers.
def compute(a = 1, b = 2, c = 1):
    s = a + b + c
    a = s/ 3
    m = max(a, b, c)
    return s, a, m
# for defaults
add, avg, maxi = compute()
print("Sum =", add)
print("Average =", avg)
print("maximum =", maxi)
# for non defaults
add, avg, maxi = compute(2, 4, 2)
print("Sum =", add)
print("Average =", avg)
print("maximum =", maxi)
# s, avg, m = compute(1, 3, 5)
# print(s, avg, m)
# please explain how unpacking works

# without unpacking
def compute(a, b= 1, c = 3):
    print("Sum =", a + b +c)
    print("Average =", (a + b + c) / 3)
    print("maximum =", max(a, b, c))
compute(4)
compute(1, 3, 5)
compute(2, 2)
(2, 2) # why it's not throwing any error

# Test 5
# Write a function that checks whether number is prime.

def PRIME(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if (n % i == 0):
            # break -> Wrong!!!
            return False
    return True
num = 2
is_prime = PRIME(num)
print("is", num, "Prime number:", is_prime)

# Test 6
# Write a function that counts vowels in a string.
def count_vowels(phrase):
    count = 0
    for ch in phrase:
        if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
            count += 1
    return count
sentence = "I am Sangeeta, upskilling my knowledge in Python"
# sentence = "aeiou" -> just testing
nums = count_vowels(sentence)
print("Number of vowels in the sentence is =", nums)

# Test 7
# Write a function that takes a list and returns only even numbers.
def even(num):
    number = 0
    for i in num:
        if (i % 2 == 0):
            print(i)
n =[1, 2, 3, 4, 5, 6, 7, 8, 9]
even(n)

# Test 8
# Write a lambda that multiplies 3 numbers.

mult = lambda x, y, z :  x * y * z
print("multiplication of 3 numbers", mult(2, 2, 5))

# Test 9
# Write a function to calculate factorial using return instead of print.
def fact(num):
    fact = 1
    for i in range (1, num + 1):
        fact *= i
    return fact
n = 5
print("Factorial of", n, "is:", fact(n))

# Test 10
# Write a menu-driven program using functions:
# add
# subtract
# multiply
# divide

def add(a, b):
    print("Addition =", a + b)
def sub(a, b):
    print("Subtraction =", a - b)
def mult(a, b):
    print("Product =", a * b)
def div(a, b):
    print("Division =", a / b)

a = int(input("enter a value: "))
b = int(input("enter b value: "))
while (True):

    print("Menu\n+\t-\t*\t/\t0")
    choice = input("Enter your choice: ")
    match choice:
        case "+":add(a, b)
        case "-":sub(a, b)
        case "*":mult(a, b)
        case "/":div(a, b)
        case "0":break
        case _:
            print("Invalid choice")