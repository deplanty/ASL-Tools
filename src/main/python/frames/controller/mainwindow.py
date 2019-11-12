from PySide2.QtWidgets import (
    QMainWindow
)
from PySide2.QtCore import QCoreApplication

from frames.ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow(self)

        self.ui.btn_quit.clicked.connect(self.btn_quit)

    def btn_quit(self):
        """
        Quit application
        """

        QCoreApplication.quit()
