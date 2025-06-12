import numpy as np
from ShortestPath import ShortestPath

class Djikstra(ShortestPath):
    def __init__(self, graph):
        super().__init__(graph)
    
    def find_shortest_path1(self, start, end):
        visited = []
        visited.append(start)
        path = [start]
        length = 0
        all_paths = []  # Liste pour stocker tous les chemins possibles
        
        def short_path(visited, path, i, j, length):
            if i == j:  # Si on arrive à destination
                all_paths.append((list(path), length))  # Sauvegarder le chemin et sa longueur
                return
            
            for k in range(len(self.graph)):
                if k not in visited and self.graph[i][k] != 0:
                    # Explorer ce chemin
                    visited.append(k)
                    path.append(k)
                    new_length = length + self.graph[i][k]
                    
                    # Appel récursif
                    short_path(visited, path, k, j, new_length)
                    
                    # Retour en arrière (backtracking)
                    visited.remove(k)
                    path.remove(k)
        
        # Trouver tous les chemins possibles
        short_path(visited, path, start, end, length)
        
        if not all_paths:  # Si aucun chemin n'est trouvé
            return None, float('inf')
        
        # Trouver le chemin le plus court
        best_path, min_length = min(all_paths, key=lambda x: x[1])
        return best_path, min_length
    def find_shortest_path2(self, start, end):
        visited=[start]
        pere={start:start}
        pivot = start
        distance=[float('inf') for i in range(len(self.graph))]
        distance[start] = 0
        while len(visited) < len(self.graph):
            for i in range(len(self.graph)):
                if i not in visited and self.graph[pivot][i] != 0:
                    if distance[pivot] + self.graph[pivot][i] < distance[i]:
                        distance[i] = distance[pivot] + self.graph[pivot][i]
                        pere[i] = pivot
            next_node=None
            min_distance = float('inf')
            for i in range(len(self.graph)):
                if i not in visited and distance[i] < min_distance:
                    min_distance = distance[i]
                    next_node = i
            visited.append(next_node)
            pivot = next_node
        path=[end]
        current=end
        while current != start:
            current = pere[current]
            path.append(current)
        path[::-1]
        return path, distance[end]
            
        

