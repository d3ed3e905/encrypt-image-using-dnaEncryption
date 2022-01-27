import numpy as np
from dna_data import rule


def split_image_to_rgb(image):
    r = np.array(image[:, :, 0])
    g = np.array(image[:, :, 1])
    b = np.array(image[:, :, 2])
    return r, g, b


def int_to_binary(r, g, b):
    vectorized_int_to_binary = np.vectorize(lambda x: np.binary_repr(x, width=8))

    return list(map(vectorized_int_to_binary, [r, g, b]))


def binary_to_int(r, g, b):
    vectorized_binary_to_int = np.vectorize(lambda x: int(x, 2))

    return list(map(vectorized_binary_to_int, [r, g, b]))


def binary_to_dna(r, g, b):
    bin_to_dna = lambda x: "".join(
        list(map(rule.get, [x[0:2], x[2:4], x[4:6], x[6:8]]))
    )

    to_dna = np.vectorize(bin_to_dna)

    return list(map(to_dna, [r, g, b]))
