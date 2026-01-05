# 🧪 TEST 1 — String + List + Function
class sentence_analyzer:
    def __init__(self, s):
        self.sentence = s
    def long_word(self):
        word_list = self.sentence.split()
        long_word_list = []
        for word in word_list:
            if(len(word) >= 3):
                long_word_list.append(word)

        return long_word_list
sent = input("Enter a sentence: ")
obj = sentence_analyzer(sent)
print(f"This sentence has {len(obj.long_word())} long words (min of 3 char)", f"The long words are: {obj.long_word()}", sep = "\n")
