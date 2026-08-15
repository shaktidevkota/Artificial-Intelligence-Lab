# Question 10: Water Jug Problem
# Shakti Raj Devkota

from collections import deque

jug1 = int(input("Enter capacity of jug 1: "))
jug2 = int(input("Enter capacity of jug 2: "))
target = int(input("Enter target amount: "))

start = (0, 0)
queue = deque([(start, [start])])
visited = {start}

found = False

while queue:
    (a, b), path = queue.popleft()

    if a == target or b == target:
        print("Solution Path:", path)
        print("Steps:", len(path) - 1)
        found = True
        break

    states = []

    # Fill jug 1
    states.append((jug1, b))

    # Fill jug 2
    states.append((a, jug2))

    # Empty jug 1
    states.append((0, b))

    # Empty jug 2
    states.append((a, 0))

    # Pour jug 1 -> jug 2
    amount = min(a, jug2 - b)
    states.append((a - amount, b + amount))

    # Pour jug 2 -> jug 1
    amount = min(b, jug1 - a)
    states.append((a + amount, b - amount))

    for state in states:
        if state not in visited:
            visited.add(state)
            queue.append((state, path + [state]))

if not found:
    print("No solution possible.")