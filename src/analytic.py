import numpy as np

def infinite_square_well_energy(n, L, hbar, m):
    analytical = (n**2 * np.pi**2 * hbar**2)/(2 * m * L**2)
    return analytical

def relative_error(true_values, observed_values):
    return np.abs((true_values - observed_values) / true_values) * 100
