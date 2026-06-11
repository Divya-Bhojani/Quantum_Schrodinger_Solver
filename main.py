import numpy as np
from src.operators import second_derivative_matrix

N = int(input("Enter the number of interior grid points:"))
L = float(input("Enter the length of the well:"))
h = L / (N + 1)

D2 = second_derivative_matrix(N, h)

np.set_printoptions(precision=2, suppress=True )
print("Grid Spacing =", h)
print("Second Derivative Matrix D2:")
print(D2)
