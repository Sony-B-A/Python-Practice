# Q1 Create a list of numbers and:
# Print the sum
# Print the maximum number

num_list = [1, 3, 5, 4, 2, 7]
print(sum(num_list))
print(f'Maximum num in list is: {max(num_list)}')

# Q2 Write a function that returns only the even numbers from a list.

def even(n):
    ev_no = []
    for no in n:
        if(no % 2 == 0):
            ev_no.append(no)
    return ev_no

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"even numbers are: {even(num)}")

# Q3 Remove duplicate elements from a list.

l = [1, 3, 2, 6, 2, 3, 9, 5, 1, 2, 3, 2, 1, 7, 5, 4]

st = set(l)
print(st)

l = list(st)

print(l)
# Q4

a = [1, 2, 3]
b = a
b.append(4)
print(a)

"""
For this one the output is [1, 2, 3, 4]
because even though we create another varialble which simply carries the another variable's values
like b = a (whatever in a is there in b too) doesn't create a another memory but points to the same
memory address where all a's vluse are in the memory  (I am not good at english btw)
"""

# Q5 Reverse a list without using reverse().

l = ["Sony", "Sangee", "Aish", "Preethu"]
print("reversed order is:", l[::-1])






#TUPLE

# Q1 Create a tuple and print: Its length Its first element
t = (90, 2, 3, 4, 5, 6)
print(len(t))
print("first element:", t[0])

# Q2 Why does this code give an error?

t = (1, 2, 3)
# t[0] = 10

"Because tuple is immutable, hence cannot add anything using slicing (item assignment)"

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

# Q5 Check if a value exists in a tuple.
t =(1, 3, 5, 2, 9, 87, 67, 9)
print(5 in t)




#DICTIONARY

# Q1 Create a dictionary with: name, age, course, Print all keys and values.
d = {
"name": "Sangeeta",
"age": 19,
"course": "AI&ML"
}
print(d.keys())
print(d.values())
print(d.items())

# Q2 Add a new key marks to an existing dictionary.
d.update({"marks": 93.667})
print(d)

# Q3 Difference between:
# dict[key]
# dict.get(key)
"""
dict[key] is like the (key access) slicing by index in list or tuple it will return the value of
specified key and if the key doen't exists it will throw an error

dict.get(key) is a dictionary method which will do the same task as the slicing but
doesn't throw error if the key not present but returns None
"""



# Q4 Loop through a dictionary and print:
for key in d:
    print(f"{key}: {d.get(key)}") 
    # print(f"{key}: {d[key]}") # both the method are possible

# Q5 Predict output:

d = {"a": 1, "b": 2}
d["a"] = 5
print(d)

# {"a": 5, "b": 2}







#SET
# Q1 Create a set from a list with duplicate values.
lst = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 6, 6, 7]
st = set(lst)
print(st)

# Q2 Why don’t sets allow duplicates?
'''
I know sets don't allow duplicates but don't know why??? You answer this.. 
:)
'''

# Q3 Find common elements between two sets.
a = {1, 2, 3, 4, 5, 6}
b = {5, 6, 7, 8, 9} 
print(a.intersection(b))
# or
print(a & b)

# Q4 Difference between:
# a.remove(8) #KeyError: 8
a.discard(8)
print(a)
'''
here remove method raises an error if the element doesn't exists
while dicard does the same task but doesn't raises an error if the element doesn't exists
so both removes the element from original set and returns nothing
'''

# Q5 Why does this give an error?

# s = {1, [2, 3]}
#set should not have mutable datatype as its element 