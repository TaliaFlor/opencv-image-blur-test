import sys
from typing import List

import cv2 as cv
#  Global Variables
from numpy import ndarray

from filter_strategy import blur_strategy, median_blur_strategy, gaussian_blur_strategy, bilateral_filter_strategy, \
    Filter
from window import Window

DELAY_CAPTION = 1500
DELAY_IMAGE = 2000
DELAY_BLUR = 150
MAX_KERNEL_LENGTH = 31
WINDOW_NAME = 'Smoothing Demo'
DEFAULT_IMAGE = '../data/uniform-plus-saltpepr.tif'
FILTERS: List[Filter] = [
    {'alias': 'homogeneous', 'name': 'Homogeneous Blur', 'strategy': blur_strategy},
    {'alias': 'gaussian', 'name': 'Gaussian Blur', 'strategy': gaussian_blur_strategy},
    {'alias': 'median', 'name': 'Median Blur', 'strategy': median_blur_strategy},
    {'alias': 'bilateral', 'name': 'Bilateral Blur', 'strategy': bilateral_filter_strategy}
]


def run(window: Window) -> None:
    cv.namedWindow(WINDOW_NAME, cv.WINDOW_AUTOSIZE)

    src_image: ndarray = window.get_src_image()

    # Display original image
    window.display_caption('Original Image')
    window.display_image(src_image, DELAY_IMAGE)

    # Applying the filters
    for filter in FILTERS:
        window.display_filter(filter.get('name'), filter.get('strategy'), src_image)

    #  Done
    window.display_caption('Done!')


if __name__ == "__main__":
    argv: list[str] = sys.argv[1:]
    filename = argv[0] if len(argv) > 0 else DEFAULT_IMAGE

    window = Window(
        window_name=WINDOW_NAME,
        filename=filename,
        max_iterations=MAX_KERNEL_LENGTH,
        delay_caption=DELAY_CAPTION,
        delay_blur=DELAY_BLUR
    )

    run(window)
