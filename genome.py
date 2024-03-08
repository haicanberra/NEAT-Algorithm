# Basic feedforward neural network.
from node import Node

class Genome:
    def __init__(self, inputSize, outputSize) -> None:

        # self.layers = [ [Layer 0 (first layer)] [Layer 1(last layer)] ], list of Node.
        self.layers = []
        self.connections = []
        self.nodeIDCounter = 0
        self.innoIDCounter = 1

        self.inputSize = inputSize
        self.outputSize = outputSize
        
        # Initialize with input/output layer.
        self._initLayers()

    def _initLayers(self):
        temp = []
        for i in range(self.inputSize):
            temp.append(Node(self.nodeIDCounter, 0))
            self.nodeIDCounter += 1
        self.layers.append(temp)
        temp = []
        for i in range(self.outputSize):
            temp.append(Node(self.nodeIDCounter, 1))
            self.nodeIDCounter += 1
        self.layers.append(temp)
        
    """
    inputs: List of inputs for first layer
    """
    def feedforward(self, inputs):
        assert len(inputs) == self.inputSize

        for i in range(len(self.layers)):
            if i == 0:
                for j in range(len(self.inputSize)):
                    self.layers[i][j].getOutput(inputs[j])



