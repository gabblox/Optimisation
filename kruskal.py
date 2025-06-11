from ShortestSpanningTree import ShortestSpanningTree

class Kruskal(ShortestSpanningTree):
    def __init__(self, graph):
        super().__init__(graph)

    def sort(self):
        edges = []
        n = len(self.graph)
        # Parcourir la matrice pour collecter toutes les arêtes
        for i in range(n):
            for j in range(i + 1, n):
                if self.graph[i][j] != 0:
                    edges.append((self.graph[i][j], i, j))
        return sorted(edges, key=lambda x: x[0])

    def kruskal(self):
        edges = self.sort()
        n = len(self.graph)
        parent = list(range(n))  # Chaque sommet est son propre parent au début
        T = []
        total_weight = 0

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Compression de chemin
            return parent[x]

        for weight, u, v in edges:
            root_u = find(u)
            root_v = find(v)
            
            if root_u != root_v:  # Si pas de cycle
                parent[root_v] = root_u  # Union directe
                T.append((u, v))
                total_weight += weight

        return T, total_weight