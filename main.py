# This Python file uses the following encoding: utf-8
import sys
import os

from PySide2.QtCore import QObject
from PySide2.QtCore import Property
from PySide2.QtCore import Signal
from PySide2.QtCore import Slot
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine


class QMLParam(Property):
    """
    Descriptor to manage an individual piece of data that needs to be shared
    between QML and python.
    """
    valueChanged = Signal(int)

    def __init__(self, type_):
        # TODO: need to figure out how to make Coordinate have the correct signals already
        #  by the time this gets called
        # print(self.valueChanged)
        Property().__init__(type_, fget=self.__get__, fset=self.__set__)#, notify=self.valueChanged)

    def __set_name__(self, owner, name):
        self.private_name = '_' + name
        self.signal_name = name + 'Changed'
        setattr(owner, self.signal_name, type(self).valueChanged)

    def __get__(self, instance, owner=None):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        """
        Set the value and emit the valueChanged signal.
        """
        print(f'{self.private_name[1:]} being changed to {value}')
        if not isinstance(value, int):
            raise TypeError(f'Expected type int, got {type(value)}')
        setattr(instance, self.private_name, value)
        signal = getattr(instance, self.signal_name)
        print('descriptor signal', type(self).valueChanged, type(type(self).valueChanged))
        print('coord signal', signal, type(signal))
        signal.emit(value)


class Coordinate(QObject):
    x = QMLParam(int)
    y = QMLParam(int)

    def __init__(self, x: int = 0, y: int = 0):
        super().__init__()
        self.x = x
        self.y = y

    def setXToFour(self):
        self.x = 4


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    coord = Coordinate(5, 5)
    engine.rootContext().setContextProperty('_coord1', coord)

    engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
