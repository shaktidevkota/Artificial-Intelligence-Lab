# Question 2: Depth-First Search
# Shakti Raj Devkota

class DFSGraph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs_iterative(self, start):
        visited = set()
        stack = [start]
        traversal = []
        
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                traversal.append(node)
                
                for neighbor in reversed(self.graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return traversal
    
    def dfs_path(self, start, goal):
        visited = set()
        
        def dfs_helper(node, goal, path):
            if node == goal:
                return path + [node]
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    result = dfs_helper(neighbor, goal, path + [node])
                    if result:
                        return result
            return None
        
        return dfs_helper(start, goal, [])


if __name__ == "__main__":
    try:
        n = int(input("Enter number of nodes: "))
        m = int(input("Enter number of edges: "))
        
        g = DFSGraph()
        
        for i in range(m):
            edge = input(f"Enter edge {i+1} (u v): ").split()
            u, v = int(edge[0]), int(edge[1])
            g.add_edge(u, v)
        
        start = int(input("Enter start node: "))
        goal = int(input("Enter goal node: "))
        
        if start not in g.graph or goal not in g.graph:
            print("Start or goal node not in graph.")
        else:
            print(f"DFS Traversal from {start}: {g.dfs_iterative(start)}")
            path = g.dfs_path(start, goal)
            if path:
                print(f"Path from {start} to {goal}: {path}")
            else:
                print(f"No path found from {start} to {goal}.")
    except Exception as e:
        print(f"Error: {e}")
# nodes by going deep into branches before backtracking.
