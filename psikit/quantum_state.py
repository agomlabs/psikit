import numpy as np

class QuantumState:
    def __init__(self, vector):
        """Initialize the quantum state with a given state vector."""
        self.vector = np.array(vector, dtype=complex)
        self.normalize()

    def normalize(self):
        norm = np.linalg.norm(self.vector)
        if norm != 0:
            self.vector = self.vector / norm

    def apply_gate(self, gate):
        """Apply a quantum gate (operator) to the state."""
        self.vector = np.dot(gate.matrix, self.vector)
        self.normalize()
