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
        self.FIGURE_NAME_MEASURED = FIGURE_NAME_MEASURED
        self.CONVERSION_FACTOR_HZ_TO_KHZ = CONVERSION_FACTOR_HZ_TO_KHZ
        self.CONVERSION_FACTOR_DEG_TO_RAD = CONVERSION_FACTOR_DEG_TO_RAD
        self.SPRING_CONSTANT = SPRING_CONSTANT

    FIGURE_FORMAT = property(operator.attrgetter('_FIGURE_FORMAT'))

    @FIGURE_FORMAT.setter
    def FIGURE_FORMAT(self, unit):
        if not (type(unit) == str):
            raise Exception("Figure format should be of type string. 'png' and 'pdf' are valid")
        self._FIGURE_FORMAT = unit

    FIGURE_WIDTH = property(operator.attrgetter('_FIGURE_WIDTH'))

    @FIGURE_WIDTH.setter
    def FIGURE_WIDTH(self, width):
        if not (type(width) == float or (type(width) == int)):
            raise Exception("Figure width should be float")
        self._FIGURE_WIDTH = width

    FIGURE_HEIGHT = property(operator.attrgetter('_FIGURE_HEIGHT'))

    @FIGURE_HEIGHT.setter
    def FIGURE_HEIGHT(self, height):
        if not (type(height) == float or (type(height) == int)):
            raise Exception("Figure height should be of type float")
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

    FIGURE_NAME_MEASURED = property(operator.attrgetter('_FIGURE_NAME_MEASURED'))

    @FIGURE_NAME_MEASURED.setter
    def FIGURE_NAME_MEASURED(self, name):
        if not (type(name) == str):
            raise Exception("Figure name should be a of type string.")
        self._FIGURE_NAME_MEASURED = name

    CONVERSION_FACTOR_HZ_TO_KHZ = property(operator.attrgetter('_CONVERSION_FACTOR_HZ_TO_KHZ'))

    @CONVERSION_FACTOR_HZ_TO_KHZ.setter
    def CONVERSION_FACTOR_HZ_TO_KHZ(self, factor):
        if not (type(factor) == float):
            raise Exception("Conversion factor should be a of type float.")
        self._CONVERSION_FACTOR_HZ_TO_KHZ = factor

    CONVERSION_FACTOR_DEG_TO_RAD = property(operator.attrgetter('_CONVERSION_FACTOR_DEG_TO_RAD'))

    @CONVERSION_FACTOR_DEG_TO_RAD.setter
    def CONVERSION_FACTOR_DEG_TO_RAD(self, factor):
        if not (type(factor) == float):
            raise Exception("Conversion factor should be a of type float.")
        self._CONVERSION_FACTOR_DEG_TO_RAD = factor

    SPRING_CONSTANT = property(operator.attrgetter('_SPRING_CONSTANT'))

    @SPRING_CONSTANT.setter
    def SPRING_CONSTANT(self, spring_constant):
        if not (type(spring_constant) == float):
            raise Exception("Spring constant should be a of type float.")
        self._SPRING_CONSTANT = spring_constant
