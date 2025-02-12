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
    
    Returns the measurement outcome.
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

def plot_experiment_diagram():
    """
    Plots a diagram of the photonic qubit experiment setup.
    
    The diagram shows:
      - Photon Source on the left.
      - Beam Splitter (as a gray box) in the center.
      - Two output paths:
          * The horizontal (rightward) path labeled 'Transmission Detector'.
          * The vertical upward path labeled 'Reflection Detector'.
          
    This function uses Matplotlib to create a simple schematic diagram.
    """
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 6))

    # Draw the Photon Source
    ax.annotate("Photon Source", xy=(0.1, 0.5), xytext=(0.1, 0.5),
                ha='center', va='center', fontsize=12, color='blue',
                bbox=dict(boxstyle="round", fc="w"))
    # Draw arrow from Photon Source to Beam Splitter
    ax.arrow(0.15, 0.5, 0.1, 0, head_width=0.02, head_length=0.03, fc='k', ec='k')

    # Draw the Beam Splitter as a rectangle
    bs_rect = plt.Rectangle((0.3, 0.45), 0.1, 0.1, fc='lightgray', ec='black')
    ax.add_patch(bs_rect)
    ax.text(0.35, 0.5, "BS", ha='center', va='center', fontsize=10)

    # Draw the Transmission path (horizontal rightwards)
    ax.arrow(0.4, 0.5, 0.25, 0, head_width=0.02, head_length=0.03, fc='k', ec='k')
    ax.annotate("Transmission Detector", xy=(0.7, 0.5), xytext=(0.7, 0.5),
                ha='center', va='center', fontsize=12, color='green',
                bbox=dict(boxstyle="round", fc="w"))

    # Draw the Reflection path (vertical upwards from the beam splitter)
    ax.arrow(0.35, 0.55, 0, 0.2, head_width=0.02, head_length=0.03, fc='k', ec='k')
    ax.annotate("Reflection Detector", xy=(0.35, 0.8), xytext=(0.35, 0.8),
                ha='center', va='center', fontsize=12, color='red',
                bbox=dict(boxstyle="round", fc="w"))

    # Remove axes and set limits
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.title("Photonic Qubit Experiment Setup", fontsize=14)
    plt.show()

# For quick testing, you can call the diagram plot when the module is run directly.
if __name__ == "__main__":
    simulate_photonic_qubit_experiment()
    plot_experiment_diagram()
