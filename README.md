# OpenCV Image Blur

A simple program to test OpenCV image blur filters `mean (blur)` and `median (medianBlur)`.

Based on [this code](https://docs.opencv.org/4.5.5/dc/dd3/tutorial_gausian_median_blur_bilateral_filter.html) on the
OpenCV documentation. A refactored version can be found in `src/original.py`.

The modified code is on the `src/smoothing.py` file.

The following values can be configured by the user:

- **image:** the full or relative path to the image.
- **filter strategy:** the blur algorithm to be used. Valid values are `mean` or `median`
- **blur delay:** how long does each processing image stays on the screen (ms). Type `0` to disable this feature and
  pass them through a key press.

It can be achived in three diferent ways:

1. By answering the prompt questions
2. By command-line arguments, in the following order: image, filter strategy and blur delay.
3. By using the default values:
    - **image:** `../data/uniform-plus-saltpepr.tif`
    - **filter strategy:** `median`
    - **blur delay:** `180`

Futher configuration can be done through editing the global variables' section of the `src/smoothing.py` file directly.
