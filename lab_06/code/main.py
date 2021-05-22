from .solve import Calculator


def main():
    x_values = (1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
    y_values = (0.571, 0.889, 1.091, 1.231, 1.333, 1.412)
    h = 1.0

    Calculator.print_init("X              :", x_values)
    Calculator.print_init("Y              :", y_values)
    Calculator.print_res("1. Односторонняя разностная: ",
                         Calculator.left(y_values, h))
    Calculator.print_res("2. Центральная: ", Calculator.center(y_values, h))
    Calculator.print_res("3. 2-я формала Рунге: ",
                         Calculator.second_runge(y_values, h, 1))
    Calculator.print_res("4. Выравнивающие переменные: ",
                         Calculator.aligned_vars(x_values, y_values))
    Calculator.print_res("5. Вторая разностная:",
                         Calculator.second_left(y_values, h))


if __name__ == "__main__":
    main()
