# Question 8: Minimax Algorithm
# Shakti Raj Devkota

def minimax(values, maximizing):

    if len(values) == 1:
        return values[0]

    next_level = []

    for i in range(0, len(values), 2):

        if maximizing:
            value = max(values[i], values[i + 1])
        else:
            value = min(values[i], values[i + 1])

        next_level.append(value)

    return minimax(next_level, not maximizing)


# User Input

n = int(input("Enter number of terminal values: "))

values = list(
    map(int, input("Enter values: ").split())
)

if len(values) != n:
    print("Number of values does not match.")

elif n < 2 or (n & (n - 1)) != 0:
    print("Number of values must be a power of 2.")

else:
    result = minimax(values, True)

    print("Minimax Value:", result)