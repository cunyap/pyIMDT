import numpy as np
from math import pi
from scipy import optimize
from pyIMD.analysis.curve_fit import fit_function

__author__ = 'Andreas P. Cuny'


def calculate_mass(spring_constant, res_freq_after_cell_load_array, res_freq_before_cell_load_array):
    """Calculates the mass given freq 1 -3 in pandas data frame

    Args:
         spring_constant (`float`):
         res_freq_after_cell_load_array (`float`):
         res_freq_before_cell_load_array (`float`):

    Returns:
         mass (`panda data frame`):                      Returns data structured in a pandas data frame.
    """
    mass = (spring_constant / (4 * pi * pi) * (1 / (res_freq_after_cell_load_array*res_freq_after_cell_load_array) - 1 /
                                               (res_freq_before_cell_load_array*res_freq_before_cell_load_array))) * 1e6

    return mass


def calculate_resonance_frequencies(frequency_array, phase_array, initial_param_guess, lower_param_bounds,
                                    upper_param_bounds):
    """Calculates the resonance frequency from input frequency and phase array.

    Args:
        frequency_array (`float`):              Array of frequencies [in kHz]
        phase_array (`float`):                  Array of phase [in Rad]
        initial_param_guess (`float`):          Initial parameter guess (1x4 array)
        lower_param_bounds (`float`):           Lower bounds (1x4 array)
        upper_param_bounds (`float`):           Upper bounds (1x4 array)

    Returns:
        resonance_frequency (`float`):          Resonance frequency [in kHz]
    Returns:
        curve_fit_parameter (`float array`):    Curve fit parameters
                                                curve_fit_parameter[0] := Q factor (losses)

                                                curve_fit_parameter[1] := Linear factor accounting for a linear \
                                                background

                                                curve_fit_parameter[2] := Offset of the background


    """

    params, _ = optimize.curve_fit(fit_function, frequency_array.astype(float), phase_array.astype(float),
                                   p0=initial_param_guess, bounds=(lower_param_bounds, upper_param_bounds))

    resonance_frequency = params[0]
    return resonance_frequency, params[1:]


def calculate_position_correction(cell_position, cantilever_length):

    """Calculates the correction factor with which the measured mass needs to be
    multiplied to get all the mass present on the cantilever. This is needed as the cantilever is differently sensitive
    to mass, depending on the location where this mass is attached.

    Args:
        cell_position (`float`):       Cell position from the free end of the cantilever [in micrometer]
        cantilever_length (`float`):   Cantilever length [in micrometer]

    Returns:
        correction_factor (`float`):   Returns a double which is the correction factor.
    """

    kL = 1.875
    cantilever_length = cantilever_length/1e6
    cell_position = cell_position/1e6
    k = kL / cantilever_length
    return (1/(0.5*((np.cos(k * (cantilever_length - cell_position)) - np.cosh(k * (cantilever_length - cell_position)))
                    - (np.cos(k * cantilever_length) + np.cosh(k*cantilever_length)) / (np.sin(k * cantilever_length) +
                                                                                        np.sinh(k * cantilever_length))
                    * (np.sin(k * (cantilever_length - cell_position)) - np.sinh(k *
                                                                                 (cantilever_length-cell_position)))))
            ** 2)
