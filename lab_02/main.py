import numpy as np
from itertools import product

import settings
from polynomes.newton_polyn import bilinear_interp, newton_polyn
from polynomes.utils import trim_table, read_table


def main():
    x, y = map(float, (input('Enter x, y: ').split()))
    raw_table = read_table(settings.PATH_TO_TABLE)

    for nx, ny in product(range(1, 4), repeat=2):
        x_args, y_args, table = trim_table(
            raw_table, (nx, ny), (x, y))

        answer = bilinear_interp(x_args, y_args, table, (x, y))
        print(f'\nnx, ny = {nx}, {ny}\nz(x, y) = z({x}, {y}) = {answer}\n')


if __name__ == '__main__':
    np.set_printoptions(precision=3)
    main()
