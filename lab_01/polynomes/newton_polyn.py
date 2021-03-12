import numpy as np


def _find_coef(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    n = x.size
    q = np.zeros((n, n - 1))
    q = np.concatenate((y[:, None], q), axis=1)

    for i in range(1, n):
        for j in range(1, i + 1):
            q[i, j] = (q[i, j - 1] - q[i - 1, j - 1]) / (x[i] - x[i - j])

    return q.diagonal(), n


def newton_polyn(table: np.ndarray, x: float) -> np.float64:
    x_data, y_data = table[:, 0], table[:, 1]
    f, n = _find_coef(x_data, y_data)

    p = f[0]
    for i in range(1, n):
        _tmp = 1
        for j in range(0, i):
            _tmp *= (x - x_data[j])
        p += _tmp * f[i]
    return p


def search_root(raw_table: np.ndarray) -> np.float64:
    x = raw_table[:, 0]
    y = raw_table[:, 1]
    table = np.concatenate((y[:, None], x[:, None]), axis=1)
    return newton_polyn(table, 0.0)
