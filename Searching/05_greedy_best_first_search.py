# Question 5: Greedy Best-First Search
# Shakti Raj Devkota

import heapq


class GreedyBestFirstGraph:

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

        queue = []
        heapq.heappush(
            queue,
            (self.heuristics[start], start, [start], 0)
        )

        visited = set()

        while queue:

            h, current, path, cost = heapq.heappop(queue)

            if current in visited:
                continue

            visited.add(current)

            if current == goal:
                return path, cost

            for neighbor, edge_cost in self.graph[current]:

                if neighbor not in visited:
                    new_cost = cost + edge_cost

                    heapq.heappush(
                        queue,
                        (
                            self.heuristics[neighbor],
                            neighbor,
                            path + [neighbor],
                            new_cost
                        )
                    )

        return None, -1


# User Input

n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))

graph = GreedyBestFirstGraph()

print("\nEnter edges:")

for i in range(m):

    u, v, cost = map(
        int,
        input(f"Enter edge {i + 1} (u v cost): ").split()
    )

    graph.add_edge(u, v, cost)


print("\nEnter heuristic values:")

for i in range(n):

    node, heuristic = map(
        int,
        input(f"Enter heuristic for node {i + 1} (node h): ").split()
    )

    graph.set_heuristic(node, heuristic)


start = int(input("\nEnter start node: "))
goal = int(input("Enter goal node: "))


if start not in graph.graph or goal not in graph.graph:
    print("Start or goal node not found.")

else:

    path, cost = graph.search(start, goal)

    if path:

        print("\nGreedy Best-First Search")
        print("Path:", path)
        print("Total cost:", cost)

    else:

        print("\nNo path found.")