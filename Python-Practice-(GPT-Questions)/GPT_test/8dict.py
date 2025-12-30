# Q1
# Create a dictionary with: name, age, course, Print all keys and values.
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
dict[key] is like the slicing by index in list or tuple it will return the value of
specified key and if the key doen't exists it will throw an error

dict.get(key) is a dictionary method which will do the same task as the slicing but
doesn't throw error if the key not present but returns None
"""



# Q4 Loop through a dictionary and print:
for key in d:
    print(f"{key}: {d.get(key)}") 
    # print(f"{key}: {d[key]}") # both the methode ore possible

# Q5 Predict output:

d = {"a": 1, "b": 2}
d["a"] = 5
print(d)

# {"a": 5, "b": 2}