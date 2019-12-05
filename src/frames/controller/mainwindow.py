import webbrowser

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (
    Qt
)
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow
)

from src.config import Config, Paths
from src.frames.controller import (
    Settings,
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

        self.settings = Settings(self)
        self.lungmodel = LungModel(self)
        self.script = Script(self)
        self.dashboard = Dashboard(self)
        self.bigscript = BigScript(self)

        self.ui.btn_quit.clicked.connect(QtCore.qApp.quit)
        self.ui.btn_help.clicked.connect(self.btn_help)
        self.ui.btn_settings.clicked.connect(self.settings.show)
        self.ui.btn_model_vr3.clicked.connect(self.lungmodel.show)
        self.ui.btn_script.clicked.connect(self.script.show)
        self.ui.btn_dashboard.clicked.connect(self.dashboard.show)
        self.ui.btn_bigscript.clicked.connect(self.bigscript.show)

        self.old_pos = None
        self.ui.frame_top.mousePressEvent = self.evt_mousePressEvent
        self.ui.frame_top.mouseMoveEvent = self.evt_mouseMoveEvent
        self.ui.frame_top.mouseReleaseEvent = self.evt_mouseReleaseEvent
        self.ui.frame_top.mouseDoubleClickEvent = self.evt_mouseDoubleClickEvent

        self.evt_mouseDoubleClickEvent(None)

    # =========================================================================
    # = Buttons
    # =========================================================================

    def btn_help(self):
        """
        Show the help on the default browser
        """

        index_help = Paths.file("help")
        webbrowser.open_new_tab(index_help)

    # =========================================================================
    # = Events
    # =========================================================================

    def evt_mousePressEvent(self, event):
        """
        Get current mouse position
        """

        self.ui.frame_top.setCursor(Qt.ClosedHandCursor)
        self.old_pos = event.globalPos()

    def evt_mouseMoveEvent(self, event):
        """
        Move the window according to mouse motion
        """

        delta = QtCore.QPoint(event.globalPos() - self.old_pos)
        self.move(self.x()+delta.x(), self.y()+delta.y())
        self.old_pos = event.globalPos()

    def evt_mouseReleaseEvent(self, event):
        """
        Set cursor back to open hand
        """

        self.ui.frame_top.setCursor(Qt.OpenHandCursor)

    def evt_mouseDoubleClickEvent(self, event):
        """
        Set the window in the top right corner
        """

        position = Config.get("mainwindow/position")
        self.set_window_position(position)

    # =========================================================================
    # = Misc
    # =========================================================================

    def set_window_position(self, position):
        """
        Set the window at the given position

        Args:
            position (str): [top-right, top-left, bottom-right, bottom-left]
        """

        # Set the window in the top right corner
        w_w, h_w = self.size().toTuple()
        w_s, h_s = QApplication.primaryScreen().size().toTuple()

        if position == "top-right":
            x = w_s - w_w
            y = 0
        elif position == "top-left":
            x = 0
            y = 0
        elif position == "bottom-right":
            x = w_s - w_w
            y = h_s - h_w
        elif position == "bottom-left":
            x = 0
            y = h_s - h_w
        else:
            raise ValueError(f"Invalid window position: '{position}'")

        self.move(x, y)
