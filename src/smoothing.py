import sys

import cv2 as cv
import numpy as np

#  Global Variables
DELAY_CAPTION = 1500
DELAY_BLUR = 150
MAX_KERNEL_LENGTH = 31
src_image = None
dst_image = None
window_name = 'Smoothing Demo'
default_image = './data/peppers_gray_ruido.bmp'


def main(argv) -> int:
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)

    # Load the source image
    image_name = argv[0] if len(argv) > 0 else default_image
    global src_image
    src_image = cv.imread(cv.samples.findFile(image_name))
    if src_image is None:
        print('Error opening image')
        print(f"Usage: smoothing.py [image_name -- default {default_image}] \n")
        return -1
    if display_caption('Original Image') != 0:
        return 0
    global dst_image
    dst_image = np.copy(src_image)
    if display_dst(DELAY_CAPTION) != 0:
        return 0

    # Applying Homogeneous blur
    if display_caption('Homogeneous Blur') != 0:
        return 0

    for i in range(1, MAX_KERNEL_LENGTH, 2):
        dst_image = cv.blur(src_image, (i, i))
        if display_dst(DELAY_BLUR) != 0:
            return 0

    # Applying Gaussian blur
    if display_caption('Gaussian Blur') != 0:
        return 0

    for i in range(1, MAX_KERNEL_LENGTH, 2):
        dst_image = cv.GaussianBlur(src_image, (i, i), 0)
        if display_dst(DELAY_BLUR) != 0:
            return 0

    # Applying Median blur
    if display_caption('Median Blur') != 0:
        return 0

    for i in range(1, MAX_KERNEL_LENGTH, 2):
        dst_image = cv.medianBlur(src_image, i)
        if display_dst(DELAY_BLUR) != 0:
            return 0

    # Applying Bilateral Filter
    if display_caption('Bilateral Blur') != 0:
        return 0

    for i in range(1, MAX_KERNEL_LENGTH, 2):
        dst_image = cv.bilateralFilter(src_image, i, i * 2, i / 2)
        if display_dst(DELAY_BLUR) != 0:
            return 0

    #  Done
    display_caption('Done!')
    return 0


def display_caption(caption: str):
    global dst_image
    dst_image = np.zeros(src_image.shape, src_image.dtype)
    rows, cols, _ch = src_image.shape
    cv.putText(
        dst_image,
        caption,
        (int(cols / 4), int(rows / 2)),
        cv.FONT_HERSHEY_COMPLEX,
        1,
        (255, 255, 255)
    )
    return display_dst(DELAY_CAPTION)


def display_dst(delay: int) -> int:
    cv.imshow(window_name, dst_image)
    c = cv.waitKey(delay)
    if c >= 0:
        return -1
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
