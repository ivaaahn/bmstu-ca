import numpy as np
from itertools import product

from settings import PATH_TO_TABLE
from polynomes.newton_polyn import bilinear_interp, newton_polyn
from polynomes.utils import read_table
from polynomes.splines import spline_interp


def main():
    x = float(input('Enter x: '))
    y = spline_interp(x, read_table(PATH_TO_TABLE))


    print(f'f({x}) = {y}')


if __name__ == '__main__':
    np.set_printoptions(precision=3)
    main()
