# Question 6: A* Search
# Shakti Raj Devkota

import heapq


class AStarGraph:

    def __init__(self):
        self.graph = {}
        self.heuristics = {}

    def add_edge(self, u, v, cost):
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append((v, cost))

    def set_heuristic(self, node, value):
        self.heuristics[node] = value

    def search(self, start, goal):

        counter = 0

        start_h = self.heuristics[start]

        queue = [
            (start_h, counter, start, [start], 0)
        ]

        best_cost = {start: 0}

        while queue:

            f, _, current, path, g = heapq.heappop(queue)

            if current == goal:
                return path, g

            if g > best_cost.get(current, float("inf")):
                continue

            for neighbor, edge_cost in self.graph[current]:

                new_g = g + edge_cost

                if new_g < best_cost.get(
                    neighbor,
                    float("inf")
                ):

                    best_cost[neighbor] = new_g

                    h = self.heuristics[neighbor]

                    new_f = new_g + h

                    counter += 1

                    heapq.heappush(
                        queue,
                        (
                            new_f,
                            counter,
                            neighbor,
                            path + [neighbor],
                            new_g
                        )
                    )

        return None, -1


# User Input

n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))

graph = AStarGraph()

print("\nEnter edges:")

for i in range(m):

    u, v, cost = map(
        int,
        input(
            f"Enter edge {i + 1} (u v cost): "
        ).split()
    )

    graph.add_edge(u, v, cost)


print("\nEnter heuristic values:")

for i in range(n):

    node, h = map(
        int,
        input(
            f"Enter heuristic for node {i + 1} (node h): "
        ).split()
    )

    graph.set_heuristic(node, h)


start = int(input("\nEnter start node: "))
goal = int(input("Enter goal node: "))


if start not in graph.graph or goal not in graph.graph:

    print("Start or goal node not found.")

else:

    path, cost = graph.search(start, goal)

    if path:

        print("\nA* Search")
        print("Path:", path)
        print("Total cost:", cost)

    else:

        print("\nNo path found.")