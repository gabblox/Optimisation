import numpy as np
from abc import ABC, abstractmethod

class ShortestSpanningTree:
    def __init__(self,graph):
        self.graph = graph
        
    @abstractmethod
    def sort(self):
        pass
        
    