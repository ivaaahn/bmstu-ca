import numpy as np
import settings
from polynomes.hermite_polyn import hermite_polyn
from polynomes.newton_polyn import newton_polyn, search_root
from polynomes.utils import trim_table, read_table


def main():
    arg_value = float(input('Enter x: '))
    raw_table = read_table(settings.PATH_TO_TABLE)

    print(f'x = {arg_value}')
    print('|n|Newton |Hermite| Root  |')
    for polyn_degree in range(1, 5):
        newton_table = trim_table(raw_table, polyn_degree + 1, arg_value)[:, 0:2]
        hermite_table = trim_table(raw_table, (polyn_degree + 2) // 2, arg_value)

        ans_newton = newton_polyn(newton_table, arg_value)
        ans_hermite = hermite_polyn(hermite_table, arg_value, polyn_degree + 1)
        root = search_root(newton_table)

        print('|{}|{:.5f}|{:.5f}|{:.5f}|'.format(polyn_degree, ans_newton, ans_hermite, root))


if __name__ == '__main__':
    np.set_printoptions(precision=3)
    main() 