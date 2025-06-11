import ShortestSpanningTree as SST

class Prim(SST.ShortestSpanningTree):
    def __init__(self, graph):
        super().__init__(graph)
    def sort(self):
        # Initialiser le dictionnaire d'adjacence
        adj_dict = {}
        n = len(self.graph)
        
        # Pour chaque sommet i
        for i in range(n):
            adj_dict[i] = []
            # Parcourir tous les autres sommets
            for j in range(n):
                # Si une arête existe (poids non nul)
                if self.graph[i][j] != 0:
                    # Ajouter le tuple (voisin, distance) à la liste des voisins de i
                    adj_dict[i].append((j, self.graph[i][j]))
        
        return adj_dict
    def prim(self):
        visited = []
        T = []
        total_weight = 0
        n = len(self.graph)
        adj_dict = self.sort()
        
        # On commence par le sommet 0
        current = 0
        visited.append(current)
        
        # Tant qu'on n'a pas visité tous les sommets
        while len(visited) < n:
            # Trouver le sommet le plus proche et sa source
            result = self.nearest(adj_dict, visited)
            if result is None:
                break  # Graphe non connexe
                
            next_vertex, current = result
            
            # Trouver le poids de l'arête
            for v, weight in adj_dict[current]:
                if v == next_vertex:
                    total_weight += weight
                    break
                    
            # Ajouter l'arête à l'arbre
            T.append((current, next_vertex))
            visited.append(next_vertex)
    
        return T, total_weight
    def nearest(self, adj_dict, visited):
        min_weight = float('inf')
        nearest_vertex = None
        best_source = None
        
        # Pour chaque sommet déjà visité
        for u in visited:
            # Examiner tous ses voisins
            for v, weight in adj_dict[u]:
                # Si le voisin n'est pas visité et son poids est minimal
                if v not in visited and weight < min_weight:
                    min_weight = weight
                    nearest_vertex = v
                    best_source = u
        
        return nearest_vertex, best_source


