import sys
from typing import List

import cv2 as cv
from numpy import ndarray

from filter_strategy import blur_strategy, median_blur_strategy, Filter
from window import Window

#  Global Variables     # TODO move this configuration to a separate file
DELAY_CAPTION: int = 1500
DELAY_IMAGE: int = 2000
DELAY_BLUR: int = 180
MAX_KERNEL_LENGTH: int = 31
WINDOW_NAME: str = 'Smoothing Demo'
DEFAULT_IMAGE: str = '../data/uniform-plus-saltpepr.tif'
FILTERS: List[Filter] = [
    {'alias': 'mean', 'name': 'Mean Blur', 'strategy': blur_strategy},
    {'alias': 'median', 'name': 'Median Blur', 'strategy': median_blur_strategy},
]
DEFAULT_FILTER: Filter = FILTERS[1]  # median
CONFIG = [DEFAULT_IMAGE, DEFAULT_FILTER, DELAY_BLUR]


def run(window: Window, filter_type: Filter) -> None:
    cv.namedWindow(WINDOW_NAME, cv.WINDOW_AUTOSIZE)

    src_image: ndarray = window.get_src_image()

    # Display original image
    window.display_caption('Original Image')
    window.display_image(src_image, DELAY_IMAGE)

    # Applying the filters
    window.display_filter(filter_type.get('name'), filter_type.get('strategy'), src_image)

    #  Done
    window.display_caption('Done!')


def load_args(argv: list[str]) -> list[str]:
    for i, arg in enumerate(argv):
        if i == 1:  # filter
            filter_result = list(filter(lambda f: f.get('alias') == arg, FILTERS))
            if len(filter_result) == 0:
                raise Exception('Filter strategy does not exists!')
            else:
                CONFIG[i] = filter_result[0]
        elif i == 2:  # delay
            CONFIG[i] = int(arg)
        else:
            CONFIG[i] = arg

    return CONFIG


# TODO use that webapp to improve the readme

if __name__ == "__main__":  # TODO impl passing of value by the print
    argv: list[str] = sys.argv[1:]
    filename, filter_type, delay_blur = load_args(argv)

    window = Window(
        window_name=WINDOW_NAME,
        filename=filename,
        max_iterations=MAX_KERNEL_LENGTH,
        delay_caption=DELAY_CAPTION,
        delay_blur=delay_blur
    )

    run(window, filter_type)
