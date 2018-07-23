from nptdms import TdmsFile
from pandas import read_csv

__author__ = 'Andreas P. Cuny'


def read_from_tdms(file):
    """read_from_tdms Reads data from tdms files and returns the data structured \
       in a pandas data frame.

    Args:
    :param file:            File path + File name string.

    Returns:
    :return    df:          Returns data structured in a pandas data frame.

    """
    tdms_file = TdmsFile(file)
    df = tdms_file.as_dataframe(time_index=False, absolute_time=False)
    return df


def read_from_text(file, delimiter, read_from_row):
    """read_from_text Reads data from text files and returns the \
       data structured in a pandas data frame.

    Args:
    :param file:              File path + File name string.
    :param delimiter:         Delimiter used in the data file to seperate columns
    :param read_from_row:     Row number from where to start reading data to be able \
                              to skip heading text rows. Make sure that you keep the \
                              Frequency, Amplitude and Phase headers.

    Returns:
    :return data:             Returns data structured in a pandas data frame.

    """
    data = read_csv(file, sep=delimiter, skiprows=read_from_row)
    return data