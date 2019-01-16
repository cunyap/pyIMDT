from numpy import arctan

__author__ = 'Andreas P. Cuny'


def fit_function(x, fn, q, a, b):
    """fit_function is the phase response of a damped harmonic oscillator. It is called from calculate_resonance_frequencies, to be fitted to the data
    primarily to extract the resonance frequency.

    Args:
    :param x:              Frequency (the independent variable of the function)
    :param fn:             Resonance frequency
    :param q:              Q factor (losses)
    :param a:              Linear factor accounting for a linear background
    :param b:              Offset of the background

    Returns:
    :return phase:           Returns the phase as panda data frame
    """

    phase = -arctan(q * (fn * fn - x * x)/(fn * x)) + a * x + b
    return phase


