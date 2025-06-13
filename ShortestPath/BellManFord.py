import numpy as np
import ShortestPath

class BellmanFord(ShortestPath.ShortestPath):
    def __init__(self, graph):
        super().__init__(graph)
        
    def find_shortest_path1(self, start, end):
        n = len(self.graph)
        distance = [float('inf')] * n
        distance[start] = 0
        predecessor = {}
        
        # Relaxation des arcs
        for k in range(n * 2):  # Augmenter le nombre d'itérations pour trouver le vrai plus court chemin
            for u in range(n):
                for v in range(n):
                    if self.graph[u][v] != 0:
                        if distance[u] + self.graph[u][v] < distance[v]:
                            distance[v] = distance[u] + self.graph[u][v]
                            predecessor[v] = u
    
        # Trouver tous les chemins possibles vers end
        def find_all_paths(current, visited, path, total_dist):
            if current == end:
                return [(path[:], total_dist)]
            
            paths = []
            for next_node in range(n):
                if self.graph[current][next_node] != 0 and next_node not in visited:
                    visited.add(next_node)
                    new_dist = total_dist + self.graph[current][next_node]
                    paths.extend(find_all_paths(next_node, visited, path + [next_node], new_dist))
                    visited.remove(next_node)
            return paths
    
        # Trouver tous les chemins possibles
        all_paths = find_all_paths(start, {start}, [start], 0)
        
        # Choisir le chemin avec la plus petite distance
        if not all_paths:
            return None, float('inf')
        
        best_path, min_dist = min(all_paths, key=lambda x: x[1])
        return best_path, min_dist

    """
    def find_shortest_path2(self, start, end):
        n = len(self.graph)
        memo = {}  # Pour la mémoïzation
        predecessor = {}
        
        def d(v, k):
            if k < 0:
                return float('inf')
            if k == 0:
                return 0 if v == start else float('inf')
                
            key = (v, k)
            if key in memo:
                return memo[key]
                
            # Initialiser avec la valeur précédente
            min_dist = d(v, k-1)
            best_pred = predecessor.get(v)
            
            # Essayer d'améliorer en passant par chaque sommet u
            for u in range(n):
                if self.graph[u][v] != 0:  # s'il y a une arête u->v
                    new_dist = d(u, k-1) + self.graph[u][v]
                    if new_dist < min_dist:
                        min_dist = new_dist
                        best_pred = u
                        
            # Mettre à jour le prédécesseur si on a trouvé un meilleur chemin
            if best_pred is not None:
                predecessor[v] = best_pred
                
            memo[key] = min_dist
            return min_dist
        
        # Calculer la plus courte distance avec n-1 arcs maximum
        final_dist = d(end, n-1)
        
        # Si pas de chemin trouvé
        if final_dist == float('inf'):
            return None, float('inf')
        
        # Reconstruction du chemin
        path = []
        current = end
        while current != start:
            if current not in predecessor:
                return None, float('inf')
            path.append(current)
            current = predecessor[current]
        path.append(start)
        path.reverse()
        
        # Calculer la distance réelle le long du chemin
        real_dist = 0
        for i in range(len(path)-1):
            real_dist += self.graph[path[i]][path[i+1]]
        
        return path, real_dist"""
        