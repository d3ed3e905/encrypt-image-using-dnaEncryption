from PIL import Image
import numpy as np

rule = {"00": "A", "01": "C", "10": "G", "11": "T"}


def split_image_to_rgb(image):
    r = np.array(image[:, :, 0])
    g = np.array(image[:, :, 1])
    b = np.array(image[:, :, 2])
    return r, g, b


def int_to_binary(r, g, b):
    vectorized_int_to_binary = np.vectorize(lambda x: np.binary_repr(x, width=8))

    return (
        vectorized_int_to_binary(r),
        vectorized_int_to_binary(g),
        vectorized_int_to_binary(b),
    )


def binary_to_int(r, g, b):
    vectorized_binary_to_int = np.vectorize(lambda x: int(x, 2))

    return (
        vectorized_binary_to_int(r),
        vectorized_binary_to_int(g),
        vectorized_binary_to_int(b),
    )


def binary_to_dna(r, g, b):
    bin_to_dna = lambda x: "".join(
        list(map(rule.get, [x[0:2], x[2:4], x[4:6], x[6:8]]))
    )

    binary_to_dna = np.vectorize(bin_to_dna)

    return (
        binary_to_dna(r),
        binary_to_dna(g),
        binary_to_dna(b),
    )


def main():

    # Read a image
    file_path = "original/rb.png"
    image = Image.open(file_path)
    # image.show("Original") # uncomment this line to show the image

    # Image size
    W, H = image.size
    print("pixels: {}  width: {} height: {} ".format(W * H, W, H))

    # Split image into R G B channels
    np_image = np.array(image)
    r, g, b = split_image_to_rgb(np_image)

    # Convert R G B values to binary representation
    r_bin, g_bin, b_bin = int_to_binary(r, g, b)
    print(type(r_bin[1][1]))

    # Convert R G B values from binary representation to DNA
    r_dna, g_dna, b_dna = binary_to_dna(r_bin, g_bin, b_bin)

    # Convert R G B from binary representation to int
    r_int, b_int, g_int = binary_to_int(r_bin, g_bin, b_bin)

    # Merge R, G, B to get the image
    np_stack = np.dstack([r, g, b]).astype(np.uint8)
    im = Image.fromarray(np_stack)
    # im.show() #uncomment this line to show the image


if __name__ == "__main__":
    main()
