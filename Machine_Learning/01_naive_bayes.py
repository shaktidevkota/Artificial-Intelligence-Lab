# Question 1: Naive Bayes Classifier
# Shakti Raj Devkota

import math


def probability(x, mean, std):
    if std == 0:
        return 1 if x == mean else 0

    return (1 / (std * math.sqrt(2 * math.pi))) * \
           math.exp(-((x - mean) ** 2) / (2 * std ** 2))


# Input training data
n = int(input("Enter number of training samples: "))
f = int(input("Enter number of features: "))

X = []
y = []

print("\nEnter training data:")

for i in range(n):
    values = list(map(float, input(f"Sample {i + 1}: ").split()))
    X.append(values[:-1])
    y.append(values[-1])

classes = list(set(y))

# Calculate mean and standard deviation
stats = {}

for c in classes:
    class_data = [X[i] for i in range(n) if y[i] == c]

    stats[c] = []

    for j in range(f):
        values = [row[j] for row in class_data]
        mean = sum(values) / len(values)

        variance = sum((x - mean) ** 2 for x in values) / len(values)
        std = math.sqrt(variance)

        stats[c].append((mean, std))


# Input test sample
test = list(map(float, input("\nEnter test sample: ").split()))

scores = {}

for c in classes:

    class_count = y.count(c)
    score = class_count / n

    for j in range(f):
        mean, std = stats[c][j]
        score *= probability(test[j], mean, std)

    scores[c] = score


prediction = max(scores, key=scores.get)

print("\nPredicted Class:", prediction)