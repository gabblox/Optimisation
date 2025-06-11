import numpy as np
from ShortestPath import ShortestPath

graph = np.array([[0, 1, 2, 0, 0],
                   [1, 0, 0, 3, 0],
                   [2, 0, 0, 1, 0],
                   [0, 3, 1, 0, 4],
                   [0, 0, 0, 4, 0]])

sp = ShortestPath(graph)
