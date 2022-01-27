from dna_data import *
import numpy as np

# logistic function
def logistic_function(x0, r, w, h):
    n = w * h - 1
    x = [x0]

    for i in range(n):
        x1 = r * x0 * (1 - x0)
        x0 = x1
        x.append(x1)

    return np.array(x).reshape(w, h)


# threshold function
def compute_f(e):
    vectorized_g = np.vectorize(lambda x: 0 if 0 < x <= 0.5 else 1)

    to_binary = int_to_binary([vectorized_g(e)])
    [to_dna] = binary_to_dna(to_binary)
    return to_dna


# chaos logistic function
def compute_g_bin(e):
    vectorized_g = np.vectorize(lambda x: int(100000 * x) % 256)

    return np.array(int_to_binary(vectorized_g(e)))


# transform data
def split_image_to_rgb(image):
    r = np.array(image[:, :, 0])
    g = np.array(image[:, :, 1])
    b = np.array(image[:, :, 2])
    return r, g, b


def int_to_binary(l):
    vectorized_int_to_binary = np.vectorize(lambda x: np.binary_repr(x, width=8))

    return list(map(vectorized_int_to_binary, l))


def binary_to_int(l):
    vectorized_binary_to_int = np.vectorize(lambda x: int(x, 2))

    return list(map(vectorized_binary_to_int, l))


def binary_to_dna(l):
    bin_to_dna = lambda x: "".join(
        list(map(rule.get, [x[0:2], x[2:4], x[4:6], x[6:8]]))
    )

    to_dna = np.vectorize(bin_to_dna)

    return list(map(to_dna, l))


def dna_to_binary(l):
    dna_to_bin = lambda x: "".join(
        list(map(reversedRule.get, [x[0], x[1], x[2], x[3]]))
    )

    to_bin = np.vectorize(dna_to_bin)

    return list(map(to_bin, l))


def scramble_add(e, f):
    add_dna = lambda x, y: "".join(
        list(map(dnaTable.get, [x[0] + y[0], x[1] + y[1], x[2] + y[2], x[3] + y[3]]))
    )
    compute_addition = np.vectorize(add_dna)
    return np.array(list(map(compute_addition, e, f)))


def get_complement(l):
    c = lambda x: "".join(list(map(dnaComplement.get, [x[0], x[1], x[2], x[3]])))

    complement = np.vectorize(c)

    return list(map(complement, l))


def compute_xor(e, g):
    xor_bin = lambda x, y: "".join(
        list(
            map(
                xorRule.get,
                [
                    x[0] + y[0],
                    x[1] + y[1],
                    x[2] + y[2],
                    x[3] + y[3],
                    x[4] + y[4],
                    x[5] + y[5],
                    x[6] + y[6],
                    x[7] + y[7],
                ],
            )
        )
    )
    xor = np.vectorize(xor_bin)
    return np.array(list(map(xor, e, g)))
