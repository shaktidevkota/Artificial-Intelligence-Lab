# Question 11: Cryptarithmetic Problem
# Shakti Raj Devkota

from itertools import permutations

word1 = input("Enter first word: ").upper()
word2 = input("Enter second word: ").upper()
result = input("Enter result word: ").upper()

letters = set(word1 + word2 + result)

if len(letters) > 10:
    print("Too many unique letters. Maximum is 10.")
else:
    leading = {word1[0], word2[0], result[0]}
    solution = None

    for digits in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, digits))

        # Leading letters cannot be zero
        if any(mapping[x] == 0 for x in leading):
            continue

        num1 = int("".join(str(mapping[x]) for x in word1))
        num2 = int("".join(str(mapping[x]) for x in word2))
        num3 = int("".join(str(mapping[x]) for x in result))

        if num1 + num2 == num3:
            solution = mapping
            break

    if solution:
        print("\nSolution:")

        for letter in sorted(solution):
            print(letter, "=", solution[letter])

        num1 = int("".join(str(solution[x]) for x in word1))
        num2 = int("".join(str(solution[x]) for x in word2))
        num3 = int("".join(str(solution[x]) for x in result))

        print("\nVerification:")
        print(num1, "+", num2, "=", num3)
    else:
        print("No solution found.")