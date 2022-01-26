from PIL import Image
import numpy as np


def split_image_to_rgb(image):
    r = np.array(image[:, :, 0])
    g = np.array(image[:, :, 1])
    b = np.array(image[:, :, 2])
    return r, g, b


int_to_binary = lambda x: np.binary_repr(x, width=8)

vectorized_int_to_binary = np.vectorize(int_to_binary)


def main():

    # Read a image
    file_path = "original/rb.png"
    image = Image.open(file_path)
    # image.show("Original")

    # Image size
    W, H = image.size
    print("pixels: {}  width: {} height: {} ".format(W * H, W, H))

    # Split image into R G B channels
    np_image = np.array(image)
    r, g, b = split_image_to_rgb(np_image)

    # Convert R G B values to binary representation
    rb = vectorized_int_to_binary(r)
    print(rb)

    # Merge R, G, B to get the image
    np_stack = np.dstack([r, g, b]).astype(np.uint8)
    im = Image.fromarray(np_stack)
    # im.show()


if __name__ == "__main__":
    main()
