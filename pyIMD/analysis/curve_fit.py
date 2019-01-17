from numpy import arctan

__author__ = 'Andreas P. Cuny'


def fit_function(x, fn, q, a, b):
<<<<<<< HEAD
    """Calculates the function fit

    Args:
         x (`float`):              Frequency (the independent variable of that function)
         fn (`float`):             Resonance frequency
         q (`float`):              Q factor (losses)
         a (`float`):              Linear factor accounting for a linear background
         b (`float`):              Offset of the background

    Returns:
         fit (`float`):           Returns fit as panda data frame
=======
    """fit_function is the phase response of a damped harmonic oscillator (i.e. the cantilever with or without cell).
    It is called from calculate_resonance_frequencies, to be fitted to the data primarily to extract the resonance frequency.

    Args:
    :param x:              Frequency (the independent variable of the function)
    :param fn:             Resonance frequency
    :param q:              Q factor (losses)
    :param a:              Linear factor accounting for a linear background
    :param b:              Offset of the background

    Returns:
    :return phase:           Returns the phase as panda data frame
>>>>>>> 464c4bfd865cfbda544467e988e82b2ad264a249
    """

    phase = -arctan(q * (fn * fn - x * x)/(fn * x)) + a * x + b
    return phase


