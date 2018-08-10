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


def calculate_resonance_frequencies(frequency_array, phase_array, initial_param_guess, lower_param_bounds,
                                    upper_param_bounds):
    """calculate_resonance_frequencies Calculates the resonance frequency
       from input frequency and phase array.

    Args:
    :param frequency_array:          Array of frequencies [in kHz]
    :param phase_array:              Array of phase [in Rad]
    :param initial_param_guess:      Initial parameter guess (1x4 array)
    :param lower_param_bounds:       Lower bounds (1x4 array)
    :param upper_param_bounds:      Upper bounds (1x4 array)

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

def calculate_position_correction(cell_position,cantilever_length):

    """calculate_position_correction calculates the correction factor with which the measured mass needs to be
    multiplied to get all the mass present on the cantilever. This is needed as the cantilever is differently sensitive
    to mass, depending on the location where this mass is attached.

    Args:
    :param cell_position:       Cell position from the free end of the cantilever [in micrometer]
    :param cantilever_length:   Cantilever length [in micrometer]

    Returns:
    :return correction_factor:           returns a double which is the correction factor.
    """

    kL=1.875
    cantilever_length=cantilever_length/1e6
    cell_position=cell_position/1e6
    k=kL/L
    return (1/(0.5*((np.cos(k*(cantilever_length-cell_position))-np.cosh(k*(cantilever_length-cell_position)))-
                    (np.cos(k*cantilever_length)+np.cosh(k*cantilever_length))/(np.sin(k*cantilever_length)+np.sinh(k*cantilever_length))*
                    (np.sin(k*(cantilever_length-cell_position))-np.sinh(k*(cantilever_length-cell_position)))))**2)