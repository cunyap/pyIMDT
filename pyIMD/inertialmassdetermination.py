import os
import logging
from pathlib import Path
from tqdm import trange
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
from pandas import concat, DataFrame
from pyIMD.configuration.config import Settings
from pyIMD.file_io.read_from_disk import read_from_text
from pyIMD.file_io.read_from_disk import read_from_tdms
from pyIMD.file_io.write_to_disk import write_to_disk_as
from pyIMD.analysis.calculations import calculate_mass
from pyIMD.analysis.calculations import calculate_resonance_frequencies
from pyIMD.visualization.figures import plot_fitting
from pyIMD.visualization.figures import plot_mass

__author__ = 'Andreas P. Cuny'


class InertialMassDetermination:
    """
    Constructs a IntertialMassDetermination object
    """

    def __init__(self, file_path1, file_path2, file_path3, delimiter, read_from_row, measurement_mode):
        """
        Constructs a InteritalMassDetermination object with the following arguments. Two modes \
        enable the analysis of different experimental setups. Sweep mode [0] and PLL mode [1].

        Args:
        :param file_path1:       File path + File name [String] of initial frequency \
                                 shift measurement before cell attachment (txt file).
        :param file_path2:       File path + File name [String] of initial frequency \
                                 shift measurement after cell attachment (txt file).
        :param file_path3:       File path + File name [String] of the actual \
                                 measurement (tdms file).
        :param measurement_mode: Boolean, 0 := sweep mode, 1 := phase lock loops mode
        """
        # InertialMassDetermination.__init__(self, file_path1, file_path2, file_path3, delimiter, read_from_row, \
        # measurement_mode)
        self.file_path1 = str(Path(file_path1))
        self.file_path2 = str(Path(file_path2))
        self.file_path3 = str(Path(file_path3))
        self.delimiter = delimiter
        self.read_from_row = read_from_row
        self.measurement_mode = measurement_mode

        self.data_pre_start_no_cell = []
        self.data_pre_start_with_cell = []
        self.data_measured = []
        self.resonance_freq_pre_start_no_cell = []
        self.resonance_freq_pre_start_with_cell = []
        self.resonance_freq_measured = []
        self.fit_param_pre_start_no_cell = []
        self.fit_param_pre_start_with_cell = []
        self.fit_param_measured = []
        self.calculated_cell_mass = []

        self.result_folder = os.path.dirname(os.path.abspath(file_path3))
        self.settings = Settings()

        self.logger = self.get_logger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.logger.info('Object constructed successfully')

    def run_intertial_mass_determination(self):
        """run_intertial_mass_determination Calculates the intertial mass.

        Returns:
        :return result:          Returns result structured in a pandas data frame and saves function fit plots as pdf
                                 files.
        """

        # Read data
        self.logger.info('Start reading all files')
        self.data_pre_start_no_cell = read_from_text(self.file_path1, self.delimiter, self.read_from_row)
        self.data_pre_start_with_cell = read_from_text(self.file_path2, self.delimiter, self.read_from_row)
        self.data_measured = read_from_tdms(self.file_path3)
        self.logger.info('Done reading all files')
        # Convert data to the correct units
        self.convert_data()
        self.logger.info('Done converting units')

        # Calc resonance frequency for pre start data without cell attached to cantilever
        self.resonance_freq_pre_start_no_cell, self.fit_param_pre_start_no_cell = calculate_resonance_frequencies(
            self.data_pre_start_no_cell.iloc[:, 0], self.data_pre_start_no_cell.iloc[:, 2],
            self.settings.INITIAL_PARAMETER_GUESS, self.settings.LOWER_PARAMETER_BOUNDS,
            self.settings.UPPER_PARAMETER_BOUNDS)

        figure_pre_start_no_cell = plot_fitting(self.data_pre_start_no_cell.iloc[:, 0],
                                                self.data_pre_start_no_cell.iloc[:, 2],
                                                self.resonance_freq_pre_start_no_cell,
                                                self.fit_param_pre_start_no_cell)

        optional_fig_param = {'width': self.settings.FIGURE_WIDTH, 'height': self.settings.FIGURE_HEIGHT,
                              'units': self.settings.FIGURE_UNITS,
                              'resolution': self.settings.FIGURE_RESOLUTION_DPI}
        write_to_disk_as(self.settings.FIGURE_FORMAT, figure_pre_start_no_cell, '{}'.format(self.result_folder +
                         os.sep + self.settings.FIGURE_NAME_PRE_START_NO_CELL), **optional_fig_param)
        self.logger.info('Done with pre start no cell resonance frequency calculation')

        # Calc resonance frequency for pre start data with cell attached to cantilever
        self.resonance_freq_pre_start_with_cell, self.fit_param_pre_start_with_cell = calculate_resonance_frequencies(
            self.data_pre_start_with_cell.iloc[:, 0], self.data_pre_start_with_cell.iloc[:, 2],
            self.settings.INITIAL_PARAMETER_GUESS, self.settings.LOWER_PARAMETER_BOUNDS,
            self.settings.UPPER_PARAMETER_BOUNDS)

        figure_pre_start_with_cell = plot_fitting(self.data_pre_start_with_cell.iloc[:, 0],
                                                  self.data_pre_start_with_cell.iloc[:, 2],
                                                  self.resonance_freq_pre_start_with_cell,
                                                  self.fit_param_pre_start_with_cell)

        write_to_disk_as(self.settings.FIGURE_FORMAT, figure_pre_start_with_cell, '{}'.format(self.result_folder +
                         os.sep + self.settings.FIGURE_NAME_PRE_START_WITH_CELL), **optional_fig_param)
        self.logger.info('Done with pre start with cell resonance frequency calculation')

        if self.measurement_mode == 0:
            # The continuous sweep mode
            self.calculated_cell_mass = []
            for iSweep in trange(0, len(self.data_measured), 3):
                # Calc resonance frequency and function fit for the ith sweep (iSweep)
                res_freq, param = calculate_resonance_frequencies(self.data_measured.iloc[iSweep + 2, 0:255],
                                                                  self.data_measured.iloc[iSweep + 1, 0:255],
                                                                  self.settings.INITIAL_PARAMETER_GUESS,
                                                                  self.settings.LOWER_PARAMETER_BOUNDS,
                                                                  self.settings.UPPER_PARAMETER_BOUNDS)
                # Calculate the mass for the ith sweep (iSweep)
                # @todo append self.resonance_freq_pre_start_with_cell to the list self.calculated_cell_mass first!
                mass = calculate_mass(self.settings.SPRING_CONSTANT, res_freq, self.resonance_freq_pre_start_no_cell)
                # Store results in a list
                self.resonance_freq_measured.append(res_freq)
                self.fit_param_measured.append(param)
                self.calculated_cell_mass.append(mass)

                if np.remainder(iSweep, 300) == 0:
                    figure_i_sweep = plot_fitting(self.data_measured.iloc[iSweep + 2, 0:255],
                                                  self.data_measured.iloc[iSweep + 1, 0:255], res_freq, param)
                    write_to_disk_as(self.settings.FIGURE_FORMAT, figure_i_sweep, '{}'.format(self.result_folder +
                                                                                              os.sep + 'ResFreqSweep_'
                                                                                              + str(iSweep)))

            calculated_cell_mass = concat([(self.data_measured.iloc[0:int(len(self.data_measured)) / 3, 256] -
                                            self.data_measured.iloc[0, 256]) / 3600, DataFrame(self.calculated_cell_mass
                                                                                               , columns=['Mass [ng]'])]
                                          , axis=1)

            figure_cell_mass = plot_mass(calculated_cell_mass)
            self.logger.info('Start writing figure to disk')
            write_to_disk_as(self.settings.FIGURE_FORMAT, figure_cell_mass, '{}'.format(self.result_folder +
                             os.sep + self.settings.FIGURE_NAME_MEASURED_DATA), **optional_fig_param)
            # Export results to csv
            calculated_cell_mass.to_csv(self.result_folder + os.sep + self.settings.FIGURE_NAME_MEASURED_DATA,
                                        sep=self.settings.TEXT_DATA_DELIMITER, index=False)
            self.calculated_cell_mass = calculated_cell_mass
            self.logger.info('Done writing figure to disk')

        else:
            # The PLL mode
            # Add resonance_freq_pre_start_with_cell to measured resonance frequency delta
            # Calculate the mass
            self.calculated_cell_mass = []
            for iPLL in trange(0, len(self.data_measured)):
                mass = calculate_mass(self.settings.SPRING_CONSTANT, self.data_measured.iloc[iPLL, 6] +
                                      self.resonance_freq_pre_start_with_cell,
                                      self.resonance_freq_pre_start_no_cell)

                self.calculated_cell_mass.append(mass)

            calculated_cell_mass = concat([(self.data_measured.iloc[:, 0] - self.data_measured.iloc[1, 0]) / 3600,
                                           DataFrame(self.calculated_cell_mass, columns=['Mass [ng]'])], axis=1)
            calculated_cell_mass['Mean mass [ng]'] = calculated_cell_mass['Mass [ng]'].rolling(window=10000).mean()
            figure_cell_mass = plot_mass(calculated_cell_mass)
            self.logger.info('Start writing figure to disk')
            write_to_disk_as(self.settings.FIGURE_FORMAT, figure_cell_mass, '{}'.format(self.result_folder +
                             os.sep + self.settings.FIGURE_NAME_MEASURED_DATA), **optional_fig_param)
            # Export results to csv
            calculated_cell_mass.to_csv(self.result_folder + os.sep + self.settings.FIGURE_NAME_MEASURED_DATA,
                                        sep=self.settings.TEXT_DATA_DELIMITER, index=False)
            self.calculated_cell_mass = calculated_cell_mass
            self.logger.info('Done writing figure to disk')
        self.logger.info('Done with all calculations')

    def convert_data(self):
        """ Converts imported data into correct units

        Note: It might be faster to skip this step and do it on the fly while computing the resonance frequencies
              directly.

        """

        attributes = ['data_pre_start_no_cell', 'data_pre_start_with_cell']
        for iAttribute in attributes:
            getattr(self, str(iAttribute)).iloc[:, 0] = getattr(self, str(iAttribute)).iloc[:, 0] / \
                                                        self.settings.CONVERSION_FACTOR_HZ_TO_KHZ
            getattr(self, str(iAttribute)).iloc[:, 2] = getattr(self, str(iAttribute)).iloc[:, 2] / \
                                                        self.settings.CONVERSION_FACTOR_DEG_TO_RAD
        if self.measurement_mode == 0:
            for iSweep in range(0, len(self.data_measured), 3):
                # Calc resonance frequency and function fit for the ith sweep (iSweep)
                self.data_measured.iloc[iSweep + 1, 0:255] = self.data_measured.iloc[iSweep + 1, 0:255] / \
                                                             self.settings.CONVERSION_FACTOR_DEG_TO_RAD
                self.data_measured.iloc[iSweep + 2, 0:255] = self.data_measured.iloc[iSweep + 2, 0:255] / \
                                                             self.settings.CONVERSION_FACTOR_HZ_TO_KHZ
        else:
            self.data_measured.iloc[:, 5] = self.data_measured.iloc[:, 5] / self.settings.CONVERSION_FACTOR_DEG_TO_RAD
            self.data_measured.iloc[:, 6] = self.data_measured.iloc[:, 6] / self.settings.CONVERSION_FACTOR_HZ_TO_KHZ

    def get_logger(self, name):
        logger = logging.getLogger(name)
        if not logger.handlers:
            # Prevent logging from propagating to the root logger
            logger.propagate = 0
            console = logging.StreamHandler()
            logger.addHandler(console)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
            console.setFormatter(formatter)
        return logger

