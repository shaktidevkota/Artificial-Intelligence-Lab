# Question 4: Tokenization
# Shakti Raj Devkota

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

text = input("Enter a sentence: ")

print("\nWord Tokenization:")
print(word_tokenize(text))

print("\nSentence Tokenization:")
print(sent_tokenize(text))