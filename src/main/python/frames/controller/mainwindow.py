from PySide2.QtWidgets import (
    QMainWindow
)

from frames.ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow(self)

        self.ui.btn_1.clicked.connect(self.btn_1)

    def btn_1(self):
        print("BOUTON 1")
