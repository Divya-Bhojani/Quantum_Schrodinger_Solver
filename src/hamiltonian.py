import numpy as np

def infinite_square_well_hamiltonian(D2, hbar: float, m: float) -> np.ndarray:

    H = - ((hbar**2)/(2*m)) * D2
    return H

def harmonic_oscillator_hamiltonian(D2, V, hbar: float, m: float) -> np.ndarray:

    T = -((hbar ** 2) / (2 * m)) * D2
    V_matrix = np.diag(V)
    H = T + V_matrix
    return H