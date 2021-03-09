import numpy as np
from bisect import bisect


__all__ = ["read_table", "trim_table"]


def read_table(path: str) -> np.ndarray:
    return np.loadtxt(path)


def _trim_axis(args: np.ndarray, table: np.ndarray, count: int, value: float) -> np.ndarray:
    pos = bisect(args, value)
    start, end = pos - count // 2, pos + count // 2
    length = len(args)

    if (start >= 0) and (end <= length):
        if (count % 2):
            if (end == length) or (abs(value - args[start-1]) < abs(value - args[end])):
                start -= 1
            else:
                end += 1
        new_table, args = table[:, start:end], args[start:end]
    elif start < 0:
        new_table, args = table[:, :count], args[:count]
    elif end > length:
        new_table, args = table[:, length - count:], args[length - count:]

    return (args, new_table)


def trim_table(table: np.ndarray, n_coeffs: tuple, point: tuple) -> np.ndarray:
    x_args, y_args = table[0][1:], table[:, 0][1:]
    table = table[1:, 1:]
    nx, ny = n_coeffs
    x, y = point

    x_args, table = _trim_axis(x_args, table, nx + 1, x)
    y_args, table = _trim_axis(y_args, table.transpose(), ny + 1, y)

    return x_args, y_args, table.transpose()
