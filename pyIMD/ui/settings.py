from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal, QRegExp
from PyQt5.Qt import QValidator, QDoubleValidator, QRegExpValidator, QStyle, QDialog
from pyIMD.configuration.defaults import *

__author__ = 'Andreas P. Cuny'


class Settings(QDialog):

    settings_has_changed = pyqtSignal(dict, name='settings_has_changed')
    send_to_console = pyqtSignal(str)

    def __init__(self, settings_dictionary):
        """
        Constructor.
        """
        super(Settings, self).__init__()
        uic.loadUi('setting_dialog.ui', self)
        # self.setupUi(self)
        self.setWindowTitle('pyIMD :: Settings')
        self.settingsIcon = QIcon()
        self.settingsIcon.addPixmap(self.style().standardPixmap(QStyle.SP_FileDialogDetailedView), QIcon.Disabled,
                                    QIcon.Off)
        self.setWindowIcon(self.settingsIcon)

        self.settings_dictionary = settings_dictionary

        # Establish connections
        self.defaultBtn.clicked.connect(self.set_defaults)
        self.commitBtn.clicked.connect(self.commit_parameters)
        self.cancelBtn.clicked.connect(self.close_dialog)

        double_validator = QDoubleValidator()
        self.figure_width_edit.setValidator(double_validator)
        self.figure_width_edit.textChanged.connect(self.check_state)
        self.figure_height_edit.setValidator(double_validator)
        self.figure_height_edit.textChanged.connect(self.check_state)
        self.figure_resolution_edit.setValidator(double_validator)
        self.figure_resolution_edit.textChanged.connect(self.check_state)
        self.conversion_factor_hz_edit.setValidator(double_validator)
        self.conversion_factor_hz_edit.textChanged.connect(self.check_state)
        self.conversion_factor_deg_edit.setValidator(double_validator)
        self.conversion_factor_deg_edit.textChanged.connect(self.check_state)
        self.spring_constant_edit.setValidator(double_validator)
        self.spring_constant_edit.textChanged.connect(self.check_state)
        self.read_text_data_from_line_edit.setValidator(double_validator)
        self.read_text_data_from_line_edit.textChanged.connect(self.check_state)

        reg_ex = QRegExp("[0-9-a-z-A-Z_]+")
        self.figure_name_wo_cell_edit.setValidator(QRegExpValidator(reg_ex, self.figure_name_wo_cell_edit))
        self.figure_name_wo_cell_edit.textChanged.connect(self.check_state)
        self.figure_name_w_cell_edit.setValidator(QRegExpValidator(reg_ex, self.figure_name_w_cell_edit))
        self.figure_name_w_cell_edit.textChanged.connect(self.check_state)
        self.figure_name_data_edit.setValidator(QRegExpValidator(reg_ex, self.figure_name_data_edit))
        self.figure_name_data_edit.textChanged.connect(self.check_state)

        self.figure_unit_edit.setValidator(QRegExpValidator(QRegExp("[a-z-A-Z_]+"), self.figure_name_wo_cell_edit))
        self.figure_unit_edit.textChanged.connect(self.check_state)

        self.figure_format_edit.setValidator(QRegExpValidator(QRegExp(".+[a-z-A-Z_]"), self.figure_name_wo_cell_edit))
        self.figure_format_edit.textChanged.connect(self.check_state)
        self.text_data_delimiter_edit.setValidator(QRegExpValidator(QRegExp("(?:\\\{1}\w*)"),
                                                                    self.text_data_delimiter_edit))
        self.text_data_delimiter_edit.textChanged.connect(self.check_state)

        self.intial_param_guess_edit.setValidator(QRegExpValidator(QRegExp("(?:\\[\d+.+,\s*)+\d+.+\\]{1}"),
                                                                     self.intial_param_guess_edit))
        self.intial_param_guess_edit.textChanged.connect(self.check_state)

        self.lower_param_bound_edit.setValidator(QRegExpValidator(QRegExp("(?:\\[\d+.+,\s*)+\d+.+\\]{1}"),
                                                                    self.lower_param_bound_edit))
        self.lower_param_bound_edit.textChanged.connect(self.check_state)

        self.upper_param_bound_edit.setValidator(QRegExpValidator(QRegExp("(?:\\[\d+.+,\s*)+\d+.+\\]{1}"),
                                                                    self.upper_param_bound_edit))
        self.upper_param_bound_edit.textChanged.connect(self.check_state)

    def set_defaults(self):
        """
        Set parameters default values.
        :return: void
        """
        # Set default values
        self.figure_format_edit.setText(str(FIGURE_FORMAT))
        self.figure_width_edit.setText(str(FIGURE_WIDTH))
        self.figure_height_edit.setText(str(FIGURE_HEIGHT))
        self.figure_unit_edit.setText(str(FIGURE_UNITS))
        self.figure_resolution_edit.setText(str(FIGURE_RESOLUTION_DPI))
        self.figure_name_wo_cell_edit.setText(str(FIGURE_NAME_PRE_START_NO_CELL))
        self.figure_name_w_cell_edit.setText(str(FIGURE_NAME_PRE_START_WITH_CELL))
        self.figure_name_data_edit.setText(str(FIGURE_NAME_MEASURED_DATA))
        self.conversion_factor_hz_edit.setText(str(CONVERSION_FACTOR_HZ_TO_KHZ))
        self.conversion_factor_deg_edit.setText(str(CONVERSION_FACTOR_DEG_TO_RAD))
        self.spring_constant_edit.setText(str(SPRING_CONSTANT))
        self.intial_param_guess_edit.setText(str(INITIAL_PARAMETER_GUESS))
        self.lower_param_bound_edit.setText(str(LOWER_PARAMETER_BOUNDS))
        self.upper_param_bound_edit.setText(str(UPPER_PARAMETER_BOUNDS))
        self.read_text_data_from_line_edit.setText(str(READ_TEXT_DATA_FROM_LINE))
        self.text_data_delimiter_edit.setText(repr(TEXT_DATA_DELIMITER).replace("'", ""))

    def set_values(self):
        """
        Set parameter values.
        """
        # Set default
        self.figure_format_edit.setText(str(self.settings_dictionary['figure_format']))
        self.figure_width_edit.setText(str(self.settings_dictionary['figure_width']))
        self.figure_height_edit.setText(str(self.settings_dictionary['figure_height']))
        self.figure_unit_edit.setText(str(self.settings_dictionary['figure_units']))
        self.figure_resolution_edit.setText(str(self.settings_dictionary['figure_resolution_dpi']))
        self.figure_name_wo_cell_edit.setText(str(self.settings_dictionary['figure_name_pre_start_no_cell']))
        self.figure_name_w_cell_edit.setText(str(self.settings_dictionary['figure_name_pre_start_with_cell']))
        self.figure_name_data_edit.setText(str(self.settings_dictionary['figure_name_measured_data']))
        self.conversion_factor_hz_edit.setText(str(self.settings_dictionary['conversion_factor_hz_to_khz']))
        self.conversion_factor_deg_edit.setText(str(self.settings_dictionary['conversion_factor_deg_to_rad']))
        self.spring_constant_edit.setText(str(self.settings_dictionary['spring_constant']))
        self.intial_param_guess_edit.setText(str(self.settings_dictionary['initial_parameter_guess']))
        self.lower_param_bound_edit.setText(str(self.settings_dictionary['lower_parameter_bounds']))
        self.upper_param_bound_edit.setText(str(self.settings_dictionary['upper_parameter_bounds']))
        self.read_text_data_from_line_edit.setText(str(self.settings_dictionary['read_text_data_from_line']))
        self.text_data_delimiter_edit.setText((self.settings_dictionary['text_data_delimiter']))
        # self.text_data_delimiter_edit.setText(repr(self.settings_dictionary['text_data_delimiter']).replace("'", ""))

    def commit_parameters(self):
        """
        Close dialog without updating parameters.
        :return: void
        """

        has_changed = False

        figure_format = str(self.figure_format_edit.text())
        if not self.settings_dictionary["figure_format"] == figure_format:
            self.settings_dictionary["figure_format"] = figure_format
            has_changed = True

        figure_width = float(self.figure_width_edit.text())
        if not self.settings_dictionary["figure_width"] == figure_width:
            self.settings_dictionary["figure_width"] = figure_width
            has_changed = True

        figure_height = float(self.figure_height_edit.text())
        if not self.settings_dictionary["figure_height"] == figure_height:
            self.settings_dictionary["figure_height"] = figure_height
            has_changed = True

        figure_unit = str(self.figure_unit_edit.text())
        if not self.settings_dictionary["figure_units"] == figure_unit:
            self.settings_dictionary["figure_units"] = figure_unit
            has_changed = True

        figure_resolution = int(self.figure_resolution_edit.text())
        if not self.settings_dictionary["figure_resolution_dpi"] == figure_resolution:
            self.settings_dictionary["figure_resolution_dpi"] = figure_resolution
            has_changed = True

        figure_name_no_cell = str(self.figure_name_wo_cell_edit.text())
        if not self.settings_dictionary["figure_name_pre_start_no_cell"] == figure_name_no_cell:
            self.settings_dictionary["figure_name_pre_start_no_cell"] = figure_name_no_cell
            has_changed = True

        figure_name_with_cell = str(self.figure_name_w_cell_edit.text())
        if not self.settings_dictionary["figure_name_pre_start_with_cell"] == figure_name_with_cell:
            self.settings_dictionary["figure_name_pre_start_with_cell"] = figure_name_with_cell
            has_changed = True

        figure_name_measured = str(self.figure_name_data_edit.text())
        if not self.settings_dictionary["figure_name_measured_data"] == figure_name_measured:
            self.settings_dictionary["figure_name_measured_data"] = figure_name_measured
            has_changed = True

        conversion_factor_hz = float(self.conversion_factor_hz_edit.text())
        if not self.settings_dictionary["conversion_factor_hz_to_khz"] == conversion_factor_hz:
            self.settings_dictionary["conversion_factor_hz_to_khz"] = conversion_factor_hz
            has_changed = True

        conversion_factor_deg = float(self.conversion_factor_deg_edit.text())
        if not self.settings_dictionary["conversion_factor_deg_to_rad"] == conversion_factor_deg:
            self.settings_dictionary["conversion_factor_deg_to_rad"] = conversion_factor_deg
            has_changed = True

        spring_constant = float(self.spring_constant_edit.text())
        if not self.settings_dictionary["spring_constant"] == spring_constant:
            self.settings_dictionary["spring_constant"] = spring_constant
            has_changed = True

        initial_guess = str(self.intial_param_guess_edit.text())
        if not self.settings_dictionary["initial_parameter_guess"] == initial_guess:
            self.settings_dictionary["initial_parameter_guess"] = initial_guess
            has_changed = True

        lower_bound = str(self.lower_param_bound_edit.text())
        if not self.settings_dictionary["lower_parameter_bounds"] == lower_bound:
            self.settings_dictionary["lower_parameter_bounds"] = lower_bound
            has_changed = True

        upper_bound = str(self.upper_param_bound_edit.text())
        if not self.settings_dictionary["upper_parameter_bounds"] == upper_bound:
            self.settings_dictionary["upper_parameter_bounds"] = upper_bound
            has_changed = True

        read_from_line = int(self.read_text_data_from_line_edit.text())
        if not self.settings_dictionary["read_text_data_from_line"] == read_from_line:
            self.settings_dictionary["read_text_data_from_line"] = read_from_line
            has_changed = True

        delimiter = str(self.text_data_delimiter_edit.text())
        if not self.settings_dictionary["text_data_delimiter"] == delimiter:
           self.settings_dictionary["text_data_delimiter"] = delimiter
           has_changed = True

        # Emit a signal
        if has_changed:
            self.settings_has_changed.emit(self.settings_dictionary)

        self.print_to_console("Parameters updated")
        # Close the dialog
        self.close()

    def check_state(self):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if state == QValidator.Acceptable:
            color = '#c4df9b'  # Green
        elif state == QValidator.Intermediate:
            color = '#fff79a'  # Yellow
        else:
            color = '#f6989d'  # Red
        sender.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def print_to_console(self, string):
        self.send_to_console.emit(string)

    def close_dialog(self):
        """
        Close dialog without updating parameters.
        :return: void
        """
        self.close()
