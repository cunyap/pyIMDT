import os
import sys
import datetime
import pathlib
import ctypes
import xmltodict
from lxml import etree
from ast import literal_eval
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.Qt import QAction, QFileDialog, QScrollArea, QMessageBox, QApplication, QStyle, QTextCursor, QIcon, \
     QPushButton, QListWidget, QSize
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QFileSystemWatcher, QThreadPool
from PyQt5.QtWidgets import QGraphicsView
from pyIMD.ui.settings import Settings
from pyIMD.ui.file_viewer import FileViewer
from pyIMD.configuration.defaults import *
from pyIMD.inertialmassdetermination import InertialMassDetermination
from pyIMD.ui.table_view_model import PandasDataFrameModel
from pyIMD.ui.graphics_rendering import GraphicScene
from concurrent.futures import ThreadPoolExecutor
from pyIMD.ui.resource_path import resource_path
from pyIMD.__init__ import __version__, __operating_system__

__author__ = 'Andreas P. Cuny'


class Stream(QtCore.QObject):
    newText = QtCore.pyqtSignal(str)

    def write(self, text: object) -> object:
        self.newText.emit(str(text))


class IMDWindow(QtWidgets.QMainWindow):

    signal_file_index_changed = pyqtSignal(int, name='file_index_changed')
    send_to_console = pyqtSignal(str)

    def __init__(self):
        super(IMDWindow, self).__init__()
        uic.loadUi(resource_path(os.path.join('ui', 'main_window.ui')), self)
        self.setWindowTitle('pyIMD: Inertial mass determination [build: v%s %s]' % (__version__, __operating_system__))
        self.setWindowIcon(QtGui.QIcon(resource_path(os.path.join(os.path.join("ui", "icons",
                                                                               "pyimd_logo2_01_FNf_icon.ico")))))
        app_id = u'ethz.csb.pyIMD.v0_0_1'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
        self.settings_dialog = None
        self.about_window = None
        self.file_viewer = None
        self.figure_viewer = None
        self.result_data_viewer = None
        self.file_list = []
        self.current_file_index = []
        self.figure_list = []
        self.current_figure_index = []
        self.current_batch_project_file = []
        self.last_selected_path = ''
        self.show()
        self.console_edit.setReadOnly(True)
        self.radio_btn_name_array = ['autoRadio', 'pllRadio', 'contSweepRadio']
        self.opening_mode = 0
        self.thread = None
        self.threadpool = QThreadPool()
        self.obj = None
        self.task_done = False
        self.executor = ThreadPoolExecutor(max_workers=4)

        # Settings
        self.__settings = {"figure_format": FIGURE_FORMAT,
                           "figure_width": FIGURE_WIDTH,
                           "figure_height": FIGURE_HEIGHT,
                           "figure_units": FIGURE_UNITS,
                           "figure_resolution_dpi": FIGURE_RESOLUTION_DPI,
                           "figure_name_pre_start_no_cell": FIGURE_NAME_PRE_START_NO_CELL,
                           "figure_name_pre_start_with_cell": FIGURE_NAME_PRE_START_WITH_CELL,
                           "figure_name_measured_data": FIGURE_NAME_MEASURED_DATA,
                           "conversion_factor_hz_to_khz": CONVERSION_FACTOR_HZ_TO_KHZ,
                           "conversion_factor_deg_to_rad": CONVERSION_FACTOR_DEG_TO_RAD,
                           "spring_constant": SPRING_CONSTANT,
                           "initial_parameter_guess": INITIAL_PARAMETER_GUESS,
                           "lower_parameter_bounds": LOWER_PARAMETER_BOUNDS,
                           "upper_parameter_bounds": UPPER_PARAMETER_BOUNDS,
                           "read_text_data_from_line": READ_TEXT_DATA_FROM_LINE,
                           "text_data_delimiter": repr(TEXT_DATA_DELIMITER).replace("'", "")}

        self.settings_dialog = Settings(self.__settings)
        self.settings_dialog.set_values()
        self.setup_console_connection()
        self.selectDirBtn.clicked.connect(self.select_data_files)
        # self.signal_file_index_changed.connect(self.handle_changed_file_index)
        self.setup_file_viewer()
        self.setup_figure_viewer()

        data_items = ['Measured data', 'Pre start no cell data', 'Pre start with cell data', 'Calculated cell mass']
        for i in range(0, len(data_items)):
            self.dataList.addItem(str(data_items[i]))
        self.dataList.itemSelectionChanged.connect(self.on_data_list_selection_changed)
        self.noCellDataBox.currentIndexChanged.connect(self.on_combo_box_changed)
        self.withCellDataBox.currentIndexChanged.connect(self.on_combo_box_changed)
        self.measuredDataBox.currentIndexChanged.connect(self.on_combo_box_changed)
        self.runCalculationBtn.clicked.connect(self.run_calculation)
        self.projectFilesBtn.clicked.connect(self.select_batch_files)
        self.runBatchBtn.clicked.connect(self.run_batch_calculation)

        self.actionView_Console.setIcon(QApplication.style().standardIcon(QStyle.SP_DialogApplyButton))
        self.actionView_Console.setShortcut("Ctrl+C")
        self.actionView_Console.setStatusTip('Show / hide console console')
        self.actionView_Console.triggered.connect(self.view_console)

        self.actionQuit.setIcon(QApplication.style().standardIcon(QStyle.SP_DialogCloseButton))
        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionQuit.setStatusTip('Quit the application')
        self.actionQuit.triggered.connect(self.close_application)

        self.actionSave_project.setIcon(QApplication.style().standardIcon(QStyle.SP_DialogSaveButton))
        self.actionSave_project.setShortcut("Ctrl+S")
        self.actionSave_project.setStatusTip('Save a pyIMD project')
        self.actionSave_project.triggered.connect(self.save_project)

        self.actionOpen_project.setIcon(QApplication.style().standardIcon(QStyle.SP_DirOpenIcon))
        self.actionOpen_project.setShortcut("Ctrl+O")
        self.actionOpen_project.setStatusTip('Open a pyIMD project')
        self.actionOpen_project.triggered.connect(self.open_project)

        self.actionSettings.setIcon(QApplication.style().standardIcon(QStyle.SP_FileDialogDetailedView))
        self.actionSettings.setShortcut("Ctrl+P")
        self.actionSettings.setStatusTip('Configure pyIMD calculation settings')
        self.actionSettings.triggered.connect(self.show_settings_dialog)

        about_action = QAction("About", self.menuBar)
        about_action.setShortcut("Ctrl+A")
        about_action.triggered.connect(self.show_about_dialog)
        self.menuBar.addAction(about_action)

        sys.stderr = Stream(newText=self.on_update_text)

        self.file_system_watcher = QFileSystemWatcher()
        self.file_system_watcher.directoryChanged.connect(self.on_folder_change)

        self.batchFileListWidget.setSelectionMode(QListWidget.MultiSelection)
        self.tabWidget.setTabEnabled(2, False)
        self.tabWidget.setCurrentIndex(0)

        self.scene = GraphicScene()
        self.scene.signalMoveOffset.connect(self.on_image_pan)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setViewportUpdateMode(
            QGraphicsView.FullViewportUpdate)
        self.graphicsView.setDragMode(QGraphicsView.RubberBandDrag)
        self.graphicsView.setMouseTracking(True)

    def on_image_pan(self, offset):
        try:
            self.graphicsView.verticalScrollBar().setValue(self.graphicsView.verticalScrollBar().value() + offset.y())
            self.graphicsView.horizontalScrollBar().setValue(self.graphicsView.horizontalScrollBar().value() + offset.x())
        except Exception as e:
            self.print_to_console("Error scrolling: " + str(e))

    def on_folder_change(self):
        # Try to add images to list and then plot
        file_list = []
        for file in pathlib.Path(self.last_selected_path).glob('*.png'):
            file_list.append(file)

        self.figure_list = []
        for idx in range(0, len(file_list)):
            self.figure_list.append(str(file_list[idx]))

        self.figure_viewer.set_data([], self.figure_list)

    def on_update_text(self, text):
        cursor = self.console_edit.textCursor()
        cursor.movePosition(QTextCursor.NoMove)
        cursor.insertText(text)
        self.console_edit.setTextCursor(cursor)
        self.console_edit.ensureCursorVisible()

    def view_console(self):
        if self.consoleDock.isVisible():
            self.consoleDock.hide()
            self.actionView_Console.setIcon(QApplication.style().standardIcon(QStyle.SP_DialogCancelButton))
        else:
            self.consoleDock.show()
            self.actionView_Console.setIcon(QApplication.style().standardIcon(QStyle.SP_DialogApplyButton))

    def run_calculation(self):

        if self.autoRadio.isChecked():
            self.print_to_console("Auto mode not implemented yet: ")
        elif self.contSweepRadio.isChecked():
            self.print_to_console("Sweep mode starting...")
            self.print_to_console('')  # Needed to output logging information to newline in console
            self.obj = InertialMassDetermination(self.noCellDataBox.currentText(), self.withCellDataBox.currentText(),
                                                 self.measuredDataBox.currentText(),
                                                 self.__settings["text_data_delimiter"],
                                                 int(self.__settings["read_text_data_from_line"]), 0)
            self.update_settings()

            task = self.executor.submit(self.obj.run_intertial_mass_determination)
            task.add_done_callback(self.on_task_finished)

        elif self.pllRadio.isChecked():
            self.print_to_console("PLL mode starting...")

            self.print_to_console('')  # Needed to output logging information to newline in console
            self.obj = InertialMassDetermination(self.noCellDataBox.currentText(), self.withCellDataBox.currentText(),
                                                 self.measuredDataBox.currentText(),
                                                 self.__settings["text_data_delimiter"],
                                                 int(self.__settings["read_text_data_from_line"]), 1)
            self.update_settings()

            task = self.executor.submit(self.obj.run_intertial_mass_determination)
            task.add_done_callback(self.on_task_finished)

    def on_task_finished(self, task):
        self.tabWidget.setTabEnabled(2, True)
        self.task_done = True

    def run_batch_calculation(self):

        selected_project_files = []
        for item in self.batchFileListWidget.selectedItems():
            selected_project_files.append(item.text())

        if len(selected_project_files) != 0:
            self.print_to_console("Batch calculation mode starting...")
            for iProject in range(0,len(selected_project_files)):
                self.current_batch_project_file = selected_project_files[iProject]  # here iterate over project files
                print(self.current_batch_project_file)
                # 1. Open Project from list
                self.open_project()
                # 2. Run
                self.run_calculation()
                # 3. Get signal that it is done
                # Start again

    def on_combo_box_changed(self, index):
        sender = self.sender().objectName()
        if sender == 'noCellDataBox':
            self.print_to_console("Pre start no cell file selected:" + self.file_list[index])
        elif sender == 'withCellDataBox':
            self.print_to_console("Pre start with cell file selected:" + self.file_list[index])
        elif sender == 'measuredDataBox':
            self.print_to_console("Measurement file selected:" + self.file_list[index])

    def on_data_list_selection_changed(self):
        item = self.dataList.selectedItems()[0]
        try:
            if item.text() == 'Measured data':
                # Display data
                model = PandasDataFrameModel(self.obj.data_measured)
                self.tableView.setModel(model)
                # Notify user about selection
                self.print_to_console("Displaying: " + item.text())

            elif item.text() == 'Pre start no cell data':
                # Display data
                model = PandasDataFrameModel(self.obj.data_pre_start_no_cell)
                self.tableView.setModel(model)
                # Notify user about selection
                self.print_to_console("Displaying: " + item.text())

            elif item.text() == 'Pre start with cell data':
                # Display data
                model = PandasDataFrameModel(self.obj.data_pre_start_with_cell)
                self.tableView.setModel(model)
                # Notify user about selection
                self.print_to_console("Displaying: " + item.text())

            elif item.text() == 'Calculated cell mass':
                # Display data
                model = PandasDataFrameModel(self.obj.calculated_cell_mass)
                self.tableView.setModel(model)
                # Notify user about selection
                self.print_to_console("Displaying: " + item.text())
            else:
                return
        except Exception as e:
            self.print_to_console("Error no pyIMD object yet. Please run calculation first: " + str(e))

    def select_data_files(self):
        """
        Select data files.
        """
        try:
            filter_ext = "All files (*.*);; Txt (*.txt);; TDMS (*.tdms);;"
            file_name = QFileDialog()
            file_name.setFileMode(QFileDialog.ExistingFiles)
            ret = file_name.getOpenFileNames(self, "Pick relevant data files",
                                             self.last_selected_path, filter_ext)
            names = ret[0]
            if len(names) > 0:
                # Clear previous file list
                self.file_list = []
                # Setting the file list
                self.file_list = names
                sorted_file_list = self.file_list
                self.last_selected_path = os.path.dirname(sorted_file_list[0])
                self.current_file_index = 0
                self.show_files()
                self.print_to_console("Selected %d files." % (len(sorted_file_list)))

            # Populate drop down list with selected items.
            self.noCellDataBox.clear()
            self.withCellDataBox.clear()
            self.measuredDataBox.clear()
            self.noCellDataBox.addItems(self.file_list)
            self.withCellDataBox.addItems(self.file_list)
            self.measuredDataBox.addItems(self.file_list)
            # Add path to system watcher
            self.file_system_watcher.addPaths([self.last_selected_path])
        except Exception as e:
            self.print_to_console("Error could not select files." + str(e))

    def select_batch_files(self):
        """
        Selection of .xml pyIMD project files for batch calculation.
        """
        filter_ext = "XML (*.xml);;, All files (*.*) "
        file_name = QFileDialog()
        file_name.setFileMode(QFileDialog.ExistingFiles)
        ret = file_name.getOpenFileNames(self, "Select the pyIMD project files for batch processing",
                                         self.last_selected_path, filter_ext)
        files = ret[0]
        for i in range(0, len(files)):
            self.batchFileListWidget.addItem(str(files[i]))

    def show_data(self):
        """
        Display the data names om the file viewer.
        """
        data_list = [self.obj.data_measured, self.obj.data_pre_start_no_cell, self.obj.data_pre_start_with_cell,
                     self.obj.calculated_cell_mass]
        self.file_viewer.set_data([], data_list)
        # model = PandasDataFrameModel(data_list[0])
        # self.tableView.setModel(model)

    def show_files(self):
        """
        Display the file names om the file viewer.
        """
        self.file_viewer.set_data([], self.file_list)

    def show_about_dialog(self):
        """
        Show about message box.
        """

        msg_box = QMessageBox(self)
        about_icon = QIcon()
        about_icon.addPixmap(self.style().standardPixmap(QStyle.SP_FileDialogInfoView))
        msg_box.setWindowIcon(about_icon)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle('pyIMD :: About')
        msg_box.setText('pyIMD: Inertial mass determination.\n[build: v%s %s]\n\nWritten by Andreas P. '
                        'Cuny' % (__version__, __operating_system__))
        msg_box.setInformativeText("(c) Copyright Andreas P. Cuny \n2018. All rights reserved."
                                   "\nAndreas P. Cuny \nETHZ CSB Laboratory\nMattenstrasse 26 \n4058 Basel")
        msg_box.addButton(QMessageBox.Close)
        msg_box.setIconPixmap(QtGui.QPixmap(resource_path(os.path.join("icons", "pyIMD_Logo2-01.png"))))
        msg_box.show()

    def show_change_log_dialog(self):
        """
        Show change log message box.
        """
        change_log = '- 0.0.3 \n' \
                     '           - New feature: Added image montage generator to pyIMD.plotting.figures \n' \
                     '           - New feature: Batch project calculation \n' \
                     '           - Fixed Bug: Reading project xml file did not recognize file delimiter properly. \n' \
                     '- 0.0.2 \n' \
                     '           - Fixed Bug: Opening multiple projects in a row did not update drop down menus.\n' \
                     '- 0.0.1 \n' \
                     '           - Alpha Pre release. \n'

        self.change_log_text.setText(change_log)

    def show_settings_dialog(self):
        """
        Show the settings dialog.
        """
        if self.settings_dialog is None:
            self.settings_dialog = Settings(self.__settings)
            self.settings_dialog.settings_has_changed.connect(
                self.on_settings_changed)

        self.settings_dialog.exec()

    @pyqtSlot(dict, name="on_settings_changed")
    def on_settings_changed(self, changed_settings):
        """
        Update settings
        :return: void
        """

        # Update the settings
        self.__settings = changed_settings

    def setup_console_connection(self):
        self.settings_dialog.send_to_console.connect(self.handle_change_console_text)

    def print_to_console(self, string):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
        self.console_edit.append(current_time + string)

    @pyqtSlot(int, name="handle_changed_file_index")
    def handle_changed_file_index(self, i):
        """
        :param i: new file index.
        """
        if i > len(self.file_list) - 1:
            self.print_to_console("Please load a data file first!")
            return

        self.current_file_index = i
        self.print_to_console("Currently selected file: " + self.file_list[i])

    @pyqtSlot(int, name="handle_changed_figure_index")
    def handle_changed_figure_index(self, i):
        """
        :param i: new figure index.
        """
        if i > len(self.figure_list) - 1:
            self.print_to_console("Please load a figure file first!")
            return
        try:
            self.scene.clear()
            self.scene.display_image(self.figure_list[i])
            self.scene.redraw()

        except Exception as e:
            self.print_to_console("Error could not open figure: " + str(e))

        self.current_figure_index = i
        self.print_to_console("Currently selected figure: " + self.figure_list[i])

    def setup_file_viewer(self):
        """
        Set up the file viewer.
        """

        # Initialize widget if need
        if self.file_viewer is None:
            self.file_viewer = FileViewer()

        # Connect the signal
        self.file_viewer.signal_file_index_changed.connect(
            self.handle_changed_file_index)
        # Add a scroll area
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.file_viewer)
        self.gridLayout.addWidget(scroll_area, 2, 0)
        # Show the widget
        self.file_viewer.show()

    def setup_figure_viewer(self):
        """
        Set up the figure viewer.
        """

        # Initialize widget if need
        if self.figure_viewer is None:
            self.figure_viewer = FileViewer()
        # Connect the signal
        self.figure_viewer.signal_file_index_changed.connect(
            self.handle_changed_figure_index)
        # Add a scroll area
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.figure_viewer)
        self.gridLayoutResultTab.addWidget(scroll_area, 1, 0)
        # Show the widget
        self.figure_viewer.show()

    @pyqtSlot(str, name="handle_change_console_text")
    def handle_change_console_text(self, string):
        """
        :param string: String received from Settings instance to print to the console.
        """
        self.print_to_console(string)

    def save_project(self):
        """
        Saves a pyIMD project file as .xml
        """

        file_dialog = QFileDialog()
        project_file_dir = file_dialog.getSaveFileName(self)

        if len(project_file_dir[0]) > 0:
            try:
                # Create the root element
                root = etree.Element('PyIMDSettings', creator='pyIMD',
                                 timestamp=datetime.datetime.now().strftime('%Y_%m_%d__%H_%M_%S'))
                # Make a new document tree
                doc = etree.ElementTree(root)
                # Add the SubElements
                general_settings = etree.SubElement(root, 'GeneralSettings')
                ui_settings = etree.SubElement(root, 'UiSettings')
                selected_files = etree.SubElement(ui_settings, 'SelectedFiles')
                # Add the SubSubElements for the general settings
                figure_format = etree.SubElement(general_settings, 'figure_format')
                figure_width = etree.SubElement(general_settings, 'figure_width')
                figure_height = etree.SubElement(general_settings, 'figure_height')
                figure_units = etree.SubElement(general_settings, 'figure_units')
                figure_resolution = etree.SubElement(general_settings, 'figure_resolution_dpi')
                figure_name_pre_start_no_cell = etree.SubElement(general_settings, 'figure_name_pre_start_no_cell')
                figure_name_pre_start_with_cell = etree.SubElement(general_settings, 'figure_name_pre_start_with_cell')
                figure_name_measured_data = etree.SubElement(general_settings, 'figure_name_measured_data')
                conversion_factor_hz_to_khz = etree.SubElement(general_settings, 'conversion_factor_hz_to_khz')
                conversion_factor_deg_to_rad = etree.SubElement(general_settings, 'conversion_factor_deg_to_rad')
                spring_constant = etree.SubElement(general_settings, 'spring_constant')
                initial_parameter_guess = etree.SubElement(general_settings, 'initial_parameter_guess')
                lower_parameter_bounds = etree.SubElement(general_settings, 'lower_parameter_bounds')
                upper_parameter_bounds = etree.SubElement(general_settings, 'upper_parameter_bounds')
                read_text_data_from_line = etree.SubElement(general_settings, 'read_text_data_from_line')
                text_data_delimiter = etree.SubElement(general_settings, 'text_data_delimiter')
                # Add the SubSubElements for the ui settings
                project_folder_path = etree.SubElement(ui_settings, 'ProjectFolderPath')
                data_pre_start_no_cell = etree.SubElement(ui_settings, 'SelectedDataPreStartNoCell')
                data_pre_start_with_cell = etree.SubElement(ui_settings, 'SelectedDataPreStartWithCell')
                data_measured = etree.SubElement(ui_settings, 'SelectedDataMeasured')
                calculation_mode = etree.SubElement(ui_settings, 'CalculationMode')

                # Add the data
                figure_format.text = str(self.__settings["figure_format"])
                figure_width.text = str(self.__settings["figure_width"])
                figure_height.text = str(self.__settings["figure_height"])
                figure_units.text = str(self.__settings["figure_units"])
                figure_resolution.text = str(self.__settings["figure_resolution_dpi"])
                figure_name_pre_start_no_cell.text = str(self.__settings["figure_name_pre_start_no_cell"])
                figure_name_pre_start_with_cell.text = str(self.__settings["figure_name_pre_start_with_cell"])
                figure_name_measured_data.text = str(self.__settings["figure_name_measured_data"])
                conversion_factor_hz_to_khz.text = str(self.__settings["conversion_factor_hz_to_khz"])
                conversion_factor_deg_to_rad.text = str(self.__settings["conversion_factor_deg_to_rad"])
                spring_constant.text = str(self.__settings["spring_constant"])
                initial_parameter_guess.text = str(self.__settings["initial_parameter_guess"])
                lower_parameter_bounds.text = str(self.__settings["lower_parameter_bounds"])
                upper_parameter_bounds.text = str(self.__settings["upper_parameter_bounds"])
                read_text_data_from_line.text = str(self.__settings["read_text_data_from_line"])
                text_data_delimiter.text = self.__settings["text_data_delimiter"]
                project_folder_path.text = self.last_selected_path
                data_pre_start_no_cell.text = self.noCellDataBox.currentText()
                data_pre_start_with_cell.text = self.withCellDataBox.currentText()
                data_measured.text = self.measuredDataBox.currentText()
                for i in range(0, len(self.radio_btn_name_array)):
                    radio_name = getattr(self, self.radio_btn_name_array[i])
                    if radio_name.isChecked():
                        calculation_mode.text = radio_name.text()

                file_dict = {}
                for i in range(0, len(self.file_list)):
                    file_dict["string{0}".format(i)] = etree.SubElement(selected_files, 'File')
                    file_dict["string{0}".format(i)].text = pathlib.Path(self.file_list[i]).name

                # Check for correct file suffix. If not provided by user or wrong suffix given correct it
                if not pathlib.Path(project_file_dir[0]).suffix:
                    save_file_name = project_file_dir[0] + '.xml'
                elif pathlib.Path(project_file_dir[0]).suffix != '.xml':
                    project_file_dir[0].suffix = '.xml'
                    save_file_name = project_file_dir[0]
                else:
                    save_file_name = project_file_dir[0]

                # Save to XML file
                doc.write(save_file_name, xml_declaration=True, encoding='utf-8', method="xml", standalone=False,
                          pretty_print=True)

                self.print_to_console("Project saved successfully")
            except Exception as e:
                self.print_to_console("Error during saving project: " + str(e))
        else:
            self.print_to_console("Project saving aborted by user")

    def open_project(self):
        """
        Opens a pyIMD project file (.xml)
        """

        # Quick hack to distinguish action depending on sender
        if self.sender().objectName() == 'actionOpen_project':

            project_filter_ext = "XML (*.xml);; All files (*.*)"
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFiles)
            selected_project_file = file_dialog.getOpenFileName(self, "Select a pyIMD project file",
                                                                self.last_selected_path, project_filter_ext)
            print('opened using dialog')
        else:
            selected_project_file = [self.current_batch_project_file]
            print('direct opening')

        if len(selected_project_file[0]) > 0:
            try:
                with open(selected_project_file[0]) as fd:
                    doc = xmltodict.parse(fd.read())

                self.__settings = doc['PyIMDSettings']['GeneralSettings']
                # fix escape characters ie \\t or \\n or \\s
                self.__settings['text_data_delimiter'] = self.__settings['text_data_delimiter'].replace("'", "")
                # self.__settings['text_data_delimiter'].encode().decode('unicode_escape')

                # Update settings dialog with opened project data
                self.settings_dialog.settings_dictionary = self.__settings
                self.settings_dialog.set_values()

                # Update ui with loaded data:
                ui_settings = doc['PyIMDSettings']['UiSettings']
                self.last_selected_path = ui_settings['ProjectFolderPath']
                self.file_system_watcher.addPaths([self.last_selected_path])
                files = ui_settings['SelectedFiles']['File']

                self.file_list = []
                for i in range(0, len(files)):
                    self.file_list.append(pathlib.Path().joinpath(self.last_selected_path, files[i]).as_posix())

                self.show_files()
                self.noCellDataBox.clear()
                self.noCellDataBox.addItems(self.file_list)
                index = self.noCellDataBox.findText(ui_settings['SelectedDataPreStartNoCell'], QtCore.Qt.MatchFixedString)

                if index >= 0:
                    self.noCellDataBox.setCurrentIndex(index)

                self.withCellDataBox.clear()
                self.withCellDataBox.addItems(self.file_list)
                index = self.withCellDataBox.findText(ui_settings['SelectedDataPreStartWithCell'], QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.withCellDataBox.setCurrentIndex(index)

                self.measuredDataBox.clear()
                self.measuredDataBox.addItems(self.file_list)
                index = self.measuredDataBox.findText(ui_settings['SelectedDataMeasured'], QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.measuredDataBox.setCurrentIndex(index)

                for i in range(0, len(self.radio_btn_name_array)):
                    radio_name = getattr(self, self.radio_btn_name_array[i])
                    if radio_name.text() == ui_settings['CalculationMode']:
                        radio_name.setChecked(True)

                self.print_to_console("Project {} successfully opened".format(pathlib.Path(selected_project_file[0]).name))
            except Exception as e:
                self.print_to_console("Error during opening project: " + str(e))
        else:
            self.print_to_console("Project opening aborted by user")

    def update_settings(self):
        """
        Updates the settings of the pyIMD object
        """

        try:
            self.obj.settings.FIGURE_WIDTH = float(self.__settings["figure_width"])
            self.obj.settings.FIGURE_HEIGHT = float(self.__settings["figure_height"])
            self.obj.settings.FIGURE_UNITS = str(self.__settings["figure_units"])
            self.obj.settings.FIGURE_FORMAT = str(self.__settings["figure_format"])
            self.obj.settings.FIGURE_RESOLUTION_DPI = int(self.__settings["figure_resolution_dpi"])
            self.obj.settings.FIGURE_NAME_PRE_START_NO_CELL = self.__settings["figure_name_pre_start_no_cell"]
            self.obj.settings.FIGURE_NAME_PRE_START_WITH_CELL = self.__settings["figure_name_pre_start_with_cell"]
            self.obj.settings.FIGURE_NAME_MEASURED_DATA = self.__settings["figure_name_measured_data"]
            self.obj.settings.CONVERSION_FACTOR_HZ_TO_KHZ = float(self.__settings["conversion_factor_hz_to_khz"])
            self.obj.settings.CONVERSION_FACTOR_DEG_TO_RAD = float(self.__settings["conversion_factor_deg_to_rad"])
            self.obj.settings.SPRING_CONSTANT = float(self.__settings["spring_constant"])
            self.obj.settings.INITIAL_PARAMETER_GUESS = literal_eval(self.__settings["initial_parameter_guess"])
            self.obj.settings.LOWER_PARAMETER_BOUNDS = literal_eval(self.__settings["lower_parameter_bounds"])
            self.obj.settings.UPPER_PARAMETER_BOUNDS = literal_eval(self.__settings["upper_parameter_bounds"])
            self.obj.settings.READ_TEXT_DATA_FROM_LINE = int(self.__settings["read_text_data_from_line"])
            self.obj.settings.TEXT_DATA_DELIMITER = str(self.__settings["text_data_delimiter"])

        except Exception as e:
            self.print_to_console("Error during opening project: " + str(e))

    def close_application(self, event):
        """
        Opens a message box to handle program exit properly asking the user if the project should be saved first.
        :param event: a QCloseEvent
        :return: 0 when process finished correctly
        """
        msg_box = QMessageBox()
        msg_box.setWindowIcon(QtGui.QIcon(resource_path(os.path.join("icons", "pyimd_logo2_01_FNf_icon.ico"))))
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle('pyIMD :: Quit Program')
        msg_box.setText('Are you sure you want to quit the program?')
        save_btn = QPushButton('Quit WITH saving')
        save_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_DialogSaveButton))
        msg_box.addButton(save_btn, QMessageBox.YesRole)
        no_save_btn = QPushButton('Quit WITHOUT saving')
        no_save_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_DialogNoButton))
        msg_box.addButton(no_save_btn, QMessageBox.NoRole)
        abort_btn = QPushButton('Abort')
        abort_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_DialogCancelButton))
        msg_box.addButton(abort_btn, QMessageBox.RejectRole)
        ret = msg_box.exec_()

        if ret == 0:
            self.save_project()
            if not event:
                self.close()
            else:
                event.accept()
        elif ret == 1:
            if not event:
                self.close()
            else:
                event.accept()
        else:
            self.print_to_console("Program quit aborted")
            if not event:
                return
            else:
                event.ignore()

    def closeEvent(self, event):
        """
        Application close event
        :param event: a QCloseEvent
        :return: 0 when process finished correctly
        """
        self.close_application(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = IMDWindow()
    app_icon = QtGui.QIcon()
    app_icon.addFile(resource_path(os.path.join("icons", "pyimd_logo2_01_FNf_icon.ico")), QSize(256, 256))
    app.setWindowIcon(app_icon)
    sys.exit(app.exec_())
