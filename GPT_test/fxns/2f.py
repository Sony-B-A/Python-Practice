# ✅ TEST 1 — Write a function that returns the bigger number

def large(a, b):
    if (a > b):
        big = a
    elif (a < b):
        big = b
    else:
        big = None
    return big

bigg = large(4, 4)
if (bigg != None):
    print(bigg)
else:
    print('Both the values are equal')

# ✅ TEST 2 — Write a function that counts consonants in a string

def consonants(s):
    # vowels = ['a', 'e', 'i', 'o', 'u']
    cons_count = 0
    for ch in s:
        if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
            cons_count += 0
        else:
            cons_count += 1
    return cons_count

s = "Sony"
s = "Preetham"
count = consonants(s)
print(f"{s} has {count} consonants")

# ✅ TEST 3 — Make a function that checks if a number is even or odd

def check(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

check(4)

# ✅ TEST 4 — Create a function with a default parameter

def fn(city = "Bengaluru"):
    return f"You live in {city}"

city = "Mumbai"
print(fn())

# ✅ TEST 5 — Function that returns BOTH area and perimeter of a rectangle

def rectangle(l, w):
    a = l * w
    p = 2 * (l + w)
    return a, p
l = float(input("Enter length: "))
w = float(input("Enter width: "))
area, peri = rectangle(l, w)
print(f'Rectangle area = {area}', f'Rectangle perimeter = {peri}', sep = '\n')