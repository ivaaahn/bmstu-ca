from settings import PATH_TO_TABLE
from utils import read_table
from splines import spline_interpolation


def main():
    x = float(input('Enter x: '))
    y = spline_interpolation(x, read_table(PATH_TO_TABLE))

    print(f'f({x}) = {y:.3f}')


if __name__ == '__main__':
    main()
