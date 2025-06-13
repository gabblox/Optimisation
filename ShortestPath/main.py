import numpy as np
from ShortestPath import ShortestPath
import Djikstra 
import BellManFord

# Créer un graphe 16x16 initialement rempli de zéros
graph = np.zeros((16, 16), dtype=int)

# Ajouter des connexions avec leurs poids
# Format: graph[source][destination] = weight
connections = [
    (0, 1, 4), (0, 2, 3), (0, 3, 7),
    (1, 4, 2), (1, 5, 5), (1, 2, 1),
    (2, 5, 8), (2, 6, 3), (2, 3, 2),
    (3, 6, 4), (3, 7, 6),
    (4, 8, 3), (4, 9, 7),
    (5, 9, 2), (5, 10, 5),
    (6, 10, 4), (6, 11, 3),
    (7, 11, 5), (7, 12, 6),
    (8, 13, 4), (8, 14, 2),
    (9, 13, 3), (9, 14, 7),
    (10, 14, 5), (10, 15, 4),
    (11, 15, 6),
    (12, 15, 8),
    (13, 14, 2), (13, 15, 5),
    (14, 15, 3)
]

# Remplir le graphe (graphe non orienté)
for i, j, weight in connections:
    graph[i][j] = weight
    graph[j][i] = weight  # Rendre le graphe symétrique

sp = BellManFord.BellmanFord(graph)
sp1 = Djikstra.Djikstra(graph)

def verify_path(path, graph):
    """Vérifie la validité d'un chemin et calcule sa distance totale"""
    if not path:
        return None
    distance = 0
    for i in range(len(path)-1):
        if graph[path[i]][path[i+1]] == 0:
            return None
        distance += graph[path[i]][path[i+1]]
    return distance

# Graphe de test avec poids négatifs
graph_negatifs = np.array([
    [0, -1, 4, 0],
    [-1, 0, 3, 2],
    [4, 3, 0, -3],
    [0, 2, -3, 0]
])

bf = BellManFord.BellmanFord(graph_negatifs)

# Graphe de test plus grand avec poids négatifs et positifs
graph_large = np.array([
    [0, -1, 4, 0, 0, 8, 0, 2],
    [-1, 0, 3, 2, -2, 0, 0, 0],
    [4, 3, 0, -3, 0, -2, 1, 0],
    [0, 2, -3, 0, 5, 0, 4, 0],
    [0, -2, 0, 5, 0, 1, -4, 3],
    [8, 0, -2, 0, 1, 0, 0, -1],
    [0, 0, 1, 4, -4, 0, 0, 2],
    [2, 0, 0, 0, 3, -1, 2, 0]
])

bf = BellManFord.BellmanFord(graph_large)

# Test de plusieurs chemins
start_points = [0, 2, 5]
end_points = [4, 6, 7]

for start in start_points:
    for end in end_points:
        if start != end:
            print(f"\n=== Chemin de {start} à {end} ===")
            path, dist = bf.find_shortest_path2(start, end)
            print(f"Chemin trouvé : {path}")
            print(f"Distance annoncée : {dist}")
            print(f"Distance vérifiée : {verify_path(path, graph_large)}")

