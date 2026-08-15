# Question 4: Iterative Deepening Search
# Shakti Raj Devkota

class IDSGraph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dls_for_ids(self, start, goal, depth_limit):
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
        
        return dls_helper(start, goal, depth_limit, [])
    
    def ids(self, start, goal, max_depth=100):
        for depth in range(max_depth + 1):
            path = self.dls_for_ids(start, goal, depth)
            if path and path != 'CUTOFF':
                return path, depth
            if path != 'CUTOFF':
                return None, -1
        return None, -1


if __name__ == "__main__":
    try:
        n = int(input("Enter number of nodes: "))
        m = int(input("Enter number of edges: "))
        
        g = IDSGraph()
        
        for i in range(m):
            edge = input(f"Enter edge {i+1} (u v): ").split()
            u, v = int(edge[0]), int(edge[1])
            g.add_edge(u, v)
        
        start = int(input("Enter start node: "))
        goal = int(input("Enter goal node: "))
        max_depth = int(input("Enter maximum depth: "))
        
        if start not in g.graph or goal not in g.graph:
            print("Start or goal node not in graph.")
        else:
            path, found_depth = g.ids(start, goal, max_depth)
            if path:
                print(f"Path from {start} to {goal}: {path}")
                print(f"Found at depth: {found_depth}")
            else:
                print(f"No path found from {start} to {goal} within depth {max_depth}.")
    except Exception as e:
        print(f"Error: {e}")
