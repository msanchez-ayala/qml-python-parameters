# This Python file uses the following encoding: utf-8
import sys
import os

from PySide2.QtCore import QObject
from PySide2.QtCore import Property
from PySide2.QtCore import Signal
from PySide2.QtCore import Slot
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine


CHANGED_SIGNAL = 'Changed'


class Param(QObject):
    """
    Descriptor to manage an individual piece of data that needs to be shared
    between QML and python.
    """
    DataClass = None

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner=None):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        """
        Set the value and emit the valueChanged signal.
        """
        self.validate(value)
        setattr(instance, self.private_name, value)
        # signal = getattr(instance, self.param_name + CHANGED_SIGNAL)
        # signal.emit(value)

    def validate(self):
        NotImplemented


class IntParam(Param):

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Expected type int, got {type(value)}')


class CompoundParamMeta(type(QObject)):

    @classmethod
    def __prepare__(metacls, name, bases):
        dct = super().__prepare__(name, bases)
        dct['_sub_params'] = {}
        return dct

    def __new__(metacls, name, parents, dct, **kwargs):
        new_cls = super().__new__(metacls, name, parents, dct, **kwargs)
        return new_cls


class CompoundParam(QObject, metaclass=CompoundParamMeta):
    """
    Container for multiple Param instances.
    """

    def __init_subclass__(cls):
        super().__init_subclass__()
        cls._populateClassParams()
        cls._populateSignalsOnClass()

    @classmethod
    def _populateClassParams(cls):
        for name, attr in list(cls.__dict__.items()):
            if isinstance(attr, Param):
                param = attr
                cls._sub_params[name] = param

    @classmethod
    def _populateSignalsOnClass(cls):
        for name in cls._sub_params:
            signal_name = name + CHANGED_SIGNAL
            signal = Signal(object)
            setattr(cls, signal_name, signal)


class Coordinate(CompoundParam):
    x = IntParam()
    y = IntParam()

    def __init__(self, x: int = 0, y: int = 0):
        super().__init__()
        self.x = x
        self.y = y

    def setXToFour(self):
        self.x = 4


c = Coordinate()
# TODO: how do we make the property?

#
# if __name__ == "__main__":
#     app = QGuiApplication(sys.argv)
#     engine = QQmlApplicationEngine()
#
#     coord = Coordinate(5, 5)
#     engine.rootContext().setContextProperty('_coord1', coord)
#
#     engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))
#
#     if not engine.rootObjects():
#         sys.exit(-1)
#     sys.exit(app.exec_())
