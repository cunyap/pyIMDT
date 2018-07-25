import warnings
from pandas import concat, DataFrame
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
    y_fit.name = 'Phase [rad]'
    x.name = 'Frequency [kHz]'
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
    :param calculated_cell_mass   List of cell mass

    Return
    :return p:                    ggplot plot object

    """

    x = list(range(0, len(calculated_cell_mass)))
    data = concat([DataFrame(x, columns=['Time [iteration]']), DataFrame(calculated_cell_mass,
                                                                         columns=['Mass [pg]'])], axis=1)
    col_names = list(data)

    # Plot data
    p = ggplot(aes(x=col_names[0], y=col_names[1]), data=data) + \
        geom_point(alpha=0.1) + \
        theme_bw()
    return p
