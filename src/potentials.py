import numpy as np

def harmonic_oscillator_potential(x: np.ndarray, m: float, omega: float) -> np.ndarray:
    V = (1/2) * m * omega**2 * x**2
    return V