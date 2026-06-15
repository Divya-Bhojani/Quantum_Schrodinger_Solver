# Quantum Mechanics Simulation: Numerical Solution of the Schrödinger Equation

> **Status:** Active work in progress
> **Current stage:** Stage 1 complete — Infinite Square Well
> **Next stage:** Stage 2 — Quantum Harmonic Oscillator

This project numerically solves the one-dimensional time-independent Schrödinger equation using finite difference methods and matrix eigenvalue solvers in Python.

The goal is to build a computational physics project that demonstrates quantum mechanics, numerical methods, finite difference methods, linear algebra, eigenvalue problems, and scientific computing in Python.

---

## Project Overview

The time-independent Schrödinger equation in one dimension is

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2}+V(x)\psi(x)=E\psi(x)
$$

The central idea of this project is to convert the continuous differential equation into a discrete matrix eigenvalue problem:

$$
H\vec{\psi}=E\vec{\psi}
$$

where:

* `H` is the Hamiltonian matrix
* `E` gives the allowed energy eigenvalues
* `ψ` gives the corresponding wavefunctions

This allows quantum bound-state problems to be solved numerically using linear algebra.

---

## Current Features

* Constructs the finite-difference second derivative matrix
* Builds the Hamiltonian matrix for the infinite square well
* Solves the Hamiltonian eigenvalue problem
* Computes numerical energy eigenvalues and eigenfunctions
* Normalizes wavefunctions using discrete numerical integration
* Compares numerical energies with analytical infinite square well energies
* Computes analytical infinite square well wavefunctions
* Overlays numerical and analytical wavefunctions
* Plots wavefunctions and probability densities
* Uses Git/GitHub for version control and project organization

---

## Project Roadmap

### Stage 1: Infinite Square Well

* [x] Discretize space
* [x] Construct finite-difference second derivative matrix
* [x] Construct Hamiltonian matrix
* [x] Solve eigenvalue problem
* [x] Normalize wavefunctions
* [x] Compare numerical energies with analytical energies
* [x] Compute analytical wavefunctions
* [x] Overlay numerical and analytical wavefunctions
* [x] Plot probability densities

### Stage 2: Quantum Harmonic Oscillator

* [ ] Build harmonic oscillator potential
* [ ] Add potential energy to the Hamiltonian
* [ ] Compute numerical eigenvalues and eigenfunctions
* [ ] Compare numerical energies with analytical harmonic oscillator energies
* [ ] Plot harmonic oscillator wavefunctions and probability densities

### Stage 3: Finite Potential Well

* [ ] Build finite well potential
* [ ] Compute bound states
* [ ] Visualize tunneling tails
* [ ] Discuss physical meaning of wavefunction leakage into classically forbidden regions

### Stage 4: Double-Well Potential

* [ ] Build double-well potential
* [ ] Study symmetric and antisymmetric states
* [ ] Explore tunneling splitting
* [ ] Connect the results to two-state quantum systems

---

## Numerical Method

The second derivative is approximated using the central finite difference formula:

$$
\frac{d^2\psi}{dx^2}\bigg|*{x_i}
\approx
\frac{\psi*{i+1}-2\psi_i+\psi_{i-1}}{h^2}
$$

where `h` is the grid spacing.

This approximation converts the continuous second derivative operator into a tridiagonal matrix:

$$
D_2 =
\frac{1}{h^2}
\begin{bmatrix}
-2 & 1 & 0 & \cdots & 0 \
1 & -2 & 1 & \cdots & 0 \
0 & 1 & -2 & \cdots & 0 \
\vdots & \vdots & \vdots & \ddots & 1 \
0 & 0 & 0 & 1 & -2
\end{bmatrix}
$$

For the infinite square well, the potential is zero inside the well:

$$
V(x)=0
$$

so the Hamiltonian becomes

$$
H=-\frac{\hbar^2}{2m}D_2
$$

The Hamiltonian eigenvalue problem is then solved numerically:

$$
H\vec{\psi}=E\vec{\psi}
$$

---

## Stage 1: Infinite Square Well

