from PySide2.QtWidgets import (
    QMainWindow
)

from src.frames.controller import (
    Script,
    Dashboard
)
from src.frames.ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow(self)
        self.script = Script(self)
        self.dashboard = Dashboard(self)

        self.ui.btn_model_vr3.clicked.connect(self.btn_model_vr3)
        self.ui.btn_script.clicked.connect(self.btn_script)
        self.ui.btn_dashboard.clicked.connect(self.btn_dashboard)

    def btn_model_vr3(self):
        ...

    def btn_script(self):
        self.script.show()

    def btn_dashboard(self):
        self.dashboard.show()
