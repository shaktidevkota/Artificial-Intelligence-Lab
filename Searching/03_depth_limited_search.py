# Question 3: Depth-Limited Search
# Shakti Raj Devkota

class DLSGraph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dls(self, start, goal, limit):
        visited = set()
        
        def dls_helper(node, goal, depth_remaining, path):
            if node == goal:
                return path + [node]
            
            if depth_remaining == 0:
                return 'CUTOFF'
            
            visited.add(node)
            cutoff_occurred = False
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    result = dls_helper(neighbor, goal, depth_remaining - 1, path + [node])
                    if result == 'CUTOFF':
                        cutoff_occurred = True
                    elif result is not None:
                        return result
            
            if cutoff_occurred:
                return 'CUTOFF'
            return None
        
        return dls_helper(start, goal, limit, [])


if __name__ == "__main__":
    try:
        n = int(input("Enter number of nodes: "))
        m = int(input("Enter number of edges: "))
        
        g = DLSGraph()
        
        for i in range(m):
            edge = input(f"Enter edge {i+1} (u v): ").split()
            u, v = int(edge[0]), int(edge[1])
            g.add_edge(u, v)
        
        start = int(input("Enter start node: "))
        goal = int(input("Enter goal node: "))
        limit = int(input("Enter depth limit: "))
        
        if start not in g.graph or goal not in g.graph:
            print("Start or goal node not in graph.")
        else:
            result = g.dls(start, goal, limit)
            if result == 'CUTOFF':
                print(f"Depth limit {limit} reached. No path found within limit.")
            elif result:
                print(f"Path from {start} to {goal} (depth limit {limit}): {result}")
            else:
                print(f"No path found from {start} to {goal}.")
    except Exception as e:
        print(f"Error: {e}")
