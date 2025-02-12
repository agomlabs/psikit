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

def apply_polarizer(state, orientation='horizontal'):
    """
    Simulates the effect of a polarizer on the photonic qubit state.
    The state is assumed to be in a 2-dimensional polarization basis:
      - |0⟩ represents horizontal polarization.
      - |1⟩ represents vertical polarization.
      
    For a 'horizontal' polarizer, only the horizontal component is passed.
    That is, the polarizer operator is:
    
        P_horizontal = |0><0| = [[1, 0],
                                  [0, 0]]
    
    The function applies this operator to the state and returns a new normalized state.
    If the photon is completely blocked (norm zero), the state remains zero.
    """
    if orientation.lower() == 'horizontal':
        polarizer_operator = np.array([[1, 0],
                                       [0, 0]], dtype=complex)
    elif orientation.lower() == 'vertical':
        polarizer_operator = np.array([[0, 0],
                                       [0, 1]], dtype=complex)
    else:
        raise ValueError("Orientation not supported. Use 'horizontal' or 'vertical'.")
    
    new_vector = np.dot(polarizer_operator, state.vector)
    # Create a new QuantumState (this will normalize automatically)
    new_state = state.__class__(new_vector)
    return new_state

def simulate_photonic_qubit_experiment():
    """
    Simulate a photonic qubit experiment:
    1. Prepare the initial photonic state |0⟩ (horizontal polarization).
    2. Apply the beam splitter gate to create a superposition of paths.
    3. Apply a polarizer (set to horizontal) on the transmission branch.
    4. Perform a measurement to simulate state collapse.
    
    In this simulation, the two basis states represent:
      - |0⟩: Transmission (and horizontal polarization)
      - |1⟩: Reflection (vertical polarization)
    
    The polarizer will filter out the vertical component in the transmission branch.
    
    Returns the measurement outcome.
    """
    # Step 1: Initialize state |0⟩ (horizontal polarization)
    state = QuantumState([1, 0])
    print("Initial state (|0⟩):")
    print(state.vector)
    
    # Step 2: Apply the beam splitter gate
    bs = beam_splitter_gate()
    state.apply_gate(bs)
    print("\nState after Beam Splitter (superposition of paths):")
    print(state.vector)
    
    # Step 3: Apply polarizer (horizontal) to simulate filtering on the transmission branch.
    # In our simple model, the polarizer operator is |0><0|, so applying it will remove any
    # vertical component. (If the photon is entirely vertical, it will be blocked.)
    print("\nApplying horizontal polarizer...")
    state = apply_polarizer(state, orientation='horizontal')
    print("State after polarizer:")
    print(state.vector)
    
    # Step 4: Define projectors for measurement:
    # - Transmission is represented by |0⟩.
    # - Reflection is represented by |1⟩.
    proj_transmission = np.array([[1, 0],
                                  [0, 0]], dtype=complex)
    proj_reflection   = np.array([[0, 0],
                                  [0, 1]], dtype=complex)
    
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
          * Transmission path: includes a polarizer block (set to Horizontal)
            before reaching the Transmission Detector.
          * Reflection path: goes directly to the Reflection Detector.
          
    This function uses Matplotlib to create a schematic diagram.
    """
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(9, 6))

    # Draw the Photon Source
    ax.annotate("Photon Source", xy=(0.1, 0.5), xytext=(0.1, 0.5),
                ha='center', va='center', fontsize=12, color='blue',
                bbox=dict(boxstyle="round", fc="w"))

    # Arrow from Photon Source to Beam Splitter
    ax.arrow(0.15, 0.5, 0.1, 0, head_width=0.02, head_length=0.03, fc='k', ec='k')

    # Draw the Beam Splitter as a rectangle
    bs_rect = plt.Rectangle((0.3, 0.45), 0.1, 0.1, fc='lightgray', ec='black')
    ax.add_patch(bs_rect)
    ax.text(0.35, 0.5, "Beam\nSplitter", ha='center', va='center', fontsize=10)

    # Transmission path (horizontal to the right)
    # Arrow from Beam Splitter to Polarizer
    ax.arrow(0.4, 0.5, 0.1, 0, head_width=0.02, head_length=0.03, fc='k', ec='k')
    # Draw the Polarizer as a rectangle on the transmission path
    polarizer_rect = plt.Rectangle((0.5, 0.45), 0.1, 0.1, fc='lavender', ec='black')
    ax.add_patch(polarizer_rect)
    ax.text(0.55, 0.5, "Polarizer\n(Horizontal)", ha='center', va='center', fontsize=10)
    # Arrow from Polarizer to Transmission Detector
    ax.arrow(0.6, 0.5, 0.1, 0, head_width=0.02, head_length=0.03, fc='k', ec='k')
    ax.annotate("Transmission Detector", xy=(0.75, 0.5), xytext=(0.75, 0.5),
                ha='center', va='center', fontsize=12, color='green',
                bbox=dict(boxstyle="round", fc="w"))

    # Reflection path (vertical upward from Beam Splitter)
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

# For quick testing, you can call the simulation and diagram plot when the module is run directly.
if __name__ == "__main__":
    simulate_photonic_qubit_experiment()
    plot_experiment_diagram()
