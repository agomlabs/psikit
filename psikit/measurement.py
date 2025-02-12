import random
import numpy as np

class Measurement:
    @staticmethod
    def measure(state, projectors):
        """
        Perform a projective measurement on the given quantum state.

        Args:
            state (QuantumState): The quantum state to measure.
            projectors (list): A list of tuples (label, projector), where each projector is a numpy array.

        Returns:
            The label of the measured outcome.
        """
        probabilities = []
        for label, proj in projectors:
            amplitude = np.vdot(state.vector, np.dot(proj, state.vector))
            probabilities.append((label, np.abs(amplitude) ** 2))
        total_prob = sum(p for _, p in probabilities)
        probabilities = [(label, p / total_prob) for label, p in probabilities]

        r = random.random()
        cumulative = 0.0
        for label, p in probabilities:
            cumulative += p
            if r < cumulative:
                return label
        return probabilities[-1][0]  # Fallback in case of rounding issues
