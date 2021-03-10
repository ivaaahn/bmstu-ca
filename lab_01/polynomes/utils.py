import numpy as np


def read_table(path: str) -> np.ndarray:
    data = np.loadtxt(path)
    data = data[data.argsort(axis=0)[:, 0]]
    return data


def print_polyn(f, x_data, n):
    print("The polynomial is:")
    print("P(x)={:+.3f}".format(f[0]), end="")
    for i in range(1, n):
        print("{:+.3f}".format(f[i]), end="")
        for j in range(0, i):
            print("(x{:+.3f})".format(x_data[j] * -1), end="")
    print("")


def trim_table(table: np.ndarray, numof_rows: int, x: float) -> np.ndarray:
    args = table[:, 0]
    length = len(args)

    pos = 0
    while (pos < length and x >= args[pos]):
        pos += 1

    start = pos - numof_rows // 2
    end = pos + numof_rows // 2

    if (start >= 0) and (end <= length):
        if (numof_rows % 2):
            if (end == length) or (abs(x - args[start - 1]) < abs(x - args[end])):
                start -= 1
            else:
                end += 1
        new_table = table[start:end]
    elif start < 0:
        new_table = table[:numof_rows]
    elif end > length:
        new_table = table[length - numof_rows:]

    return new_table
    