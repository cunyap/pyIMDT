from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot, Qt, pyqtSignal, QPointF
from PyQt5.QtWidgets import QGraphicsScene

__author__ = 'Andreas P. Cuny'


class GraphicScene(QGraphicsScene):
    """
    The GraphicsScene displays the results interactively
    """

    signalMoveOffset = pyqtSignal(QPointF, name="move_offset")

    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)

        self.image = None
        self.__prevMousePos =[]

    @pyqtSlot(int, name="zoom_in")
    def zoom_in(self, zoom_in_factor):
        """
        Zoom the scene in
        """
        print('zoom in called')
        f = float(zoom_in_factor)
        self.views()[0].scale(f, f)

    @pyqtSlot(int, name="zoom_out")
    def zoom_out(self, zoom_out_factor):
        """
        Zoom the scene out
        """

        f = 1.0 / float(zoom_out_factor)
        self.views()[0].scale(f, f)

    def display_image(self, image_path):
        """
        Stores and displays an image
        :param image_path: a path to the image
        :return: void
        """

        # Show the image (and store it)
        self.image = QPixmap(str(image_path))
        self.addPixmap(self.image)

        # Reset the scene size
        self.setSceneRect(0, 0, self.image.width(), self.image.height())

    def redraw(self):
        """
        Redraws the scene.
        :return: void
        """
        self.views()[0].viewport().update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__prevMousePos = event.scenePos()
        else:
            super(GraphicScene, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            offset = self.__prevMousePos - event.scenePos()
            self.signalMoveOffset.emit(offset)
        else:
            super(GraphicScene, self).mouseMoveEvent(event)
