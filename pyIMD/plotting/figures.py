import math
import warnings
import numpy as np
from pandas import concat
from pyIMD.analysis.curve_fit import fit_function
from plotnine import ggplot, aes, geom_line, geom_point, theme_bw

__author__ = 'Andreas P. Cuny'

warnings.filterwarnings("ignore")


def plot_fitting(x, y, resonance_frequency, parameter):
    """ Plots the resonance frequency and the function fit

    Args:
    :param x:                       X coordinates (frequency in kHz)
    :param y:                       Y coordinates (phase in radians)
    :param resonance_frequency:     Resonnance frequency of x,y
    :param parameter:               Parameter of function fit

    Returns:
    :return: p:                     ggplot object
    """

    y_fit = fit_function(x, resonance_frequency, parameter[0], parameter[1], parameter[2])
    y_fit.name = 'Phase fit'
    x.name = 'Frequency [kHz]'
    y.name = 'Phase [rad]'
    data = concat([x, y, y_fit], axis=1)
    col_names = list(data)

    # Plot data
    p = ggplot(aes(x=col_names[0], y=col_names[1]), data=data) + \
        geom_point() + \
        geom_line(aes(x=col_names[0], y=col_names[2]),  color='red', size=0.5) + \
        theme_bw()
    return p


def plot_mass(calculated_cell_mass):
    """ Plots the resulting mass

    Args
    :param calculated_cell_mass   Dataframe [Nx2] with time and calculated cell mass data

    Return
    :return p:                    ggplot plot object

    """

    col_names = list(calculated_cell_mass)
    col_names[0] = 'Time [h]'
    calculated_cell_mass.columns = col_names

    # Plot data
    p = ggplot(aes(x=col_names[0], y=col_names[1]), data=calculated_cell_mass) + \
        geom_point(alpha=0.1) + \
        geom_line(aes(y=col_names[2]), color='red') + \
        theme_bw()
    return p


def get_montage_array_size(size, image_row_count, image_col_count, frame_count):
    """

    :param size: numpy array specifying the amount of images displayed in the montage per row and column.
    If one argument is replaced with np.nan, the needed amount of rows or columns is calculated automatically. E. g.
    [5, np.nan]
    :param image_row_count: Number of rows per image
    :param image_col_count: Number of columns per image
    :param frame_count: Number of image frames in the stack
    :return: montage_size: array with the number of rows and columns needed in the montage array for the images
    """

    if len(size) == 0 or np.isnan(size).all():
        col = math.sqrt(image_row_count * frame_count / image_col_count)

        col = math.ceil(col)
        row = math.ceil(frame_count / col)
        montage_size = [row, col]

    elif any(np.isnan(size)):
        montage_size = size
        nan_idx = np.isnan(size)
        montage_size[nan_idx] = np.ceil(frame_count / size[~nan_idx])

    elif size[0] * size[1] < frame_count:
        return

    else:
        montage_size = size

    return montage_size


def create_montage_array(img_stack, size):
    """
    Creates an image montage of a 3D numpy array with the shape [image frames, image row, image col] for the specified
    size.
    :param img_stack: 3D numpy array [image frames, image row, image col]
    :param size: numpy array specifying the amount of images displayed in the montage per row and column.
    If one argument is replaced with np.nan, the needed amount of rows or columns is calculated automatically. E. g.
    [5, np.nan]
    :return: 2D numpy array with the image montage
    """

    image_row_count = img_stack.shape[1]
    image_col_count = img_stack.shape[2]
    frame_count = img_stack.shape[0]

    montage_size = get_montage_array_size(size, image_row_count, image_col_count, frame_count)

    montage_size = list(np.int_(montage_size))
    montage_row_count = montage_size[0]
    montage_col_count = montage_size[1]

    montage_image_size = [montage_row_count * image_row_count, montage_col_count * image_col_count]

    montage_image_size = list(np.int_(montage_image_size))
    montage = np.zeros(montage_image_size)

    rows = list(range(0, image_row_count))
    cols = list(range(0, image_col_count))
    i_frame = 0

    for i in range(0, montage_row_count):
        for j in range(0, montage_col_count):
            if i_frame < frame_count:
                r = list(np.asarray(rows) + i * image_row_count)
                c = list(np.asarray(cols) + j * image_col_count)
                montage[np.ix_(r, c)] = img_stack[i_frame, :, :]

            else:
                montage = montage
            i_frame = i_frame + 1

    return montage
