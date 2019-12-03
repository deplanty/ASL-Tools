from PySide2 import QtCore
from PySide2.QtWidgets import (
    QApplication,
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

        self.ui.btn_quit.clicked.connect(QtCore.qApp.quit)
        self.ui.btn_model_vr3.clicked.connect(self.lungmodel.show)
        self.ui.btn_script.clicked.connect(self.script.show)
        self.ui.btn_dashboard.clicked.connect(self.dashboard.show)
        self.ui.btn_bigscript.clicked.connect(self.bigscript.show)

        def mousePressEvent(event):
            self.old_pos = event.globalPos()

        def mouseMoveEvent(event):
            delta = QtCore.QPoint(event.globalPos() - self.old_pos)
            self.move(self.x()+delta.x(), self.y()+delta.y())
            self.old_pos = event.globalPos()

        self.old_pos = None
        self.ui.frame_top.mousePressEvent = mousePressEvent
        self.ui.frame_top.mouseMoveEvent = mouseMoveEvent
