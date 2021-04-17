from settings import PATH_TO_TABLE
from polynomes.utils import read_table
from polynomes.splines import spline_interpolation


def main():
    x = float(input('Enter x: '))
    y = spline_interpolation(x, read_table(PATH_TO_TABLE))

    print(f'f({x}) = {y:.3f}')


if __name__ == '__main__':
    main()
