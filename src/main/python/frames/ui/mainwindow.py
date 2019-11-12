from PySide2.QtCore import (
    QSize,
    Qt
)
from PySide2.QtGui import (
    QIcon
)
from PySide2.QtWidgets import (
    QDesktopWidget,
    QMainWindow,
    QToolButton,
    QVBoxLayout,
    QWidget,
)

class Ui_MainWindow():
    def __init__(self, MainWindow:QMainWindow):

        # Set main window parameters
        MainWindow.setWindowTitle("ASL Tools")
        MainWindow.setWindowIcon(QIcon(":/images/icon.png"))
        MainWindow.setWindowFlag(Qt.Tool)
        MainWindow.setWindowFlag(Qt.WindowStaysOnTopHint)
        MainWindow.setAttribute(Qt.WA_QuitOnClose)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)

        # Main frame
        frame = QWidget()
        frame.setObjectName("mainwindow")
        # Button create vr3 model
        self.btn_model_vr3 = QToolButton()
        self.btn_model_vr3.setIcon(QIcon(":/images/model-vr3.svg"))
        self.btn_model_vr3.setIconSize(QSize(32, 32))
        self.btn_model_vr3.setObjectName("tool")
        self.btn_model_vr3.setCursor(Qt.CursorShape.PointingHandCursor)
        # Create script
        self.btn_script = QToolButton()
        self.btn_script.setIcon(QIcon(":/images/script.svg"))
        self.btn_script.setIconSize(QSize(32, 32))
        self.btn_script.setObjectName("tool")
        self.btn_script.setCursor(Qt.CursorShape.PointingHandCursor)
        # Create dashboard
        self.btn_dashboard = QToolButton()
        self.btn_dashboard.setIcon(QIcon(":/images/dashboard.svg"))
        self.btn_dashboard.setIconSize(QSize(32, 32))
        self.btn_dashboard.setObjectName("tool")
        self.btn_dashboard.setCursor(Qt.CursorShape.PointingHandCursor)
        # Set the buttons in a vertical layout
        self.h_layout = QVBoxLayout(frame)
        self.h_layout.addWidget(self.btn_model_vr3)
        self.h_layout.addWidget(self.btn_script)
        self.h_layout.addWidget(self.btn_dashboard)
        # Window fit the layout
        MainWindow.setCentralWidget(frame)
        MainWindow.setFixedSize(frame.sizeHint())

        # Set the window in the top right corner
        w_w, _ = MainWindow.size().toTuple()
        w_s, _ = QDesktopWidget().size().toTuple()
        x_left = w_s - w_w
        MainWindow.move(x_left, 0)
