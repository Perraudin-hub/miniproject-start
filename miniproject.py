from miniprojectutils import *


def rgb_to_grey(r: int, g: int, b: int) -> int:
    """Convert an RGB color to a greyscale value."""
    return ...  # TODO


def to_grayscale(img: Image) -> Image:
    """Convert the given image to grayscale."""
    print("   Converting to grayscale...")
    return ...  # TODO


def clamp_index(index: int, length: int) -> int:
    """Return the index, clamped to the range [0, length-1]."""
    return ...  # TODO


def apply_kernel(img_grey: Image, kernel: Kernel) -> Image:
    """Apply a kernel to an image."""
    return ...  # TODO


def smoothen(img_grey: Image) -> Image:
    """Smooth the image using a 3x3 kernel."""
    print("   Smoothening image...")
    kernel_smooth = np.array([
        [1, 1, 1],
        [1, 2, 1],
        [1, 1, 1],
    ]) / 10
    return apply_kernel(img_grey, kernel_smooth)


def sobel(img_grey: Image) -> Image:
    """Apply the Sobel filter to the image."""
    print("   Sobel...")
    kernel_sobel_x = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1],
    ])
    kernel_sobel_y = np.array([
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1],
    ])
    sobel_x = apply_kernel(img_grey, kernel_sobel_x)
    sobel_y = apply_kernel(img_grey, kernel_sobel_y)
    result = np.sqrt(sobel_x * sobel_x + sobel_y * sobel_y)
    return result


def find_seam(img_grey: Image) -> Seam:
    """Find the seam with the lowest energy."""
    print("   Finding seam...")
    return ... # TODO


def seam_carving(img_path: str, num_cols: int) -> None:
    print("---- Seam carving on", img_path, "with", num_cols, "columns ----")
    
    # make a folder with the same name as the image without the extension
    name, ext = split_name_ext(img_path)
    folder = name + os.path.sep
    os.makedirs(folder, exist_ok=True)

    img = load_image(img_path)

    # 1. convert to grayscale
    # img_grey = to_grayscale(img)
    # save_image(img_grey, folder + "grey" + ext)

    # 2. smoothen
    # img_grey = smoothen(img_grey)
    # save_image(img_grey, folder + "smooth" + ext)

    # 3. sobel
    # img_grey = sobel(img_grey)
    # save_image(img_grey, folder + "sobel" + ext)

    # (conversion step)
    # img_grey = np.uint8(img_grey)

    for i in range(num_cols):
        # 4. find seam
        # seam = find_seam(img_grey)

        # 5. highlight seam
        # img_highlight = highlight_seam(img, seam)
        # save_image(img_highlight, folder + f"highlight_{i}" + ext)
        # img_grey_highlight = highlight_seam(img_grey, seam)
        # save_image(img_grey_highlight, folder + f"highlight_{i}_grey" + ext)

        # 6. remove seam from both the color and the grayscale image
        # img = remove_seam(img, seam)
        # save_image(img, folder + f"step_{i}" + ext)
        # img_grey = remove_seam(img_grey, seam)

        pass


if __name__ == "__main__":
    seam_carving("imgs/americascup.jpg", 200)
