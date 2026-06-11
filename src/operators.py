import numpy as np

def second_derivative_matrix(N: int, h: float) -> np.ndarray:

    if N <= 0 or h <= 0:
        raise ValueError('N and h must be positive')

    main_diagonal = -2 * np.ones(N)
    off_diagonal = np.ones(N - 1)

    D2 = (
        np.diag(main_diagonal)
        + np.diag(off_diagonal, k = 1)
        + np.diag(off_diagonal, k = -1)
    ) / h**2

    return D2
