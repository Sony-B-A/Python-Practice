# Q1 Write a function that takes a name and prints:
# Expected o/p: Hello <name>
def greet(name):
    print(f"Hello {name}")
name = "Sony" #input("Enter your name: ")
greet(name)

# Q2 Write a function that returns the square of a number.

def square(num):
    return num ** 2
print("Square of 5 is", square(5))

# Q3 Write a function with default parameter:
#def greet(name="Guest")
def greet(name = "Friends"):
    print("Good mornig", name)
print("Hiii", greet("sony"))
'''the output (greet()) is:
Good mornig Friends
Hiii None
output (greet("sony")) is:
Good mornig Sony
Hiii None
'''

# Q4:
# Write a function to return:sum, average, max of 3 numbers.
def compute(a, b, c): # for (x, y, z)
    print("Sum =",a + b + c)
    print("Average =",(a + b + c)/3)
    print("Maximum value = ",max(a, b, c))
a = 1
b = 3
c = 5
print("Computations are:", compute(1, 3, 5)) # this and
# for (a, b, c) the o/p is
"""Sum = 9
Average = 3.0
Maximum value =  5
Computations are: None
Why the function call is happening befor the preveous stuff
"""

# Q5 Write a function that checks whether number is prime.
#Idont know the logic 
# I think I need to learn basic math right
#its already late night so I am quitting here 9:53pm 
# 28 - 11 - 2025