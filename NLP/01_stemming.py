# Question 1: Stemming
# Shakti Raj Devkota

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

text = input("Enter a sentence: ")

words = text.split()
stemmed = [stemmer.stem(word) for word in words]

print("Original:", text)
print("Stemmed:", stemmed)