from math import pi
from scipy import optimize
from pyIMD.analysis.curve_fit import fit_function

__author__ = 'Andreas P. Cuny'


def calculate_mass(spring_constant, res_freq_after_cell_load_array, res_freq_before_cell_load_array):
    """calculate_mass Calculates the mass given freq 1 -3 in pandas data frame

    Args:
    :param spring_constant:
    :param res_freq_after_cell_load_array:
    :param res_freq_before_cell_load_array:

    Returns:
    :return mass:           Returns data structured in a pandas data frame.
    """
    mass = (spring_constant / (4 * pi * pi) * (1 / (res_freq_after_cell_load_array*res_freq_after_cell_load_array) - 1 /
                                               (res_freq_before_cell_load_array*res_freq_before_cell_load_array))) * 1e6

    return mass


def calculate_resonance_frequencies(frequency_array, phase_array):
    """calculate_resonance_frequencies Calculates the resonance frequency
       from input frequency and phase array.

    Args:
    :param frequency_array:          Array of frequencies [in kHz]
    :param phase_array:              Array of phase [in Rad]

    Returns:
    :retrun resonance_frequency:     Resonance frequency [in kHz]
    :retrun params:                  Curve fit parameters;
                                     param[0] := Q factor (losses)
                                     param[1] := Linear factor accounting for a linear background
                                     param[2] := Offset of the background@TODO name each of them!

    """

    params, _ = optimize.curve_fit(fit_function, frequency_array.astype(float), phase_array.astype(float),
                                   p0=[70.0, 2.0, 0.5, 0], bounds=([10.0, 1.0, -0.5, -1.0], [80.0, 5.0, 1, 1.0]))

    resonance_frequency = params[0]
    return resonance_frequency, params[1:]
