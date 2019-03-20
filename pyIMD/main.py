import sys
from PyQt5.QtWidgets import QApplication
from pyIMD.ui.main_ui import IMDWindow


def show_ui():
    app = QApplication(sys.argv)
    main = IMDWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = IMDWindow()
    main.show()
    sys.exit(app.exec_())
