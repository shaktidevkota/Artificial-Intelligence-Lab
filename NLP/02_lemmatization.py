# Question 2: Lemmatization
# Shakti Raj Devkota

import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet', quiet=True)

lemmatizer = WordNetLemmatizer()

text = input("Enter a sentence: ")

words = text.split()
lemmatized = [lemmatizer.lemmatize(word) for word in words]

print("Original:", text)
print("Lemmatized:", lemmatized)