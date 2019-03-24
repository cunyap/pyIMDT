from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal


class AppEventFilter(QtCore.QObject):
    """
    Implementation of the app event filter
    """

    signal_zoom_in = pyqtSignal(int, name='zoom_in')
    signal_zoom_out = pyqtSignal(int, name='zoom_out')

    def eventFilter(self, receiver, event):
        """
        Overwrites the default eventFilter method handling the zoom in and out signals for the plus, minus key
        and the mouse wheel.

        Args:
            receiver:               Receiver
            event:                  Event

        Returns:
            state (`boolean`):      Returns true for a handled event
            signal (`int`);         Emits the distance for the respective signal
        """

        if event.type() == QtCore.QEvent.KeyPress:

            if event.key() == Qt.Key_Minus:

                self.signal_zoom_out.emit(2)
                return True

            if event.key() == Qt.Key_Plus:

                self.signal_zoom_in.emit(2)
                return True

            else:
                return super(AppEventFilter, self).eventFilter(receiver, event)

        elif event.type() == QtCore.QEvent.Wheel:

                if event.angleDelta().y() > 0:
                    self.signal_zoom_out.emit(2)
                else:
                    self.signal_zoom_in.emit(2)
                return True

        else:

            return super(AppEventFilter, self).eventFilter(receiver, event)
