# Question 7: Hill Climbing Search
# Shakti Raj Devkota

def hill_climbing(values, start):

    current = start
    path = [current]

    while True:

        current_index = values.index(current)

        neighbors = []

        if current_index > 0:
            neighbors.append(values[current_index - 1])

        if current_index < len(values) - 1:
            neighbors.append(values[current_index + 1])

        if not neighbors:
            break

        best = max(neighbors)

        if best <= current:
            break

        current = best
        path.append(current)

    return path


# User Input

n = int(input("Enter number of values: "))

values = list(
    map(
        int,
        input("Enter values: ").split()
    )
)

if len(values) != n:

    print("Number of values does not match.")

else:

    start = int(input("Enter starting value: "))

    if start not in values:

        print("Starting value not found.")

    else:

        path = hill_climbing(values, start)

        print("Hill Climbing Path:", path)
        print("Local Maximum:", path[-1])