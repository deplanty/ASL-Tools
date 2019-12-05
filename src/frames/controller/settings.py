import json

from PySide2 import QtCore, QtGui, QtWidgets

from PySide2.QtCore import (
    QFile
)
from PySide2.QtWidgets import (
    QMainWindow
)

from src.config import Config
from src.frames.ui import Ui_Settings


class Settings(QMainWindow):
    def __init__(self, parent):
        QMainWindow.__init__(self, parent)

        self.ui = Ui_Settings(self)

        # Buttons
        self.ui.group_corner.buttonClicked.connect(self.btn_corner)

        self.check_btn_corner()

    def check_btn_corner(self):
        pos = Config.get("mainwindow/position")
        if pos == "top-right":
            self.ui.btn_corner_tr.setChecked(True)
        elif pos == "top-left":
            self.ui.btn_corner_tl.setChecked(True)
        elif pos == "bottom-right":
            self.ui.btn_corner_br.setChecked(True)
        elif pos == "bottom-left":
            self.ui.btn_corner_bl.setChecked(True)
        else:
            raise ValueError(f"Invalid window position: '{pos}'")

    def btn_corner(self):
        """
        When a button in the corner group button is clicked
        Save the position in the config file
        """

        # Save the new position
        btn = self.ui.group_corner.checkedButton()
        pos = btn.objectName()
        Config.set("mainwindow/position", pos)

        # Move the whindow
        QtCore.qApp.window.set_window_position(pos)
