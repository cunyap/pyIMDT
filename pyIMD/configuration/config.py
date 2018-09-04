import operator
from pyIMD.configuration.defaults import *

__author__ = 'Andreas P. Cuny'


class Settings(object):
    def __init__(self):
        self.FIGURE_WIDTH = FIGURE_WIDTH
        self.FIGURE_HEIGHT = FIGURE_HEIGHT
        self.FIGURE_UNITS = FIGURE_UNITS
        self.FIGURE_FORMAT = FIGURE_FORMAT
        self.FIGURE_RESOLUTION_DPI = FIGURE_RESOLUTION_DPI
        self.FIGURE_NAME_PRE_START_NO_CELL = FIGURE_NAME_PRE_START_NO_CELL
        self.FIGURE_NAME_PRE_START_WITH_CELL = FIGURE_NAME_PRE_START_WITH_CELL
        self.FIGURE_NAME_MEASURED_DATA = FIGURE_NAME_MEASURED_DATA
        self.CONVERSION_FACTOR_HZ_TO_KHZ = CONVERSION_FACTOR_HZ_TO_KHZ
        self.CONVERSION_FACTOR_DEG_TO_RAD = CONVERSION_FACTOR_DEG_TO_RAD
        self.SPRING_CONSTANT = SPRING_CONSTANT
        self.INITIAL_PARAMETER_GUESS = INITIAL_PARAMETER_GUESS
        self.LOWER_PARAMETER_BOUNDS = LOWER_PARAMETER_BOUNDS
        self.UPPER_PARAMETER_BOUNDS = UPPER_PARAMETER_BOUNDS
        self.READ_TEXT_DATA_FROM_LINE = READ_TEXT_DATA_FROM_LINE
        self.CANTILEVER_LENGTH = CANTILEVER_LENGTH
        self.CELL_POSITION = CELL_POSITION
        self.TEXT_DATA_DELIMITER = TEXT_DATA_DELIMITER

    def __repr__(self):
        """
        Settings representation.
        :return: string
        """
        return "pyIMD Setting: \n\tFIGURE_WIDTH: %s (%s) \n\tFIGURE_HEIGHT: %s (%s) \n\tFIGURE_UNITS: %s (%s) " \
               "\n\tFIGURE_FORMAT: %s (%s) \n\tFIGURE_RESOLUTION_DPI: %s (%s) " \
               "\n\tFIGURE_NAME_PRE_START_NO_CELL: %s (%s) \n\tFIGURE_NAME_PRE_START_WITH_CELL: %s (%s)" \
               "\n\tFIGURE_NAME_MEASURED_DATA: %s(%s) \n\tCONVERSION_FACTOR_HZ_TO_KHZ: %s (%s) " \
               "\n\tCONVERSION_FACTOR_DEG_TO_RAD: %s (%s) \n\tSPRING_CONSTANT: %s (%s) " \
               "\n\tINITIAL_PARAMETER_GUESS: %s (%s) \n\tLOWER_PARAMETER_BOUNDS: %s (%s) " \
               "\n\tUPPER_PARAMETER_BOUNDS: %s (%s) \n\tREAD_TEXT_DATA_FROM_LINE: %s (%s) " \
               "\n\tCANTILEVER_LENGTH: %s (%s) \n\tCELL_POSITION: %s (%s) " \
               "\n\tTEXT_DATA_DELIMITER: %s (%s)" % (
            self.FIGURE_WIDTH, type(self.FIGURE_WIDTH), self.FIGURE_HEIGHT, type(self.FIGURE_HEIGHT), self.FIGURE_UNITS,
            type(self.FIGURE_UNITS), self.FIGURE_FORMAT, type(self.FIGURE_FORMAT), self.FIGURE_RESOLUTION_DPI,
            type(self.FIGURE_RESOLUTION_DPI), self.FIGURE_NAME_PRE_START_NO_CELL, type(self.FIGURE_NAME_PRE_START_NO_CELL),
            self.FIGURE_NAME_PRE_START_WITH_CELL, type(self.FIGURE_NAME_PRE_START_WITH_CELL),  self.FIGURE_NAME_MEASURED_DATA,
            type(self.FIGURE_NAME_MEASURED_DATA), self.CONVERSION_FACTOR_HZ_TO_KHZ, type(self.CONVERSION_FACTOR_HZ_TO_KHZ),
            self.CONVERSION_FACTOR_DEG_TO_RAD, type(self.CONVERSION_FACTOR_DEG_TO_RAD), self.SPRING_CONSTANT,
            type(self.SPRING_CONSTANT), self.INITIAL_PARAMETER_GUESS, type(self.INITIAL_PARAMETER_GUESS),
            self.LOWER_PARAMETER_BOUNDS, type(self.LOWER_PARAMETER_BOUNDS), self.UPPER_PARAMETER_BOUNDS,
            type(self.UPPER_PARAMETER_BOUNDS), self.READ_TEXT_DATA_FROM_LINE, type(self.READ_TEXT_DATA_FROM_LINE),
            self.CANTILEVER_LENGTH, type(self.CANTILEVER_LENGTH),self.CELL_POSITION, type(self.CELL_POSITION),
            self.TEXT_DATA_DELIMITER, type(self.TEXT_DATA_DELIMITER))

    FIGURE_FORMAT = property(operator.attrgetter('_FIGURE_FORMAT'))

    @FIGURE_FORMAT.setter
    def FIGURE_FORMAT(self, unit):
        if not (type(unit) == str):
            raise Exception("Figure format should be of type string. 'png' and 'pdf' are valid")
        self._FIGURE_FORMAT = unit

    FIGURE_WIDTH = property(operator.attrgetter('_FIGURE_WIDTH'))

    @FIGURE_WIDTH.setter
    def FIGURE_WIDTH(self, width):
        if not (type(width) == float or type(width) == int):
            raise Exception("Figure width should be float or int")
        self._FIGURE_WIDTH = width

    FIGURE_HEIGHT = property(operator.attrgetter('_FIGURE_HEIGHT'))

    @FIGURE_HEIGHT.setter
    def FIGURE_HEIGHT(self, height):
        if not (type(height) == float or type(height) == int):
            raise Exception("Figure height should be of type float or int")
        self._FIGURE_HEIGHT = height

    FIGURE_UNITS = property(operator.attrgetter('_FIGURE_UNITS'))

    @FIGURE_UNITS.setter
    def FIGURE_UNITS(self, unit):
        if not (type(unit) == str):
            raise Exception("Figure unit should be of type string. 'mm', 'cm' and 'in' are valid")
        self._FIGURE_UNITS = unit

    FIGURE_RESOLUTION_DPI = property(operator.attrgetter('_FIGURE_RESOLUTION_DPI'))

    @FIGURE_RESOLUTION_DPI.setter
    def FIGURE_RESOLUTION_DPI(self, resolution):
        if not (type(resolution) == int):
            raise Exception("Figure resolution should be a of type int.")
        self._FIGURE_RESOLUTION_DPI = resolution

    FIGURE_NAME_PRE_START_NO_CELL = property(
        operator.attrgetter('_FIGURE_NAME_PRE_START_NO_CELL'))

    @FIGURE_NAME_PRE_START_NO_CELL.setter
    def FIGURE_NAME_PRE_START_NO_CELL(self, name):
        if not (type(name) == str):
            raise Exception("Figure name should be a of type string.")
        self._FIGURE_NAME_PRE_START_NO_CELL = name

    FIGURE_NAME_PRE_START_WITH_CELL = property(
        operator.attrgetter('_FIGURE_NAME_PRE_START_WITH_CELL'))

    @FIGURE_NAME_PRE_START_WITH_CELL.setter
    def FIGURE_NAME_PRE_START_WITH_CELL(self, name):
        if not (type(name) == str):
            raise Exception("Figure name should be a of type string.")
        self._FIGURE_NAME_PRE_START_WITH_CELL = name

    FIGURE_NAME_MEASURED_DATA = property(operator.attrgetter('_FIGURE_NAME_MEASURED_DATA'))

    @FIGURE_NAME_MEASURED_DATA.setter
    def FIGURE_NAME_MEASURED_DATA(self, name):
        if not (type(name) == str):
            raise Exception("Figure name of measured data should be a of type string.")
        self._FIGURE_NAME_MEASURED_DATA = name

    CONVERSION_FACTOR_HZ_TO_KHZ = property(operator.attrgetter('_CONVERSION_FACTOR_HZ_TO_KHZ'))

    @CONVERSION_FACTOR_HZ_TO_KHZ.setter
    def CONVERSION_FACTOR_HZ_TO_KHZ(self, factor):
        if not (type(factor) == float or type(factor) == int):
            raise Exception("Conversion factor should be a of type float or int.")
        self._CONVERSION_FACTOR_HZ_TO_KHZ = factor

    CONVERSION_FACTOR_DEG_TO_RAD = property(operator.attrgetter('_CONVERSION_FACTOR_DEG_TO_RAD'))

    @CONVERSION_FACTOR_DEG_TO_RAD.setter
    def CONVERSION_FACTOR_DEG_TO_RAD(self, factor):
        if not (type(factor) == float or type(factor) == int):
            raise Exception("Conversion factor should be a of type float or int.")
        self._CONVERSION_FACTOR_DEG_TO_RAD = factor

    SPRING_CONSTANT = property(operator.attrgetter('_SPRING_CONSTANT'))

    @SPRING_CONSTANT.setter
    def SPRING_CONSTANT(self, spring_constant):
        if not (type(spring_constant) == float or type(spring_constant) == int):
            raise Exception("Spring constant should be a of type float or int.")
        self._SPRING_CONSTANT = spring_constant

    INITIAL_PARAMETER_GUESS = property(operator.attrgetter('_INITIAL_PARAMETER_GUESS'))

    @INITIAL_PARAMETER_GUESS.setter
    def INITIAL_PARAMETER_GUESS(self, array):
        if not (array.__len__() == 4 and all(isinstance(n, int) or isinstance(n, float) for n in array)):
            raise Exception("Initial parameter guess list should be a of type list.")
        self._INITIAL_PARAMETER_GUESS = array

    LOWER_PARAMETER_BOUNDS = property(operator.attrgetter('_LOWER_PARAMETER_BOUNDS'))

    @LOWER_PARAMETER_BOUNDS.setter
    def LOWER_PARAMETER_BOUNDS(self, array):
        if not (array.__len__() == 4 and all(isinstance(n, int) or isinstance(n, float) for n in array)):
            raise Exception("Lower parameter bounds list should be a of type list.")
        self._LOWER_PARAMETER_BOUNDS = array

    UPPER_PARAMETER_BOUNDS = property(operator.attrgetter('_UPPER_PARAMETER_BOUNDS'))

    @UPPER_PARAMETER_BOUNDS.setter
    def UPPER_PARAMETER_BOUNDS(self, array):
        if not (array.__len__() == 4 and all(isinstance(n, int) or isinstance(n, float) for n in array)):
            raise Exception("Upper parameter bounds list should be a of type list.")
        self._UPPER_PARAMETER_BOUNDS = array

    READ_TEXT_DATA_FROM_LINE = property(operator.attrgetter('_READ_TEXT_DATA_FROM_LINE'))

    @READ_TEXT_DATA_FROM_LINE.setter
    def READ_TEXT_DATA_FROM_LINE(self, line_number):
        if not (type(line_number) == float or type(line_number) == int):
            raise Exception("Line number should be a of type float or int.")
        self._READ_TEXT_DATA_FROM_LINE = line_number

    CANTILEVER_LENGTH = property(operator.attrgetter('_CANTILEVER_LENGTH'))

    @CANTILEVER_LENGTH.setter
    def CANTILEVER_LENGTH(self, cantilever_length):
        if not (type(cantilever_length) == float or type(cantilever_length) == int):
            raise Exception("Data text delimiter should be a of float or int.")
        self._CANTILEVER_LENGTH = cantilever_length

    CELL_POSITION = property(operator.attrgetter('_CELL_POSITION'))

    @CELL_POSITION.setter
    def CELL_POSITION(self, cell_position):
        if not (type(cell_position) == float or type(cell_position) == int):
            raise Exception("Data text delimiter should be a of float or int.")
        self._CELL_POSITION = cell_position

    TEXT_DATA_DELIMITER = property(operator.attrgetter('_TEXT_DATA_DELIMITER'))

    @TEXT_DATA_DELIMITER.setter
    def TEXT_DATA_DELIMITER(self, delimiter):
        if not (type(delimiter) == str):
            raise Exception("Data text delimiter should be a of type string.")
        self._TEXT_DATA_DELIMITER = delimiter
