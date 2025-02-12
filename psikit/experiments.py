import numpy as np
from .quantum_state import QuantumState
from .quantum_gate import QuantumGate
from .measurement import Measurement

def beam_splitter_gate():
    """
    Returns a QuantumGate representing a beam splitter.
    The beam splitter is modeled as:
        BS = (1/√2) * [[1, 1],
                       [-1, 1]]
    """
    bs_matrix = 1 / np.sqrt(2) * np.array([[1, 1],
                                             [-1, 1]])
    return QuantumGate(bs_matrix)

def simulate_photonic_qubit_experiment():
    """
    Simulate a photonic qubit experiment:
    1. Prepare the initial photonic state |0⟩.
    2. Apply the beam splitter gate to create a superposition.
    3. Perform a measurement to simulate state collapse into either the
       'Transmission' (|0⟩) or 'Reflection' (|1⟩) path.
    """
    # Step 1: Initialize state |0⟩ (e.g., representing horizontal polarization)
    state = QuantumState([1, 0])
    print("Initial state (|0⟩):")
    print(state.vector)
    
    # Step 2: Apply the beam splitter gate
    bs = beam_splitter_gate()
    state.apply_gate(bs)
    print("\nState after Beam Splitter (superposition of paths):")
    print(state.vector)
    
    # Step 3: Define projectors for the two paths
    proj_transmission = np.array([[1, 0],
                                  [0, 0]], dtype=complex)
    proj_reflection   = np.array([[0, 0],
                                  [0, 1]], dtype=complex)
    
    # Perform measurement
    outcome = Measurement.measure(state, [
        ("Transmission", proj_transmission),
        ("Reflection", proj_reflection)
    ])
    
    print("\nMeasurement outcome:")
    print(f"The photon was measured in the '{outcome}' path.")
    return outcome

# If running the experiment directly, uncomment the following lines:
# if __name__ == "__main__":
#     simulate_photonic_qubit_experiment()
