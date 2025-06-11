import numpy as np

class ShortestPath:
    def __init__(self,graph):
        self.graph = graph
        self.adj_dict = self.adj_dict()
        
    def adj_dict(self):
        adj_dict={}
        for i in range(len(self.graph)):
            for j in range(i, len(self.graph)):
                adj_dict[(i,j)] = self.graph[i][j]
        return adj_dict
    
    
                   