For a particle in a one-dimensional infinite square well of length `L`, the wavefunction satisfies the boundary conditions:

$$
\psi(0)=0
$$

$$
\psi(L)=0
$$

The analytical energy eigenvalues are

$$
E_n=\frac{n^2\pi^2\hbar^2}{2mL^2}
$$

and the analytical wavefunctions are

$$
\psi_n(x)=\sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)
$$

where

$$
n=1,2,3,\dots
$$

The numerical results are compared against these analytical solutions to validate the finite difference method.

---

## Wavefunction Normalization

The continuous normalization condition is

$$
\int |\psi(x)|^2 dx = 1
$$

After discretizing space, the integral is approximated as a sum:

$$
\sum_i |\psi_i|^2h \approx 1
$$

where `h` is the grid spacing.

Although NumPy returns eigenvectors normalized as ordinary vectors,

$$
\sum_i \psi_i^2 = 1
$$

the wavefunctions must be rescaled so that they satisfy the physical normalization condition.

---

## Repository Structure

```text
quantum-schrodinger-solver/
│
├── main.py
├── README.md
├── requirements.txt
│
├── src/
│   ├── __init__.py
│   ├── operators.py
│   ├── hamiltonian.py
│   ├── solver.py
│   ├── analytic.py
│   └── plots.py
│
├── figures/
│
└── tests/
```

---

## File Descriptions

### `main.py`

Runs the Stage 1 infinite square well simulation.

It performs the full workflow:

1. Takes user inputs for grid size, well length, reduced Planck constant, and mass
2. Constructs the finite-difference second derivative matrix
3. Builds the Hamiltonian matrix
4. Solves the eigenvalue problem
5. Normalizes the wavefunctions
6. Compares numerical and analytical energies
7. Plots numerical and analytical wavefunctions

### `src/operators.py`

Contains finite-difference operator construction.

Current function:

* `second_derivative_matrix(N, h)`

### `src/hamiltonian.py`

Contains Hamiltonian construction.

Current function:

* `infinite_square_well_hamiltonian(D2, hbar, m)`

### `src/solver.py`

Contains eigenvalue-solving and wavefunction normalization tools.

Current functions:

* `solve_eigenstates(H)`
* `normalize_wavefunction(wavefunctions, h)`

### `src/analytic.py`

Contains analytical solutions used for validation.

Current functions:

* `infinite_square_well_energy(n, L, hbar, m)`
* `infinite_square_well_wavefunction(n, x, L)`
* `relative_error(true_values, observed_values)`

### `src/plots.py`

Contains plotting functions for wavefunctions and probability densities.

Current function:

* `plot_wavefunctions(x, wavefunctions, L, num_states=5)`

---

## Requirements

This project uses:

* Python
* NumPy
* Matplotlib

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/Divya-Bhojani/quantum-schrodinger-solver.git
```

Navigate into the project folder:

```bash
cd quantum-schrodinger-solver
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the simulation:

```bash
python main.py
```

Example input values:

```text
Enter the number of interior grid points: 100
Enter the length of the well: 1
Enter hbar value: 1
Enter the mass: 1
```

---

## Example Output

For

```text
N = 100
L = 1
hbar = 1
m = 1
```

the first analytical energy values are approximately:

```text
E_1 ≈ 4.934802
E_2 ≈ 19.739209
E_3 ≈ 44.413220
E_4 ≈ 78.956835
E_5 ≈ 123.370055
```

The numerical values should approach these analytical values as the number of grid points increases.

---

## Skills Demonstrated

* Quantum Mechanics
* Computational Physics
* Numerical Methods
* Finite Difference Methods
* Linear Algebra
* Eigenvalue Problems
* Python Programming
* NumPy
* Matplotlib
* Scientific Computing
* Data Visualization
* Git/GitHub Project Organization
* Numerical validation against analytical solutions

---

## Next Steps

The next stage is to extend the solver to the quantum harmonic oscillator by adding the potential

$$
V(x)=\frac{1}{2}m\omega^2x^2
$$

to the Hamiltonian matrix.

This will generalize the project from a zero-potential infinite well to a position-dependent potential system.
