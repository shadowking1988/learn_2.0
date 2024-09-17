import random
word_list = ["Canada", "America","Baboon", "Camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)