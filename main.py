# This Python file uses the following encoding: utf-8
import sys
import os

from PySide2.QtCore import QObject
from PySide2.QtCore import Property
from PySide2.QtCore import Signal
from PySide2.QtCore import Slot
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine


class Coordinate(QObject):
    xChanged = Signal(float)
    yChanged = Signal(float)
    valueChanged = Signal()

    def __init__(self, x=0, y=0, parent=None):
        super().__init__(parent)
        self._x = x
        self._y = y

    def getX(self) -> float:
        return self._x

    def setX(self, x: float):
        self._x = x
        self.xChanged.emit(x)
        self.valueChanged.emit()

    def getY(self) -> float:
        return self._y

    def setY(self, y: float):
        self._y = y
        self.yChanged.emit(y)
        self.valueChanged.emit()

    x = Property(float, getX, setX, notify=xChanged)
    y = Property(float, getY, setY, notify=yChanged)


class Midpoint(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.coord1 = Coordinate()
        self.coord2 = Coordinate()
        self.midpoint = Coordinate()
        self.coord1.valueChanged.connect(self.updateMidpoint)
        self.coord2.valueChanged.connect(self.updateMidpoint)
        self.updateMidpoint()

    def updateMidpoint(self):
        self.midpoint.x = abs(self.coord2.x + self.coord1.x) / 2
        self.midpoint.y = abs(self.coord2.y + self.coord1.y) / 2


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    model = Midpoint()
    coord1 = model.coord1
    coord2 = model.coord2
    midpoint = model.midpoint

    engine.rootContext().setContextProperty('_coord1', coord1)
    engine.rootContext().setContextProperty('_coord2', coord2)
    engine.rootContext().setContextProperty('_midpoint', midpoint)

    engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
