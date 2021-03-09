import numpy as np

__all__ = ["newton_polyn"]


def _find_coef(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    n = x.size
    q = np.zeros((n, n - 1))
    # print(f"x = {x}\ny = {y}\nq = {q}")
    q = np.concatenate((y[:, None], q), axis=1)
    # print(f"q after: {q}")

    for i in range(1, n):
        for j in range(1, i + 1):
            q[i, j] = (q[i, j - 1] - q[i - 1, j - 1]) / (x[i] - x[i - j])

    return q.diagonal(), n


def newton_polyn(x_data: np.ndarray, y_data: np.ndarray, x: float) -> np.float64:
    f, n = _find_coef(x_data, y_data)

    p = f[0]
    for i in range(1, n):
        _tmp = 1
        for j in range(0, i):
            _tmp *= (x - x_data[j])
        p += _tmp * f[i]

    return p

def bilinear_interp(x_args, y_args, z: np.ndarray, point: tuple):
    f = []
    # print("Z = \n", z)
    for i, y in zip(range(len(y_args)), y_args):
        # print(f"i = {i}, y = {y}")
        # print(f"x: {x_args}, z: {z[i, :]}")
        f.append(newton_polyn(x_args, z[i, :], point[0]))

    answer = newton_polyn(y_args, np.copy(f), point[1])

    return answer

