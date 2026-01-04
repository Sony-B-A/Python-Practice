# '''Write a function that:Takes a sentence Returns:
# number of characters (excluding spaces) number of vowels'''

# '''def val_counts(s):
#     vow_count = 0
#     sent_list = s.split()
#     for ch in s:
#         if ch in "aeiou":
#             vow_count += 1
#     return vow_count, len(sent_list)

# sentence = input("Enter a sentence: ")
# v, l = val_counts(sentence.lower())
# print(f"the sentence has {l} words and {v} vowels")'''



# '''✅ TEST 2 — List + Function

# Write a function that:

# Takes a list of numbers

# Returns a new list containing:

# only numbers divisible by 3'''

# def nums(nl):
#     new = []
#     for num in nl:
#         if num % 3 == 0:
#             new.append(num)
#     return new
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
# print(f"3 multipliers from list are: {nums(num_list)}")


# ✅ TEST 3 — Tuple + Concept

data = ("Sangeeta", [78, 82, 91, 88])
l = len(data[1])
avg_marks = sum(data[1])/l
print(f"{data[0]}'s average marks is: {avg_marks}")

# Explain (in a comment) why modifying the list inside the tuple is allowed
# though tuple is immutable, its elements that are mutable can be modifiable
# in this case tuple (data) has a list in it's 1st index and as the list is mutable we can modify it
# sum() doesn't modify that

# ✅ TEST 4 — Dictionary + Logic
info = {
    "Phy":91,
    "che":93,
    "math":96,
    "bio":96
}

def fxn(i):
    mini = min(i.values())
    for sub in i:
        if(i.get(sub) == mini):
            return sub, mini
s, low = fxn(info)
print(f"Subject with minimum marks is {s} with the marks {low}")


# ✅ TEST 5 — OOP (Very Important)

class student:
    college = "xyz"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def res(self):
        if(self.marks >= 40 and self.marks <= 100):
            return "pass"
        elif(self.marks >= 0 and self.marks < 40):
            return "fail"
        else:
            return "invalid marks"

s1 = student("A", 79)
s2 = student("B", 39)
s3 = student("c", 102)
print(f"student {s1.name}'s result: {s1.res()}", f"student {s2.name}'s result: {s2.res()}", f"student {s3.name}'s result: {s3.res()}", sep = "\n")