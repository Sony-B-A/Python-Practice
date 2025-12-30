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
like b = a (whatever in a is there in b too) doesn't create a another memory but points to the same memory address where all a's vluse
are in the memory  (I am not good a english bttw)
"""

# Q5 Reverse a list without using reverse().

l = ["Sony", "Sangee", "Aish", "Preethu"]
print("reversed order is:", l[::-1])