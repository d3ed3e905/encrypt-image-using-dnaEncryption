from PIL import Image
from utils import *

# chaos logistic function init data
FILENAME = "lenna.png"
X0 = 0.25
R = 3.94


def dna_encryption(image):
    # Image size
    W, H = image.size
    print("pixels: {}  width: {} height: {} ".format(W * H, W, H))

    # compute logistic function
    x = logistic_function(X0, R, H, W)

    # compute chaos logistic function
    log_g_bin = compute_g_bin(x)

    # compute threshold function
    f_dna = compute_f(x)

    # Split image into R G B channels
    np_image = np.array(image)
    r, g, b = split_image_to_rgb(np_image)

    # Convert R G B values to binary representation
    r_bin, g_bin, b_bin = int_to_binary([r, g, b])

    # Convert R G B values from binary representation to DNA
    r_dna, g_dna, b_dna = binary_to_dna([r_bin, g_bin, b_bin])

    # Compute DNA addition
    r_s_add = scramble_add(r_dna, f_dna)
    g_s_add = scramble_add(g_dna, f_dna)
    b_s_add = scramble_add(b_dna, f_dna)

    # Compute DNA complement
    r_s_complement, g_s_complement, b_s_complement = get_complement(
        [r_s_add, g_s_add, b_s_add]
    )

    r_s_bin, g_s_bin, b_s_bin = dna_to_binary(
        [r_s_complement, g_s_complement, b_s_complement]
    )

    r_xored_bin = compute_xor(r_s_bin, log_g_bin)
    g_xored_bin = compute_xor(g_s_bin, log_g_bin)
    b_xored_bin = compute_xor(b_s_bin, log_g_bin)

    # Convert R G B from binary representation to int
    r_int, g_int, b_int = binary_to_int([r_xored_bin, g_xored_bin, b_xored_bin])

    # Merge R, G, B to get the image
    np_stack = np.dstack([r_int, g_int, b_int]).astype(np.uint8)
    im = Image.fromarray(np_stack)

    return im


def dna_decryption(image):
    W, H = image.size
    print("pixels: {}  width: {} height: {} ".format(W * H, W, H))

    # compute logistic function
    x = logistic_function(X0, R, H, W)

    # compute chaos logistic function
    log_g_bin = compute_g_bin(x)

    # compute threshold function
    f_dna = compute_f(x)

    # Split image into R G B channels
    np_image = np.array(image)
    r, g, b = split_image_to_rgb(np_image)

    # Convert R G B values to binary representation
    r_bin, g_bin, b_bin = int_to_binary([r, g, b])

    # Get R G B after scrambling
    r_after_s_bin = compute_xor(r_bin, log_g_bin)
    g_after_s_bin = compute_xor(g_bin, log_g_bin)
    b_after_s_bin = compute_xor(b_bin, log_g_bin)

    # Convert R G B values from binary representation to DNA
    r_dna, g_dna, b_dna = binary_to_dna([r_after_s_bin, g_after_s_bin, b_after_s_bin])

    # Compute DNA complement
    r_s_complement, g_s_complement, b_s_complement = get_complement(
        [r_dna, g_dna, b_dna]
    )

    # Compute DNA substraction (same as addition)
    r_before_add_dna = scramble_add(r_s_complement, f_dna)
    g_before_add_dna = scramble_add(g_s_complement, f_dna)
    b_before_add_dna = scramble_add(b_s_complement, f_dna)

    r_bin, g_bin, b_bin = dna_to_binary(
        [r_before_add_dna, g_before_add_dna, b_before_add_dna]
    )

    # Convert R G B from binary representation to int
    r_int, g_int, b_int = binary_to_int([r_bin, g_bin, b_bin])

    # Merge R, G, B to get the image
    np_stack = np.dstack([r_int, g_int, b_int]).astype(np.uint8)
    im = Image.fromarray(np_stack)

    return im


def main():

    # -------------------------------------------------------------------   ENCRYPTION
    file_path = "original/" + FILENAME
    image = Image.open(file_path)
    # image.show("Original")  # uncomment this line to show the image
    encrypted_image = dna_encryption(image)
    encrypted_image.save("encrypted/" + FILENAME)
    encrypted_image.show()

    # -------------------------------------------------------------------   DECRYPTION
    image = Image.open("encrypted/" + FILENAME)
    decrypted_image = dna_decryption(image)
    decrypted_image.save("decrypted/" + FILENAME)
    decrypted_image.show()


if __name__ == "__main__":
    main()
