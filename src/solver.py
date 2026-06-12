import numpy as np

def solve_eigenstates(H: np.ndarray) -> tuple[np.ndarray, np.ndarray]:

    energies, wavefunctions = np.linalg.eigh(H)
    wavefunctions = wavefunctions.T
    return energies, wavefunctions

def normalize_wavefunction(wavefunctions: np.ndarray, h: float) -> np.ndarray:

    norms = np.sum(wavefunctions**2, axis = 1) * h
    wavefunctions = wavefunctions / np.sqrt(norms[:, np.newaxis])
    return wavefunctions




