from enum import Enum
from math import cos, sin, exp, pi
from scipy.special import roots_legendre
from typing import List, Callable


class Method(Enum):
    GAUSS = 0
    SIMPSON = 1

    def get_func(self) -> Callable:
        interp = {
            Method.GAUSS: Calculator.gauss,
            Method.SIMPSON: Calculator.simpson
        }
        return interp[self]

    def __str__(self) -> str:
        interp = {
            Method.GAUSS: 'Гаусс',
            Method.SIMPSON: 'Симпсон'
        }
        return interp[self]


class Calculator(object):
    def __init__(self, boundaries: List[List[float]], n: int, m: int, methods: List[Method]):
        self.boundaries = boundaries
        self.n = n
        self.m = m
        self.f1 = methods[0].get_func()
        self.f2 = methods[1].get_func()

    def __call__(self, p: float) -> float:
        f = Calculator.__integrated(p)

        def inner(x): return self.f2(
            lambda val1: f(x, val1),
            self.boundaries[1][0],
            self.boundaries[1][1],
            self.m)

        def integ(): return self.f1(
            inner,
            self.boundaries[0][0],
            self.boundaries[0][1],
            self.n)

        return integ()

    @staticmethod
    def __integrated(p: float) -> Callable[[float, float], float]:
        def t(x, y): return 2 * cos(x) / (1 - sin(x) ** 2 * cos(y) ** 2)
        return lambda x, y: 4 / pi * (1 - exp(-p * t(x, y))) * cos(x) * sin(x)

    @staticmethod
    def simpson(f: Callable[[float], float], a: float, b: float, n: int) -> float:
        if n < 3 or n % 2 == 0:
            raise Exception('Некорректное значение N')

        h = (b - a) / (n - 1.0)
        x = a
        res = 0.0

        for _ in range((n - 1) // 2):
            res += f(x) + 4 * f(x + h) + f(x + 2 * h)
            x += 2 * h

        return res * h / 3

    @staticmethod
    def gauss(f: Callable[[float], float], a: float, b: float, n: int) -> float:
        def p2v(p: float, c: float, d: float) -> float:
            return (d + c) / 2 + (d - c) * p / 2

        x, w = roots_legendre(n)
        return sum([(b - a) / 2 * w[i] * f(p2v(x[i], a, b)) for i in range(n)])
