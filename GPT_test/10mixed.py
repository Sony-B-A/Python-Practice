# Q1 — String + Function

'''Write a function that:
Takes a sentence as input Counts: number of words number of vowels Returns both values'''

def ret_val(sent):
    sent_list = sent.split(" ")
    word_count = 0
    vow_count = 0
    vowels = "aeiou"
    for ch in sent:
        if ch in vowels:
            vow_count += 1
    for word in sent_list:
        word_count += 1

    return word_count, vow_count

s = "I am Sangeeta learning Python basics".lower()
wc, vc = ret_val(s)
print(f"Number of words: {wc}\nNumber of vowels: {vc}")


# Q2 List logic
'''Write a function that:
Takes a list of numbers
Returns a new list containing:
only numbers greater than the average of the list'''

def lst(l):
    print("Actual list:\n", l)
    tot = len(l)
    avg = (sum(l))/tot
    print("Average is:", avg)
    new_lst = []
    for num in l:
        if(num > avg):
            new_lst.append(num)
    return new_lst

ls = [1, 2, 3, 4, 5, 9, 8, 3, 2, 1, 3, 4, 2, 7]
nls = lst(ls)
print(f'new list of numbers greater than average is:\n{nls}')


# Q3 Tuple concept
'''Write a function that:
Calculates the average marks'''

student = ("Sangeeta", [90, 85, 88, 92])
l = len(student[1])
avg_marks = sum(student[1])/l
print(f"Name: {student[0]}\nNumber of subjects: {l}\nAverage marks: {avg_marks}")


# Q4
'''Write a function that:
Finds the subject with highest marks
Returns the subject name'''

marks = {
    "Maths": 90,
    "Physics": 78,
    "Chemistry": 85,
    "English": 88
}

def high(marks):
    mark = marks.values()
    # print(mark)

    print(f"Highest marks is: {max(mark)}", end = " ")
    for sub in marks:
        if(marks.get(sub) == max(mark)):
            return sub
            break # not necessary after return

s = high(marks)
print("in", s)


# Q5 Set + function
'''Write a function that:
Takes two lists as input
Returns a set of common elements'''

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]

def cmn(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    return s1 & s2

cmn_elems = cmn(list1, list2)
print(f"Common elements from\n{list1}\n{list2}\n{cmn_elems}")