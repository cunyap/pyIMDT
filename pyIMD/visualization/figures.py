import warnings
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
