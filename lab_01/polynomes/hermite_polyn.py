import numpy as np


def _find_coef(x: np.ndarray, y: np.ndarray, dy: np.ndarray, n: int) -> np.ndarray:
    q = np.zeros((n, n - 1))
    q = np.concatenate((y[:n, None], q), axis=1)

    k = 0
    for i in range(1, n):
        for j in range(1, i + 1):
            if x[i] == x[i - j]:
                q[i, j] = dy[k]
                k += 1
            else:
                q[i, j] = (q[i, j - 1] - q[i - 1, j - 1]) / (x[i] - x[i - j])
    return q.diagonal()


def hermite_polyn(table: np.ndarray, x: float, numof_params: int) -> np.float64:
    x_data, y_data = np.repeat(table[:, 0], 2), np.repeat(table[:, 1], 2)
    dy_data = table[:, 2]

    n = numof_params
    f = _find_coef(x_data, y_data, dy_data, n)
    p = f[0]

    for i in range(1, n):
        _tmp = 1
        for j in range(0, i):
            _tmp *= (x - x_data[j])
        p += _tmp * f[i]
    return p
