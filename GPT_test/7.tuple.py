# Q1 Create a tuple and print: Its length Its first element
t = (90, 2, 3, 4, 5, 6)
print(len(t))
print("first element:", t[0])

# Q2 Why does this code give an error?

t = (1, 2, 3)
# t[0] = 10

"Because tuple is immutable, hence cannot add anything using slicing"

# Q3 Unpack this tuple:

student = ("Sangeeta", 19, "AIML")
name, age, course = student
print(f"Name: {name}\nAge: {age}\n/Course: {course}")

# Q4 Predict output and explain:

t = (1, [2, 3])
t[1][0] = 99
print(t)

"""
(1, [99, 3])
"""

# Check if a value exists in a tuple.
t =(1, 3, 5, 2, 9, 87, 67, 9)
print(5 in t)