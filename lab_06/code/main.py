from .solve import Calculator


def main():
    x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    y = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]
    h = 1.0

    Calculator.print_init("X              :", x)
    Calculator.print_init("Y              :", y)
    Calculator.print_res("Onesided       :", Calculator.left(y, h))
    Calculator.print_res("Center         :",
                         Calculator.center(y, h))
    Calculator.print_res("Second Runge   :",
                         Calculator.second_runge(y, h, 1))
    Calculator.print_res("Aligned params :",
                         Calculator.aligned_vars(x, y))
    Calculator.print_res("Second onesided:",
                         Calculator.second_left(y, h))


if __name__ == "__main__":
    main()
