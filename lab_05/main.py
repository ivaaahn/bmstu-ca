from math import pi

from plot import plot
import solve


def main():
    all_n, all_m = [], []
    methods1, methods2 = [], []
    values = []

    go_on = 'y'
    while go_on == 'y':
        all_n.append(int(input("Введите N: ")))
        all_m.append(int(input("Введите M: ")))

        p = float(input("Введите параметр (тау): "))

        methods1.append(solve.Method(
            int(input('Выберите "внешний" метод интегрирования: (0 - Гаусс, 1 - Симпсон): '))))

        methods2.append(solve.Method(
            int(input('Выберите "внутренний" метод интегрирования: (0 - Гаусс, 1 - Симпсон): '))))

        lm = [[0, pi / 2], [0, pi / 2]]

        values.append(solve.Calculator(
            lm, [all_n[-1], all_m[-1]], [methods1[-1], methods2[-1]]))

        print(f'Результат (тау = {p:.2f}): {values[-1](p):.7f}')

        go_on = input("Продолжить работу? [y/n]: ")

    plot(values, all_n, all_m, methods1, methods2)


if __name__ == "__main__":
    main()
