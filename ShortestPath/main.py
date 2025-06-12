import numpy as np
from ShortestPath import ShortestPath
import Djikstra 

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

sp = Djikstra.Djikstra(graph)
# Test du chemin le plus court entre le sommet 0 et 15
path, distance = sp.find_shortest_path(2, 15)
print(f"Chemin le plus court : {path}")
print(f"Distance totale : {distance}")
