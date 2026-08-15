# Question 2: Backpropagation Neural Network
# Shakti Raj Devkota

import math
import random


class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, lr=0.5):
        self.lr = lr
        self.w1 = [[random.uniform(-1, 1) for _ in range(input_size)]
                   for _ in range(hidden_size)]
        self.w2 = [[random.uniform(-1, 1) for _ in range(hidden_size)]
                   for _ in range(output_size)]
        self.b1 = [random.uniform(-1, 1) for _ in range(hidden_size)]
        self.b2 = [random.uniform(-1, 1) for _ in range(output_size)]

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def train(self, X, y, epochs):
        for _ in range(epochs):
            for x, target in zip(X, y):

                # Forward pass
                hidden = [
                    self.sigmoid(sum(x[j] * self.w1[i][j]
                                     for j in range(len(x))) + self.b1[i])
                    for i in range(len(self.w1))
                ]

                output = [
                    self.sigmoid(sum(hidden[j] * self.w2[i][j]
                                     for j in range(len(hidden))) + self.b2[i])
                    for i in range(len(self.w2))
                ]

                # Backpropagation
                oe = [target[i] - output[i] for i in range(len(output))]
                od = [oe[i] * output[i] * (1 - output[i])
                      for i in range(len(output))]

                he = [
                    sum(od[k] * self.w2[k][j] for k in range(len(od)))
                    for j in range(len(hidden))
                ]
                hd = [he[i] * hidden[i] * (1 - hidden[i])
                      for i in range(len(hidden))]

                # Update weights
                for i in range(len(self.w2)):
                    for j in range(len(self.w2[i])):
                        self.w2[i][j] += self.lr * od[i] * hidden[j]
                    self.b2[i] += self.lr * od[i]

                for i in range(len(self.w1)):
                    for j in range(len(self.w1[i])):
                        self.w1[i][j] += self.lr * hd[i] * x[j]
                    self.b1[i] += self.lr * hd[i]

    def predict(self, x):
        hidden = [
            self.sigmoid(sum(x[j] * self.w1[i][j]
                             for j in range(len(x))) + self.b1[i])
            for i in range(len(self.w1))
        ]

        output = [
            self.sigmoid(sum(hidden[j] * self.w2[i][j]
                             for j in range(len(hidden))) + self.b2[i])
            for i in range(len(self.w2))
        ]

        return output


if __name__ == "__main__":
    n = int(input("Enter number of training samples: "))
    f = int(input("Enter number of features: "))

    X = []
    y = []

    print("\nEnter training data:")
    for i in range(n):
        data = list(map(float, input(f"Sample {i + 1}: ").split()))
        X.append(data[:f])
        y.append(data[f:])

    hidden = int(input("Enter number of hidden neurons: "))
    epochs = int(input("Enter number of epochs: "))

    nn = NeuralNetwork(f, hidden, len(y[0]))
    nn.train(X, y, epochs)

    test = list(map(float, input("\nEnter test sample: ").split()))

    print("\nPredicted Output:", nn.predict(test))