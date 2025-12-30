# Q1
'''Write a function that:
Takes a sentence as input
Extracts all the words
Returns a list of words that start with a vowel'''

sent = "I am learning Python and Artificial Intelligence"
def vow_words(s):
    word_list = s.split()
    v_words = []
    vowels = "aeiouAEIOU"
    for word in word_list:
        for ch in vowels:
            if word.startswith(ch):
                v_words.append(word)
    return v_words
new_list = vow_words(sent)
print(f"Words starting with vowels are: {new_list}")