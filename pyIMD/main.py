import sys
from PyQt5.QtWidgets import QApplication
from pyIMD.ui.main_ui import IMDWindow
from pyIMD.ui.appeventfilter import AppEventFilter


if __name__ == '__main__':

    app = QApplication(sys.argv)
    if sys.platform.startswith("linux"):
        app.setStyle("fusion")
    main = IMDWindow()
    main.show()
    app_event_filter = AppEventFilter()
    app.installEventFilter(app_event_filter)
    app_event_filter.signal_zoom_in.connect(main.scene.zoom_in)
    app_event_filter.signal_zoom_out.connect(main.scene.zoom_out)
    sys.exit(app.exec_())