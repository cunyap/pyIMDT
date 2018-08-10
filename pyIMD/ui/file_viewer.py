import ntpath
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject
from PyQt5.QtWidgets import QSizePolicy, QAbstractItemView, QTableWidget, QTableWidgetItem, QHeaderView


class FileViewer(QTableWidget, QObject):
    """
    Display files in a QTableWidget.
    """

    signal_file_index_changed = pyqtSignal(int, name='file_index_changed')

    def __init__(self):
        """
        Constructor.
        """
        QTableWidget.__init__(self, 1, 1)
        self.setup()
        self.resizeRowsToContents()
        self.setMinimumWidth(230)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.cellClicked.connect(self.handle_row_clicked)

    def set_data(self, input_files, image_files):
        """
        Displays files.
        """
        # Delete current content
        self.setRowCount(0)
        # Create enough rows to fit the data
        num_elements = max(len(input_files), len(image_files))
        if num_elements == 0:
            self.viewport().update()
            return
        # Fill the table
        self.setRowCount(num_elements)
        for i in range(num_elements):
            try:
                image_file = ntpath.basename(image_files[i])
            except IndexError:
                image_file = ''

            new_item = QTableWidgetItem(ntpath.basename(image_file))
            new_item.setFlags(QtCore.Qt.ItemIsSelectable |
                              QtCore.Qt.ItemIsEnabled)
            self.setItem(i, 0, new_item)

    def setup(self):
        """
        Sets the column headers.
        """
        self.horizontalHeader().hide()
        self.setRowCount(0)
        for i in range(1):
            empty_item = QTableWidgetItem("")
            empty_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.setItem(0, i, empty_item)

        self.horizontalHeader().resizeSection(0, 250)
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)

    @pyqtSlot(int)
    def handle_row_clicked(self, row):
        """
        Emits the index of the row the user selected.

        :param row: row number
        """
        self.signal_file_index_changed.emit(row)

