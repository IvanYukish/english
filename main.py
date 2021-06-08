import random

with open('top_1000_english_words', 'r') as file:
    words = file.read().split()

with open('top_1000_translation', 'r') as file_translate:
    translation = file_translate.read().split('\n')

some_list = list(zip(words, translation))
so = random.choice(some_list)
print(so)

