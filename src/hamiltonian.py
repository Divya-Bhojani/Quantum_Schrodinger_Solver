import numpy as np

def infinite_square_well_hamiltonian(D2, hbar: float, m: float) -> np.ndarray:


    H = - ((hbar**2)/(2*m)) * D2
    return H

