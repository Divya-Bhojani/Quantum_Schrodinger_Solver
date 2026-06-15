# Quantum Mechanics Simulation: Numerical Solution of the Schrödinger Equation

> **Status:** Active work in progress  
> **Current stage:** Stage 1 complete — Infinite Square Well  
> **Next stage:** Quantum Harmonic Oscillator
> 
This project numerically solves the one-dimensional time-independent Schrödinger equation using finite difference methods and matrix eigenvalue solvers in Python.

## Project Goals

- Discretize the 1D Schrödinger equation
- Construct the Hamiltonian matrix
- Solve eigenvalue problems numerically
- Visualize quantum wavefunctions and energy levels
- Compare numerical results with analytical solutions

## Current Features

- Constructs the finite-difference second derivative matrix
- Builds the Hamiltonian matrix for the infinite square well
- Solves the Hamiltonian eigenvalue problem
- Computes numerical energy eigenvalues and wavefunctions
- Normalizes wavefunctions using discrete numerical integration
- Compares numerical energies with analytical infinite square well energies
- Overlays numerical and analytical wavefunctions
- Plots wavefunctions and probability densities

## Project Roadmap

### Stage 1: Infinite Square Well
- [x] Discretize space
- [x] Construct second derivative matrix
- [x] Construct Hamiltonian matrix
- [x] Solve eigenvalue problem
- [x] Normalize wavefunctions
- [x] Compare numerical and analytical energies
- [x] Plot numerical and analytical wavefunctions

### Stage 2: Quantum Harmonic Oscillator
- [ ] Build harmonic oscillator potential
- [ ] Add potential energy to Hamiltonian
- [ ] Compute numerical eigenvalues and eigenfunctions
- [ ] Compare with analytical energy formula

### Stage 3: Finite Potential Well
- [ ] Build finite well potential
- [ ] Compute bound states
- [ ] Visualize tunneling tails

### Stage 4: Double Well Potential
- [ ] Build double-well potential
- [ ] Study symmetric and antisymmetric states
- [ ] Explore tunneling splitting


## Skills Demonstrated

- Quantum Mechanics
- Computational Physics
- Numerical Methods
- Finite Difference Methods
- Linear Algebra
- Eigenvalue Problems
- Python
- NumPy
- SciPy
- Matplotlib