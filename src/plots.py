import matplotlib.pyplot as plt
import numpy as np

def plot_wavefunctions(x: np.ndarray, wavefunctions: np.ndarray, num_states: int = 5) -> None:

    plt.figure(figsize=(10, 6))

    for i in range(num_states):
        n = i + 1

        plt.subplot(2, 1, 1)
        plt.plot(x, wavefunctions[i], label = f"n = {n}")

        plt.subplot(2, 1, 2)
        plt.plot(x, wavefunctions[i]**2, label=f"n = {n}")

    plt.subplot(2, 1, 1)
    plt.xlabel("x")
    plt.ylabel(r"$\psi_n(x)$")
    plt.title("Infinite Square Well: First Five Wavefunctions")
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.xlabel("x")
    plt.ylabel(r"$|\psi_n(x)^2|$")
    plt.title("Probability Density")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()



