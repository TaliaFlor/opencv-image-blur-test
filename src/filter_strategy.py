from typing import Callable, TypedDict

import cv2 as cv
from numpy import ndarray

FilterStrategy = Callable[[ndarray, int], ndarray]


class FilterType(TypedDict):
    alias: str
    name: str
    strategy: FilterStrategy


def blur_strategy(image: ndarray, ksize: int) -> ndarray:
    return cv.blur(image, (ksize, ksize))


def gaussian_blur_strategy(image: ndarray, ksize: int) -> ndarray:
    return cv.GaussianBlur(image, (ksize, ksize), 0)


def median_blur_strategy(image: ndarray, ksize: int) -> ndarray:
    return cv.medianBlur(image, ksize)


def bilateral_filter_strategy(image: ndarray, ksize: int) -> ndarray:
    return cv.bilateralFilter(image, ksize, ksize * 2, ksize / 2)
