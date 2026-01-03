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