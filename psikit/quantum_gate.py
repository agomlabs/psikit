import numpy as np

class QuantumGate:
    def __init__(self, matrix):
        """Initialize the quantum gate with a given matrix."""
        self.matrix = np.array(matrix, dtype=complex)
