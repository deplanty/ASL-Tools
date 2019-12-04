import json

from PySide2.QtCore import (
    QFile
)
from PySide2.QtWidgets import (
    QMainWindow
)

from src.frames.ui import Ui_Settings


class Settings(QMainWindow):
    def __init__(self, parent):
        QMainWindow.__init__(self, parent)

        self.ui = Ui_Settings(self)

        self.check_btn_corner()

    def check_btn_corner(self):
        file = QFile(":/config/config.json")
        file.open(QFile.ReadOnly)
        config = file.readAll().data().decode()
        config = json.loads(config)
        file.close()

        pos = config["mainwindow"]["position"]
        if pos == "top-right":
            self.ui.btn_corner_tr.setChecked(True)
            self.ui.btn_corner_tl.setChecked(False)
        elif pos == "top-left":
            self.ui.btn_corner_tr.setChecked(False)
            self.ui.btn_corner_tl.setChecked(True)
