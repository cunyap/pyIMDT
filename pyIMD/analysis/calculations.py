import numpy as np
from math import pi
from scipy import optimize
from pyIMD.analysis.curve_fit import fit_function

__author__ = 'Andreas P. Cuny'


def calculate_mass(spring_constant, res_freq_after_cell_load_array, res_freq_before_cell_load_array):
    """calculate_mass Calculates the mass given freq 1 -3 in pandas data frame

    Args:
    :param spring_constant:                     Stiffness of the cantilever [in N/m]
    :param res_freq_after_cell_load_array:      Resonance frequency of the cantilever AFTER the cell is picked up, at timepoint t [in kHz]
    :param res_freq_before_cell_load_array:     Resonance frequency of the cantilever BEFORE the cell is picked up [in kHz]
    
    // ARE THE TWO LAST ONES REALLY ARRAYS AS THE NAME SUGGESTS? PLEASE CHECK GF

    Returns:
    :return mass:           Returns data structured in a pandas data frame, which is the mass at timepoint t.
    
    // IS THIS REALLY A STRUCT IN A DATAFRAME OR JUST A DOUBLE? PLEASE CHECK GF
    """
    mass = (spring_constant / (4 * pi * pi) * (1 / (res_freq_after_cell_load_array*res_freq_after_cell_load_array) - 1 /
                                               (res_freq_before_cell_load_array*res_freq_before_cell_load_array))) * 1e6

    return mass


def calculate_resonance_frequencies(frequency_array, phase_array, initial_param_guess, lower_param_bounds,
                                    upper_param_bounds):
    """calculate_resonance_frequencies calculates the resonance frequency
       from input frequency and phase array. It does so via fitting the phase response of a harmonic oscillator (defined in pyIMD.analysis.curve_fit). 
       The first fit parameter of the fit parameter array is the resonance frequency.

    Args:
    :param frequency_array:          Array of frequencies [in kHz]
    :param phase_array:              Array of phase [in Rad]
    :param initial_param_guess:      Initial parameter guess (1x4 array)
    :param lower_param_bounds:       Lower bounds (1x4 array)
    :param upper_param_bounds:       Upper bounds (1x4 array)

    Returns:
    :retrun resonance_frequency:     Resonance frequency [in kHz]
    :retrun params:                  Curve fit parameters;
                                     param[0] := Q factor (losses)
                                     param[1] := Linear factor accounting for a linear background
                                     param[2] := Offset of the background

    """

    params, _ = optimize.curve_fit(fit_function, frequency_array.astype(float), phase_array.astype(float),
                                   p0=initial_param_guess, bounds=(lower_param_bounds, upper_param_bounds))

    resonance_frequency = params[0]
    return resonance_frequency, params[1:]


def calculate_position_correction(cell_position, cantilever_length):

    """calculate_position_correction calculates the correction factor with which the measured mass needs to be
    multiplied to get all the mass present on the cantilever. This is needed as the cantilever is differently sensitive
    to mass, depending on the location where this mass is attached. The measurements are performed with the first mode of vibration,
    which is described by the factor kL = 1.875. For higher modes, different would be used (4.694 for the second , 7.855 for the third etc.)

    Args:
    :param cell_position:       Cell position from the free end of the cantilever [in micrometer]
    :param cantilever_length:   Cantilever length [in micrometer]

    Returns:
    :return correction_factor:           returns a double which is the correction factor.
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
