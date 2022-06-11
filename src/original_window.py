import cv2 as cv
import numpy as np
from numpy import ndarray

from filter_strategy import FilterStrategy


def load_image(filename: str) -> ndarray:
    return cv.imread(filename)


class OriginalWindow:

    def __init__(self, window_name: str, filename: str, max_iterations: int, delay_caption: int,
                 delay_blur: int) -> None:
        self.window_name = window_name
        self.src_image: ndarray = load_image(filename)
        self.max_iterations = max_iterations
        self.delay_caption = delay_caption
        self.delay_blur = delay_blur

    def get_src_image(self) -> ndarray:
        return self.src_image

    def display_image(self, image: ndarray, delay: int = None) -> None:
        cv.imshow(self.window_name, image)
        if delay is None:
            delay = self.delay_blur
        cv.waitKey(delay)

    def display_caption(self, caption: str, delay: int = None) -> None:
        dst_image = np.zeros(self.src_image.shape, self.src_image.dtype)
        rows, cols, _ch = self.src_image.shape
        cv.putText(
            dst_image,
            caption,
            (int(cols / 4), int(rows / 2)),
            cv.FONT_HERSHEY_COMPLEX,
            1,
            (255, 255, 255)
        )

        if delay is None:
            delay = self.delay_caption
        self.display_image(dst_image, delay)

    def display_filter(self, caption: str, filter_strategy: FilterStrategy, image: ndarray,
                       max_iterations: int = None) -> None:
        self.display_caption(caption)

        if max_iterations is None:
            max_iterations = self.max_iterations

        for i in range(1, max_iterations, 2):
            dst_image: ndarray = filter_strategy(image, i)
            self.display_image(dst_image)
