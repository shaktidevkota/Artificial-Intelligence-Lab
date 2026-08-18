# Question 3: Part-of-Speech Tagging
# Shakti Raj Devkota

import nltk
from nltk import word_tokenize, pos_tag

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)

text = input("Enter a sentence: ")

words = word_tokenize(text)
tags = pos_tag(words)

print("\nWord\tPOS Tag")
print("-" * 20)

for word, tag in tags:
    print(f"{word}\t{tag}")