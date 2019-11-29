from PySide2.QtWidgets import (
    QMainWindow
)

from src.frames.controller import (
    LungModel,
    Script,
    Dashboard,
    BigScript
)
from src.frames.ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow(self)

        self.lungmodel = LungModel(self)
        self.script = Script(self)
        self.dashboard = Dashboard(self)
        self.bigscript = BigScript(self)

        self.ui.btn_model_vr3.clicked.connect(self.lungmodel.show)
        self.ui.btn_script.clicked.connect(self.script.show)
        self.ui.btn_dashboard.clicked.connect(self.dashboard.show)
        self.ui.btn_bigscript.clicked.connect(self.bigscript.show)
