import numpy as np

__author__ = 'Andreas P. Cuny'


def fit_function(x, fn, q, a, b):
    """fit_function defines the phase response of a damped harmonic oscillator (i.e. the cantilever with or without cell).
    It is called from calculate_resonance_frequencies, to be fitted to the data primarily to extract the natural resonance \
    frequency.

    Args:
         x (`float`):              Frequency (the independent variable of that function)
         fn (`float`):             Natural resonance frequency
         q (`float`):              Q factor (losses)
         a (`float`):              Linear factor accounting for a linear background
         b (`float`):              Constant Phase-Offset

    Returns:
    phase (`float`):               Returns the phase.
    """

    phase = -np.arctan(q * (fn * fn - x * x)/(fn * x)) + a * x + b
    return phase


