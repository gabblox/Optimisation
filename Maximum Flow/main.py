import numpy as np
from FordFulkerson import FordFulkerson

# Créer un graphe simple avec 6 sommets (0 à 5)
# où 0 est la source et 5 est le puits
graph = np.array([
    [0, 16, 13, 0, 0, 0],   # Capacités depuis le sommet 0 (source)
    [0, 0, 10, 12, 0, 0],   # Capacités depuis le sommet 1
    [0, 4, 0, 0, 14, 0],    # Capacités depuis le sommet 2
    [0, 0, 9, 0, 0, 20],    # Capacités depuis le sommet 3
    [0, 0, 0, 7, 0, 4],     # Capacités depuis le sommet 4
    [0, 0, 0, 0, 0, 0]      # Capacités depuis le sommet 5 (puits)
])

# Créer une instance de FordFulkerson
ff = FordFulkerson(graph)

# Calculer le flot maximum
source = 0
sink = 5
max_flow = ff.max_flow(source, sink)

print(f"Graphe des capacités:")
for i in range(len(graph)):
    print(f"Depuis le sommet {i}: {graph[i]}")

print(f"\nFlot maximum de {source} à {sink}: {max_flow}")

# Obtenir la matrice des flots
flows = ff.ford_fulkerson(source, sink)
print("\nMatrice des flots:")
for i in range(len(flows)):
    print(f"Depuis le sommet {i}: {flows[i]}")