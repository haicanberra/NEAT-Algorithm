# Basic feedforward neural network.

class Genome:
    def __init__(self, inputSize, outputSize) -> None:
        self.nodes = []
        self.connections = []

        self.inputSize = inputSize
        self.outputSize = outputSize
        