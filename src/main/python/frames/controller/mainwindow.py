from PySide2.QtWidgets import (
    QMainWindow
)

from frames.controller import Script
from frames.ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow(self)
        self.script = Script(self)

        self.ui.btn_script.clicked.connect(self.btn_script)

    def btn_script(self):
        self.script.show()
