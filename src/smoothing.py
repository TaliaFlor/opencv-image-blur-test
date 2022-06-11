import sys

import cv2 as cv
from numpy import ndarray

from config import Config
from filter_strategy import blur_strategy, median_blur_strategy, FilterType
from window import Window

#  Global Variables
DELAY_CAPTION: int = 1500
DELAY_IMAGE: int = 2000
DELAY_BLUR: int = 0
DEFAULT_KSIZE: int = 3
MAX_ITERATIONS: int = 3
WINDOW_NAME: str = 'Smoothing Demo'
DEFAULT_IMAGE: str = '../data/uniform-plus-saltpepr.tif'
DEFAULT_FILTERS: list[FilterType] = [
    {'alias': 'mean', 'name': 'Mean Blur', 'strategy': blur_strategy},
    {'alias': 'median', 'name': 'Median Blur', 'strategy': median_blur_strategy},
]
DEFAULT_FILTER: FilterType = DEFAULT_FILTERS[1]  # median
CONFIG = [DEFAULT_IMAGE, DEFAULT_FILTER, DELAY_BLUR]


def run(window: Window, filter_type: FilterType) -> None:
    cv.namedWindow(WINDOW_NAME, cv.WINDOW_AUTOSIZE)

    src_image: ndarray = window.get_src_image()

    # Display original image
    window.display_caption('Original Image')
    window.display_image(src_image, DELAY_IMAGE)

    window.display_filter(filter_type.get('name'), filter_type.get('strategy'), src_image)

    window.display_caption('Done!')


def get_config() -> list:
    config = Config(default_config=CONFIG, default_filters=DEFAULT_FILTERS)
    argv: list[str] = sys.argv[1:]
    if len(argv) > 0:
        return config.load_args(argv)
    else:
        if not config.ask_to_display_config_questions():
            return CONFIG
        else:
            return config.ask_config_questions(DEFAULT_IMAGE, DEFAULT_FILTER, DELAY_BLUR)


# TODO use that webapp to improve the readme

if __name__ == "__main__":
    filename, filter_type, delay_blur = get_config()

    window = Window(
        window_name=WINDOW_NAME,
        filename=filename,
        ksize=DEFAULT_KSIZE,
        max_iterations=MAX_ITERATIONS,
        delay_caption=DELAY_CAPTION,
        delay_blur=delay_blur
    )

    run(window, filter_type)
