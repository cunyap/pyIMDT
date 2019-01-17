from numpy import arctan

__author__ = 'Andreas P. Cuny'


def fit_function(x, fn, q, a, b):
    """Calculates the function fit

    Args:
         x (`float`):              Frequency (the independent variable of that function)
         fn (`float`):             Resonance frequency
         q (`float`):              Q factor (losses)
         a (`float`):              Linear factor accounting for a linear background
         b (`float`):              Offset of the background

    Returns:
         fit (`float`):           Returns fit as panda data frame
    """

    fit = -arctan(q * (fn * fn - x * x)/(fn * x)) + a * x + b
    return fit


