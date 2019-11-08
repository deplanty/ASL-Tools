from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import (
    QMainWindow
)

from frames.ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, ctx:ApplicationContext):
        QMainWindow.__init__(self)

        self.ctx = ctx
        self.ui = Ui_MainWindow(self)
