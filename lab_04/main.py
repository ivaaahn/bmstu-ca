from os.path import split
import matplotlib.pyplot as plt
import numpy as np
from termcolor import colored

from settings import PATH_TO_TABLE

float_formatter = "{:.2f}".format
np.set_printoptions(formatter={'float_kind':float_formatter})


def matprint(mat, fmt=".2f"):
    col_maxes = [max([len(("{:"+fmt+"}").format(x)) for x in col]) for col in mat.T]
    for x in mat:
        for i, y in enumerate(x):
            print(("{:"+str(col_maxes[i])+fmt+"}").format(y), end="  ")
        print("")

def f(x_arr, coeff):
    res = np.zeros(len(x_arr))
    for i in range(len(coeff)):
        res += coeff[i]*(x_arr**i)
    return res                   

def read_table(filename):
    f = open(filename, "r")
    x, y, ro = [], [], []
    for line in f:
        line = line.split(" ")
        x.append(float(line[0]))
        y.append(float(line[1]))
        ro.append(float(line[2]))
    return x, y, ro

def print_table(x, y, ro):
    length = len(x)
    print("x      y      ro")
    for i in range(length):
        print("%.4f %.4f %.4f" % (x[i], y[i], ro[i]))
    print()

def root_mean_square(x, y, ro, n):
    length = len(x)
    sum_x_n = [sum([x[i]**j*ro[i] for i in range(length)]) for j in range(n*2 -1)]
    sum_y_x_n = [sum([x[i]**j*ro[i]*y[i] for i in range(length)]) for j in range(n)]
    matr = [sum_x_n[i:i+n] for i in range(n)]
    for i in range(n):
        matr[i].append(sum_y_x_n[i])
    print(colored("\nSOURCE:", 'red'))
    matprint(np.array(matr))
    return calc_gauss(matr)

def calc_gauss(matr):
    n = len(matr)
    # приводим к треугольному виду
    for k in range(n):
        for i in range(k+1,n):
            coeff = -(matr[i][k]/matr[k][k])
            for j in range(k,n+1):
                matr[i][j] += coeff*matr[k][j]
    print(colored("\nTRIANGLED:", 'red'))
    matprint(np.array(matr))
    print(colored('===========================', 'yellow'))

    a = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            matr[i][n] -= a[j]*matr[i][j]
        a[i] = matr[i][n]/matr[i][i]
    return a
    

def show(result, all_x, all_y, all_ro):
    t = np.arange(min(all_x), max(all_x)+0.2, 0.02)
    plt.title('Среднеквадратичное приближение.')
    plt.ylabel("y")
    plt.xlabel("x")

    colors = ['k', 'g', 'b', 'y', 'c']

    for a, n in result:
        color = colors.pop()
        plt.plot(t, f(t, a), color=color, label=f'n = {n}')

    for x, y, ro in zip(all_x, all_y, all_ro):
        plt.plot(x, y, 'ro', markersize=ro+5)

    plt.rc('grid', linestyle="-", color='black')
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    file = input('Выберите таблицу: [1/2/3/4]\n')
    x, y, ro = read_table(PATH_TO_TABLE + file + '.txt')

    all_n = list(map(int, input('Введите степени полинома: ').split()))

    print(colored('===========================', 'yellow'))
    print(colored('\tSOURCE TABLE', 'yellow'))
    print(colored('===========================', 'yellow'))


    all_n = [n for n in all_n]

    print_table(x, y, ro)


    print(colored('===========================', 'yellow'))
    print(colored('\tMATRICIES', 'yellow'))
    print(colored('===========================', 'yellow'))


    all_a = [root_mean_square(x, y, ro, n+1) for n in all_n]

    result = list(zip(all_a, all_n))

    print(colored('===========================', 'green'))
    print(colored('\tRESULT', 'green'))
    print(colored('===========================', 'green'))
    
    for a, n in result:
        pr_a = np.array(a)
        print(f'n = {n}\na = {pr_a}')
        print(colored('===========================', 'green'))

    show(result, x, y, ro)


if __name__ == '__main__':
    main()