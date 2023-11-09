# Neuron in the network.
import math

class Node:
    def __init__(self, nodeID) -> None:
        self.nodeID = nodeID

        self.bias = 1
        self.sum = 0

    def _sigmoid(self):
        return 1.0 / (1.0 + math.exp(-(self.sum + self.bias)))
    
    def output()