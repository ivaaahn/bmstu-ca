from typing import Tuple
import numpy as np
from bisect import bisect
from dataclasses import dataclass

from numpy.lib.polynomial import poly
from polynomes.utils import parse_table


def _get_h(table: np.ndarray, index: int) -> float:
    return table[index, 0] - table[index-1, 0]


def _get_c_coef(table: np.ndarray, index: int):
    def _get_f(i: int) -> float:
        ydelta = lambda i: table[i, 1] - table[i-1, 1]
        return 3 * (ydelta(i) / _get_h(table, i) - ydelta(i-1) / _get_h(table, i-1))

    def _get_eta(eta_prev: float, xi_prev: float, i: int):
        hr, hl = _get_h(table, i), _get_h(table, i-1)
        return (_get_f(i) - hl * eta_prev) / (hl * xi_prev + 2 * (hl + hr))

    def _get_xi(xi_prev: float, i: int):
        hr, hl = _get_h(table, i), _get_h(table, i-1)
        return -hr / (hl * xi_prev + 2 * (hl + hr))

    count: int = len(table)
    xi, eta = np.zeros(count+1), np.zeros(count+1)

    for i in range(1, count):
        xi[i+1] = _get_xi(xi[i], i)
        eta[i+1] = _get_eta(eta[i], xi[i], i)

    print(xi, eta)

    c: float = 0.0
    for i in range(count-1, index+1, -1):
        c = xi[i+1] * c + eta[i+1]

    cr = xi[index+2] * c + eta[index+2]
    cl = xi[index+1] * cr + eta[index+1]
        
    return cl, cr

def _get_a_coef(table: np.ndarray, index) -> None:
    return table[index-1, 1]

def _get_b_coef(table: np.ndarray, cl, cr, index, hi) -> None:
    ydelta = lambda i: table[i, 1] - table[i-1, 1]
    return (ydelta(index)) / hi - hi * (cr + 2 * cl) / 3

def _get_d_coef(cl, cr, hi) -> float:
    return (cr - cl) / (3 * hi)


def _get_coeffs(table: np.ndarray, index, hi) -> Tuple[float, float, float, float, float]:
    cl, cr = _get_c_coef(table, index)
    a = _get_a_coef(table, index)
    b = _get_b_coef(table, cl, cr, index, hi)
    d = _get_d_coef(cl, cr, hi)
    return a, b, cl, d


def spline_interpolation(x: float, table: np.ndarray) -> float:
    index = bisect(table[:, 0], x)
    print(index)
    a,b,c,d = _get_coeffs(table, index, _get_h(table, index))
    dx = x - table[index-1, 0]

    return a + b*dx + c*dx*dx + d*dx*dx*dx



