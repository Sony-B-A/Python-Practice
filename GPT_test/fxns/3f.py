



# ⭐ Q1. Write a function that returns the smallest number among three numbers.

def smallest(num1, num2, num3):
    return min(num1, num2, num3)
a, b, c = 87, 46, 64
print("Smallest number is", smallest(a, b, c))

# ⭐ Q2. Write a function that counts how many vowels are in a string.

def vow(str):
    count = 0
    for ch in str:
        if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
            count += 1
    return count

st = "I am Sony B A"
print(f"Number of vowels in {st} are {vow(st.lower())}")

# ⭐ Q3. Write a function that returns the factorial of a number.

def fact(num):
    res = 1
    for i in range(1, num + 1):
       res *= i

    return res

print(f"factorial of 5 is {fact(5)}")

# ⭐ Q4. Write a function that checks if a given word is a palindrome.

def pali(str):
    if str == str[::-1]:
        return "PALINDROME"
    else:
        return "Not PALINDROME"

s = "SoS"
print(f"The string {s} is {pali(s)}")


# ⭐ Q5. Write a function that returns the second largest number in a list.

def larg(n):
    l = sorted(n, reverse = True)[1:]
    # n.sort(reverse = True)
    # n = n[1:]
    # return max(n)
    return max(l)

num_list = [2, 8, 4, 9, 2, 7, 3]
print(f"second large number in {num_list} is {larg(num_list)}")