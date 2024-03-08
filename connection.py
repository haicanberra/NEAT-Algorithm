# Connection gene between nodes.
import random

class Connection:
    def __init__(self, inputID, outputID, innovationID) -> None:
        self.inputID = inputID
        self.outputID = outputID
        self.innovationID = innovationID

        self.weight = 1
        self.enabled = True
        
    def mutateWeight(self):
        pass