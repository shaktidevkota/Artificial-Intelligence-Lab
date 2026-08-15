# Question 1: Breadth-First Search
# Shakti Raj Devkota

from collections import deque

class BFSGraph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs_traversal(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        traversal = []
        
        while queue:
            node = queue.popleft()
            traversal.append(node)
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return traversal
    
    def bfs_path(self, start, goal):
        visited = set()
        queue = deque([(start, [start])])
        visited.add(start)
        
        while queue:
            node, path = queue.popleft()
            
            if node == goal:
                return path
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None


if __name__ == "__main__":
    try:
        n = int(input("Enter number of nodes: "))
        m = int(input("Enter number of edges: "))
        
        g = BFSGraph()
        
        for i in range(m):
            edge = input(f"Enter edge {i+1} (u v): ").split()
            u, v = int(edge[0]), int(edge[1])
            g.add_edge(u, v)
        
        start = int(input("Enter start node: "))
        goal = int(input("Enter goal node: "))
        
        if start not in g.graph or goal not in g.graph:
            print("Start or goal node not in graph.")
        else:
            print(f"BFS Traversal from {start}: {g.bfs_traversal(start)}")
            path = g.bfs_path(start, goal)
            if path:
                print(f"Path from {start} to {goal}: {path}")
            else:
                print(f"No path found from {start} to {goal}.")
    except Exception as e:
        print(f"Error: {e}")
