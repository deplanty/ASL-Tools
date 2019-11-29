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

        icon_size = QSize(48, 48)

        # Main frame
        frame = QWidget()
        frame.setObjectName("mainwindow")
        self.v_layout = QVBoxLayout(frame)
        # Button create vr3 model
        self.btn_model_vr3 = QToolButton()
        self.btn_model_vr3.setIcon(QIcon(":/images/model-vr3.svg"))
        self.btn_model_vr3.setIconSize(icon_size)
        self.btn_model_vr3.setCursor(Qt.CursorShape.PointingHandCursor)
        self.v_layout.addWidget(self.btn_model_vr3)
        # Create script
        self.btn_script = QToolButton()
        self.btn_script.setIcon(QIcon(":/images/script.svg"))
        self.btn_script.setIconSize(icon_size)
        self.btn_script.setCursor(Qt.CursorShape.PointingHandCursor)
        self.v_layout.addWidget(self.btn_script)
        # Create dashboard
        self.btn_dashboard = QToolButton()
        self.btn_dashboard.setIcon(QIcon(":/images/dashboard.svg"))
        self.btn_dashboard.setIconSize(icon_size)
        self.btn_dashboard.setCursor(Qt.CursorShape.PointingHandCursor)
        self.v_layout.addWidget(self.btn_dashboard)
        # Create big script
        self.btn_bigscript = QToolButton()
        self.btn_bigscript.setIcon(QIcon(":/images/dashboard.svg"))
        self.btn_bigscript.setIconSize(icon_size)
        self.btn_dashboard.setCursor(Qt.CursorShape.PointingHandCursor)
        self.v_layout.addWidget(self.btn_bigscript)
        # # Window fit the layout
        MainWindow.setCentralWidget(frame)
        MainWindow.setFixedSize(frame.sizeHint())

        # Set the window in the top right corner
        w_w, _ = MainWindow.size().toTuple()
        w_s, _ = QDesktopWidget().size().toTuple()
        x_left = w_s - w_w
        MainWindow.move(x_left, 0)
