from PySide2.QtWidgets import (
    QMainWindow
)

from src.frames.ui import Ui_Settings


class Settings(QMainWindow):
    def __init__(self, parent):
        QMainWindow.__init__(self, parent)

        self.ui = Ui_Settings(self)
