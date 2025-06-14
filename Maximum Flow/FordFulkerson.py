class FordFulkerson:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)

    def find_path(self, source, sink, flows):
        """Find an augmenting path using BFS"""
        visited = {source}
        paths = {source: []}
        if source == sink:
            return paths[source]
            
        queue = [source]
        while queue:
            u = queue.pop(0)
            for v in range(self.n):
                # Forward edge with remaining capacity
                if v not in visited and self.graph[u][v] - flows[u][v] > 0:
                    visited.add(v)
                    paths[v] = paths[u] + [(u, v, self.graph[u][v] - flows[u][v])]
                    if v == sink:
                        return paths[v]
                    queue.append(v)
                # Backward edge with flow
                elif v not in visited and flows[v][u] > 0:
                    visited.add(v)
                    paths[v] = paths[u] + [(u, v, flows[v][u])]
                    if v == sink:
                        return paths[v]
                    queue.append(v)
        return None

    def ford_fulkerson(self, source, sink):
        flows = [[0] * self.n for _ in range(self.n)]
        
        while True:
            path = self.find_path(source, sink, flows)
            if not path:
                break
                
            # Find minimum residual capacity along the path
            flow = min(cap for _, _, cap in path)
            
            # Update flows along the path
            for u, v, _ in path:
                if self.graph[u][v] > 0:  # Forward edge
                    flows[u][v] += flow
                    flows[v][u] -= flow
                else:  # Backward edge
                    flows[v][u] -= flow
                    flows[u][v] += flow
                    
        return flows

    def max_flow(self, source, sink):
        flows = self.ford_fulkerson(source, sink)
        return sum(flows[source][j] for j in range(self.n))
