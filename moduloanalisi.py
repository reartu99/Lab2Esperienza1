import numpy as np


def incertezzadigitale(epsilon, misure, m, dg):
    return np.sqrt(pow(epsilon/100*misure, 2) + pow(m*dg, 2))


def tdc(x1, y1, ex1, ey1):
    return abs(x1-y1)/np.sqrt((pow(ex1, 2) + pow(ey1, 2)))


def line(x, a, b):
    return a * np.array(x) + b

