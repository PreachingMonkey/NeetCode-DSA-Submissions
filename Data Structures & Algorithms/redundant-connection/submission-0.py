class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Adjacency list to represent our graph as we build it
        graph = defaultdict(list)
        
        # Helper function to check if a path exists between source and target
        def dfs(source: int, target: int, visited: set) -> bool:
            if source == target:
                return True
                
            visited.add(source)
            
            for neighbor in graph[source]:
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True
                        
            return False

        # Process each edge one by one
        for u, v in edges:
            # If both nodes are already in the graph, check for an existing path
            if u in graph and v in graph:
                visited = set()
                # If a path exists, adding this edge creates a cycle
                if dfs(u, v, visited):
                    return [u, v]
            
            # Otherwise, add the undirected edge to the graph and continue
            graph[u].append(v)
            graph[v].append(u)
            
        return []