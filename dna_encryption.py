from readline import get_completer
from PIL import Image
from utils import *

# chaos logistic function init data
X0 = 0.25
R = 3.94


def main():

    # Read a image
    file_path = "original/rb.png"
    image = Image.open(file_path)
    # image.show("Original") # uncomment this line to show the image

    # Image size
    W, H = image.size
    print("pixels: {}  width: {} height: {} ".format(W * H, W, H))

    # compute logistic function
    x = logistic_function(X0, R, H, W)

    # compute chaos logistic function
    log_g_dna = compute_g_dna(x)
    #print(log_g_dna)

    # Split image into R G B channels
    np_image = np.array(image)
    r, g, b = split_image_to_rgb(np_image)

    # Convert R G B values to binary representation
    r_bin, g_bin, b_bin = int_to_binary([r, g, b])

    # Convert R G B values from binary representation to DNA
    r_dna, g_dna, b_dna = binary_to_dna([r_bin, g_bin, b_bin])
    #print(r_dna)

    # Compute DNA addition
    r_s_add = scramble_add(r_dna, log_g_dna)
    g_s_add = scramble_add(g_dna, log_g_dna)
    b_s_add = scramble_add(b_dna, log_g_dna)
    print(r_s_add)
    
    # Compute DNA complement
    r_s_complement, g_s_complement, b_s_complement = get_complement([r_s_add, g_s_add, b_s_add])
    print(r_s_complement)

    # Convert R G B from binary representation to int
    r_int, b_int, g_int = binary_to_int([r_bin, g_bin, b_bin])

    # Merge R, G, B to get the image
    np_stack = np.dstack([r, g, b]).astype(np.uint8)
    im = Image.fromarray(np_stack)
    # im.show() #uncomment this line to show the image


if __name__ == "__main__":
    main()
