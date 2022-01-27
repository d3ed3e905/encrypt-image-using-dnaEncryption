import numpy as np


def logistic_function(x0, r, w, h):
    n = w * h - 1
    x = [x0]

    for i in range(n):
        x1 = r * x0 * (1 - x0)
        x0 = x1
        x.append(x1)

    return np.array(x).reshape(w, h)


def f(x):
    if 0 < x <= 0.5:
        return 0
    return 1


def g(x):
    return int(100000 * x) % 256
