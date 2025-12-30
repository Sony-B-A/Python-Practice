# Write a program that:
# Takes a string
# Prints its length
# Prints the first and last 

input_str = "sony" #input("Enter a String: ")
print("length of the entered string is", len(input_str))
print("First character:",input_str[0])
print("Last character:",input_str[-1])


# Q2 Write a function that counts the number of vowels in a string.

def count_vowel(s):
    count = 0
    v = "aeiou"
    for ch in v:
        for char in s:
            if(ch == char):
                count += 1

    return count

s = "Anantha B N"
vow_num = count_vowel(s.lower())
print("The number of vowels in", s, "is:", vow_num)

# Check whether a given string is a palindrome.

s = "Sos".lower()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Given a sentence, replace all spaces with _

sentence = "I am Sony B A, Studying Computer Science and Enginnering and\nEnhancing my knowledge in AI"
print("_".join(sentence)) #I donno How to add "_" at spaces only
# modif = "_".join(sentence)
# print(modif)

sent = ["I", "am", "Sony", "B A", "Studying", "Computer", "Science", "and", "Enginnering", "and", "\nEnhancing", "my", "knowledge", "in", "AIML"]
print("_".join(sent))
#This works


# Using f-string, print:
name = "Sangeeta"
age = 19
course = "AIML"

print(f"Name: {name}\nAge: {19}\nCourse: {course}")


# Q Given a sentence, replace all spaces with _

sentence = "I am Sony B A\nI am studying Bachelor of Engineering"
# rep = sentence.replace(" ", "_")
# print(rep)

print(sentence.replace(" ", "_"))