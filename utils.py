import numpy as np
from matplotlib.path import Path as MplPath

def apply_mask(im, mask):
    """
    :param im: image np.array
    :param mask: np.array of the same size to mask
    :return: return masked image
    """
    im[mask != 1] = 0
    return im


def get_mask_poly_verts(image, poly_verts, on_original=True):
    """
    :param image: np.array of image
    :param poly_verts: list of  coordinates from ROI selection
    :param on_original: boolean indicating if the mask is applied to original or sliced image
    :return: image mask that can be applied to image
    """
    if len(np.shape(image)) == 3:
        ny, nx, nz = np.shape(image)
    else:
        ny, nx = np.shape(image)
    # if mask is applied to original, each coordinate is multiplied by 2
    if on_original:
        poly_verts = [(2 * x, 2 * y) for (x, y) in poly_verts]

    x, y = np.meshgrid(np.arange(nx), np.arange(ny))
    x, y = x.flatten(), y.flatten()
    points = np.vstack((x, y)).T
    roi_path = MplPath(poly_verts)
    mask = roi_path.contains_points(points).reshape((ny, nx))
    return mask

