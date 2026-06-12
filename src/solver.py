import numpy as np

def solve_eigenstates(H: np.ndarray) -> tuple[np.ndarray, np.ndarray]:

    energies, wavefunctions = np.linalg.eigh(H)
    wavefunctions = wavefunctions.T
    return energies, wavefunctions



