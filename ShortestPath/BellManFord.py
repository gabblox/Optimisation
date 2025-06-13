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
    
    def find_shortest_path2(self, start, end):
        n = len(self.graph)
        distance = [float('inf')] * n
        distance[start] = 0
        predecessor = {}
        memo = {}
        
        def d(x, k):
            """
            d_k(x) : longueur minimale des chemins reliant start et x 
            avec au plus k arcs
            """
            # Cas de base
            if k == 0:
                return float('inf') if x != start else 0
                
            # Vérifier mémoïzation
            key = (x, k)
            if key in memo:
                return memo[key]
                
            # Optimisation : si k > n, utiliser le résultat de n
            if k > n:
                return d(x, n)
            
            # Initialiser avec la distance actuelle
            min_dist = distance[x]
            
            # Pour chaque prédécesseur potentiel y de x
            for y in range(n):
                if self.graph[y][x] != 0:  # s'il y a une arête y->x
                    dist_via_y = d(y, k-1)
                    if dist_via_y != float('inf'):
                        new_dist = dist_via_y + self.graph[y][x]
                        if new_dist < min_dist:
                            min_dist = new_dist
                            distance[x] = min_dist  # Mettre à jour la distance
                            predecessor[x] = y      # Mettre à jour le prédécesseur
        
            memo[key] = min_dist
            return min_dist

        # Calculer pour tous les k jusqu'à n
        for k in range(n+1):
            dist = d(end, k)
            # Si on trouve une amélioration, continuer
            if k == n and dist < d(end, n-1):
                continue
    
        # Reconstruction du chemin
        if end not in predecessor:
            return None, float('inf')
            
        path = []
        current = end
        visited = set()
        
        while current != start:
            if current in visited:  # Éviter les boucles infinies
                break
            visited.add(current)
            path.append(current)
            current = predecessor[current]
        path.append(start)
        path.reverse()
        
        return path, distance[end]