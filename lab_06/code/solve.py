from typing import List

class Calculator:
    @staticmethod
    def _check_none(value: float):
        return 0 if value is None else value

    @staticmethod
    def __left_inter(y: float, yl: float, h: float) -> float:
        return (y - yl) / h

    @staticmethod
    def left(y: List[float], h: float) -> List[float]:
        res = []

        for i in range(len(y)):
            res.append(None if i == 0
                       else Calculator.__left_inter(y[i], y[i - 1], h))

        return res

    @staticmethod
    def center(y: List[float], h: float) -> List[float]:
        res = []

        for i in range(len(y)):
            res.append(None if i == 0 or i == len(y) - 1
                       else (y[i + 1] - y[i - 1]) / 2 * h)

        return res

    @staticmethod
    def second_runge(y: List[float], h: float, p: float) -> List[float]:
        res, y2h = [], []
        for i in range(len(y)):
            y2h.append(0.0 if i < 2 else (y[i] - y[i - 2]) / (2. * h))

        yh = Calculator.left(y, h)
        for i in range(len(y)):
            res.append(None if i < 2
                       else
                       Calculator._check_none(yh[i]) +
                       (
                               Calculator._check_none(yh[i]) -
                               Calculator._check_none(y2h[i])
                       ) / (2.0 ** p - 1))

        return res

    @staticmethod
    def aligned_vars(x: List[float], y: List[float]) -> List[float]:
        res = []
        for i in range(len(y)):
            res.append(None if i == len(y) - 1
                       else
                       y[i] * y[i] / x[i] / x[i] *
                       Calculator.__left_inter(
                           -1. / y[i + 1], -1. / y[i],
                           -1. / x[i + 1] - -1. / x[i]
                       ))

        return res

    @staticmethod
    def second_left(y: List[float], h: float) -> List[float]:
        res = []
        for i in range(len(y)):
            res.append(None if i == 0 or i == len(y) - 1
                       else (y[i - 1] - 2 * y[i] + y[i + 1]) / (h * h))

        return res

    @staticmethod
    def print_init(txt: str, init: List[float]):
        print(txt)

        for i in init:
            print("{:7.4} ".format(i if i is not None else "none"))

        print()

    @staticmethod
    def print_res(txt: str, res: List[float]):
        print(txt)

        for i in res:
            print("{:7.4} ".format(i if i is not None else "none"))

        print()