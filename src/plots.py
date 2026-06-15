import matplotlib.pyplot as plt
import numpy as np
from src.analytic import infinite_square_well_wavefunction



def plot_wavefunctions(x: np.ndarray, wavefunctions: np.ndarray, L: float, num_states: int = 5,
                       save_path: str | None = None) -> None:

    plt.figure(figsize=(10, 6))


    for i in range(num_states):
        n = i + 1

        num_psi = wavefunctions[i].copy()
        ana_psi = infinite_square_well_wavefunction(n, x, L)

        if np.dot(num_psi, ana_psi) < 0:
            num_psi = -num_psi

        plt.subplot(2, 1, 1)
        plt.plot(x, num_psi, label = f"Num. n = {n}")
        plt.plot(x, ana_psi, "--", label = f"Ana. n = {n}")

        plt.subplot(2, 1, 2)
        plt.plot(x, wavefunctions[i]**2, label=f"n = {n}")

    plt.subplot(2, 1, 1)
    plt.xlabel("x")
    plt.ylabel(r"$\psi_n(x)$")
    plt.title("Infinite Square Well: First Five Wavefunctions")
    plt.legend(fontsize='small', loc = 'lower left',borderpad=0.15, labelspacing=0.2, handletextpad=0.3, handlelength=1.5,)
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.xlabel("x")
    plt.ylabel(r"$|\psi_n(x)|^2$")
    plt.title("Probability Density")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()

    if save_path is not None:
        plt.savefig(save_path, dpi = 300, bbox_inches='tight')
    plt.show()

def plot_numerical_wavefunctions(x: np.ndarray, wavefunctions: np.ndarray, title: str, num_states: int = 5, save_path: str | None = None) -> None:
    plt.figure(figsize=(10, 6))

    for i in range(num_states):
        n = i

        psi = wavefunctions[i].copy()


        if psi[np.argmax(np.abs(psi))] < 0:
            psi = -psi

        plt.subplot(2, 1, 1)
        plt.plot(x, psi, label=f"n = {n}")

        plt.subplot(2, 1, 2)
        plt.plot(x, psi**2, label=f"n = {n}")

    plt.subplot(2, 1, 1)
    plt.xlabel("x")
    plt.ylabel(r"$\psi_n(x)$")
    plt.title(title)
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.xlabel("x")
    plt.ylabel(r"$|\psi_n(x)|^2$")
    plt.title("Probability Density")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()

    if save_path is not None:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()


