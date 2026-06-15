import numpy as np
import os
from src.hamiltonian import infinite_square_well_hamiltonian, harmonic_oscillator_hamiltonian
from src.operators import second_derivative_matrix
from src.solver import solve_eigenstates, normalize_wavefunction
from src.analytic import infinite_square_well_energy, relative_error
from src.plots import plot_wavefunctions
from src.potentials import harmonic_oscillator_potential

"""Inputs For the System"""

N = int(input("Enter the Number of Interior Grid Points:"))
L = float(input("Enter the Length of the Well:"))
hbar = float(input("Enter hbar value:"))
m = float(input("Enter the Mass:"))
omega = float(input("Enter the Angular Frequency:"))
h = L / (N + 1)


"""Operator"""

D2 = second_derivative_matrix(N, h)

"""Hamiltonian"""

H = infinite_square_well_hamiltonian(D2,hbar,m)

"""Eigenstates"""

energies, wavefunctions = solve_eigenstates(H)

"""Normalization"""


wavefunctions = normalize_wavefunction(wavefunctions, h)
check_norm = np.sum(wavefunctions[0]**2) * h

print(f"Normalization check for first wavefunction: {check_norm:.6f}")

"""Wavefunction vs x Plot"""

x = np.linspace(h, L - h, N)

os.makedirs("figures", exist_ok=True)
plot_wavefunctions(x, wavefunctions, L, num_states = 5, save_path="figures/infinite_well_wavefunctions.png")

"""Energy Comparison"""

print("Energy Comparison:")
for i in range(5):
    n = i + 1

    numerical = energies[i]
    analytical = infinite_square_well_energy(n, L, hbar, m)
    error = relative_error(analytical, numerical)

    print(f"n = {n}")
    print(f"Numerical Energy = {numerical:.6f}")
    print(f"Analytical Energy = {analytical:.6f}")
    print(f"Relative Error = {error:.6f}")
    print()

"""Print Data"""

np.set_printoptions(precision=4, suppress=True )
print("Grid Spacing =", h)
print("Second Derivative Matrix D2:")
print(D2)
print("Hamiltonian Matrix H:")
print(H)
print("First 5 Numerical Energies:")
for i in range(5):
    print(f"E_{i+1} = {energies[i]:.6f}")


"""Stage 2 Test: Quantum Harmonic Oscillator"""

print("\nQuantum Harmonic Oscillator Test")

x_min = -5.0
x_max = 5.0
N_ho = 300

x_ho = np.linspace(x_min, x_max, N_ho)
h_ho = x_ho[1] - x_ho[0]

D2_ho = second_derivative_matrix(N_ho, h_ho)
V_ho = harmonic_oscillator_potential(x_ho, m, omega)
H_ho = harmonic_oscillator_hamiltonian(D2_ho, V_ho, hbar, m)

energies_ho, wavefunctions_ho = solve_eigenstates(H_ho)
wavefunctions_ho = normalize_wavefunction(wavefunctions_ho, h_ho)

print("First 5 harmonic oscillator numerical energies:")
for i in range(5):
    print(f"E_{i} = {energies_ho[i]:.6f}")