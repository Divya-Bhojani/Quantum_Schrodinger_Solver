import numpy as np
from src.hamiltonian import infinite_square_well_hamiltonian
from src.operators import second_derivative_matrix
from src.solver import solve_eigenstates

N = int(input("Enter the number of interior grid points:"))
L = float(input("Enter the length of the well:"))
hbar = float(input("Enter hbar value:"))
m = float(input("Enter the mass:"))
h = L / (N + 1)

D2 = second_derivative_matrix(N, h)

H = infinite_square_well_hamiltonian(D2,hbar,m)

energies, wavefunctions = solve_eigenstates(H)

np.set_printoptions(precision=4, suppress=True )
print("Grid Spacing =", h)
print("Second Derivative Matrix D2:")
print(D2)
print("Hamiltonian Matrix H:")
print(H)
print("First 5 Numerical Energies:")
for i in range(5):
    print(f"E_{i+1} = {energies[i]:.6f}")