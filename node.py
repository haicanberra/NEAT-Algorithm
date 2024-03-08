# Neuron in the network.
import math

class Node:
    def __init__(self, nodeID, layerID) -> None:
        self.nodeID = nodeID
        self.layerID = layerID

        self.output = 0

    def _sigmoid(self, input):
        return 1.0 / (1.0 + math.exp(-input))
    
    def getOutput(self, input=None, connections=None):
        # First layer
        if input != None:
            self.output = self._sigmoid(input)
        # For all other layers (grab inputs from nodes' output)
        elif connections != None: