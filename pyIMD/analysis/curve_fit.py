from numpy import arctan

__author__ = 'Andreas P. Cuny'


def fit_function(x, fn, q, a, b):
    """fit_function Calculates the function fit

    Args:
    :param x:              Frequency (the independent variable of that function)
    :param fn:             Resonance frequency
    :param q:              Q factor (losses)
    :param a:              Linear factor accounting for a linear background
    :param b:              Offset of the background

    Returns:
    :return fit:           Returns fit as panda data frame
    """

    fit = -arctan(q * (fn * fn - x * x)/(fn * x)) + a * x + b
    return fit


