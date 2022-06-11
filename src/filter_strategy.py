from typing import Callable, TypedDict

import cv2 as cv
from numpy import ndarray

FilterStrategy = Callable[[ndarray, int], ndarray]


class Filter(TypedDict):
    alias: str
    name: str
    strategy: FilterStrategy


def blur_strategy(image: ndarray, index: int) -> ndarray:
    return cv.blur(image, (index, index))


def gaussian_blur_strategy(image: ndarray, index: int) -> ndarray:
    return cv.GaussianBlur(image, (index, index), 0)


def median_blur_strategy(image: ndarray, index: int) -> ndarray:
    return cv.medianBlur(image, index)


def bilateral_filter_strategy(image: ndarray, index: int) -> ndarray:
    return cv.bilateralFilter(image, index, index * 2, index / 2)
