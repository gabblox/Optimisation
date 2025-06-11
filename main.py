from kruskal import Kruskal
import numpy as np

# Créer un graphe d'exemple sous forme de matrice d'adjacence
# 0 représente pas de connexion, les autres valeurs sont les poids des arêtes
graph = np.array([
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
])

# Créer une instance de Kruskal avec notre graphe
kruskal = Kruskal(graph)

# Obtenir l'arbre couvrant minimal
mst = kruskal.kruskal()

print(mst[0])
print("Poids total de l'arbre couvrant minimal:", mst[1])