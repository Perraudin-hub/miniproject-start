from dataclasses import dataclass
from typing import Tuple
import PIL.Image
import numpy as np
import os

# Type definitions
Image = np.ndarray
Kernel = list[list[float]]
Position = tuple[int, int]
Seam = list[int]

# Constant definitions
Infinity = float("inf")


@dataclass
class PixelData:
    min_energy: int = Infinity
    parent: Position = (-1, -1)


def split_name_ext(filename: str) -> tuple[str, str]:
    """Split a filename (or filepath) into its name or path without the extension, and its and extension separately"""
    dot_position = filename.rfind(".")
    if dot_position == -1:
        return filename, ""
    return filename[:dot_position], filename[dot_position:]


def load_image(filename: str) -> Image:
    """Load an image from a file and returns it as a numpy array"""
    print(">> Reading image from", filename)
    return np.array(PIL.Image.open(filename))


def save_image(img: Image, filename: str) -> None:
    """Save an image to a file"""
    print("<< Writing image to", filename)
    if not is_rgb(img):
        # convert to 0-255 range
        img = np.uint8(img)
    PIL.Image.fromarray(img).save(filename)


def dimensions(img: Image) -> Tuple[int, int]:
    """Return the dimensions of an image as a tuple (height, width)"""
    return img.shape[0], img.shape[1]


def new_image_grey(height: int, width: int) -> Image:
    """Create a new greyscale image with the given dimensions"""
    # int16 is used to hold all uint8 values and negative values,
    # needed for the sobel filter
    return np.zeros((height, width), dtype=np.int16)


def new_image_rgb(height: int, width: int) -> Image:
    """Create a new RGB image with the given dimensions"""
    return np.zeros((height, width, 3), dtype=np.uint8)


def is_rgb(img: Image) -> bool:
    """Return True if the image is RGB, False if it is greyscale"""
    return len(img.shape) == 3


def copy_image(img: Image) -> Image:
    """Return a copy of the given image"""
    return np.copy(img)

def highlight_seam(img: Image, seam: Seam) -> Image:
    """Return a copy of the given image with the given seam highlighted"""
    print("   Highlighting seam...")
    result = copy_image(img)
    highlight_value = (255, 0, 0) if is_rgb(img) else 255
    for row, col in enumerate(seam):
        result[row, col] = highlight_value
    return result


def remove_seam(img: Image, seam: Seam) -> Image:
    """Return a copy of the given image with the given seam removed"""
    print("   Removing seam...")
    height, width = dimensions(img)
    if is_rgb(img):
        result = new_image_rgb(height, width - 1)
    else:
        result = new_image_grey(height, width - 1)
    for row in range(height):
        for col in range(width - 1):
            if col < seam[row]:
                result[row, col] = img[row, col]
            else:
                result[row, col] = img[row, col + 1]
    return result
