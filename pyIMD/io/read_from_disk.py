from nptdms import TdmsFile
from pandas import read_csv

__author__ = 'Andreas P. Cuny'


def read_from_tdms(file):
    """Method to read data from National Instruments technical data management streaming files (TDMS).

    Args:
        file (`str`):              File path + File name string.

    Returns:
        data (`pandas data frame`):  Returns data structured in a pandas data frame.

    """
    tdms_file = TdmsFile(file)
    df = tdms_file.as_dataframe(time_index=False, absolute_time=False)
    return df


def read_from_text(file, delimiter, read_from_row):
    """Method to read data from text files.

    Args:
        file (`str`):               File path + File name.
        delimiter (`str`):          Delimiter used in the data file to seperate columns
        read_from_row (`int`):      Row number from where to start reading data to be able \
                                    to skip heading text rows. Make sure that you keep the \
                                    Frequency, Amplitude and Phase headers.

    Returns:
        data (`pandas data frame`):  Returns data structured in a pandas data frame.

    """
    data = read_csv(file, sep=delimiter, skiprows=read_from_row)
    return data
