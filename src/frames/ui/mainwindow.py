from PySide2 import QtCore, QtGui, QtWidgets

from PySide2.QtCore import (
    QSize,
    Qt
)
from PySide2.QtGui import (
    QIcon
)
from PySide2.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QMainWindow,
    QToolButton,
    QVBoxLayout,
    QWidget,
)

class Ui_MainWindow():
    def __init__(self, MainWindow:QMainWindow):

        # Set main window parameters
        MainWindow.setWindowTitle("ASL Tools")
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.setWindowFlag(Qt.FramelessWindowHint)
        MainWindow.setWindowFlag(Qt.WindowStaysOnTopHint)
        MainWindow.setAttribute(Qt.WA_QuitOnClose)

        icon_size = QSize(48, 48)

        # Main frame
        frame = QWidget()
        frame.setObjectName("mainwindow")
        self.v_layout = QVBoxLayout(frame)
        self.v_layout.setMargin(0)
        self.v_layout.setSpacing(0)

        # Top frame
        self.frame_top = QFrame()
        self.frame_top.setObjectName("topframe")
        self.frame_top.setMaximumHeight(20)
        self.v_layout.addWidget(self.frame_top)
        self.h_layout = QHBoxLayout(self.frame_top)
        self.h_layout.setMargin(0)
        self.btn_quit = QToolButton()
        self.btn_quit.setIcon(QIcon(":/images/quit.svg"))
        self.btn_quit.setIconSize(QSize(16, 16))
        self.btn_quit.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_quit.setAutoRaise(True)
        self.h_layout.addWidget(self.btn_quit, alignment=Qt.AlignRight)

        # Misc
        self.h_layout_misc = QHBoxLayout()
        self.h_layout_misc.setSpacing(0)
        self.h_layout_misc.setMargin(0)
        self.v_layout.addLayout(self.h_layout_misc)
        # Help
        self.btn_help = QToolButton()
        self.btn_help.setIcon(QIcon(":/images/help.svg"))
        self.btn_help.setObjectName("toolsmall")
        self.btn_help.setIconSize(QSize(20, 20))
        self.btn_help.setCursor(Qt.CursorShape.PointingHandCursor)
        self.h_layout_misc.addWidget(self.btn_help)
        # Settings
        self.btn_settings = QToolButton()
        self.btn_settings.setIcon(QIcon(":/images/settings.svg"))
        self.btn_settings.setObjectName("toolsmall")
        self.btn_settings.setIconSize(QSize(20, 20))
        self.btn_settings.setCursor(Qt.CursorShape.PointingHandCursor)
        self.h_layout_misc.addWidget(self.btn_settings)
        # Button create vr3 model
        self.btn_model_vr3 = QToolButton()
        self.btn_model_vr3.setIcon(QIcon(":/images/model-vr3.svg"))
        self.btn_model_vr3.setObjectName("tool")
        self.btn_model_vr3.setIconSize(icon_size)
        self.btn_model_vr3.setCursor(Qt.CursorShape.PointingHandCursor)
        self.v_layout.addWidget(self.btn_model_vr3)
        # Create script
        self.btn_script = QToolButton()
        self.btn_script.setIcon(QIcon(":/images/script.svg"))
        self.btn_script.setObjectName("tool")
        self.btn_script.setIconSize(icon_size)
        self.btn_script.setCursor(Qt.CursorShape.PointingHandCursor)
        self.v_layout.addWidget(self.btn_script)
        # Create dashboard
        self.btn_dashboard = QToolButton()
        self.btn_dashboard.setIcon(QIcon(":/images/dashboard.svg"))
        self.btn_dashboard.setObjectName("tool")
        self.btn_dashboard.setIconSize(icon_size)
        self.btn_dashboard.setCursor(Qt.CursorShape.PointingHandCursor)
        self.v_layout.addWidget(self.btn_dashboard)
        # Create big script
        self.btn_bigscript = QToolButton()
        self.btn_bigscript.setIcon(QIcon(":/images/big-script.svg"))
        self.btn_bigscript.setObjectName("tool")
        self.btn_bigscript.setIconSize(icon_size)
        self.btn_bigscript.setCursor(Qt.CursorShape.PointingHandCursor)
        self.v_layout.addWidget(self.btn_bigscript)
        # # Window fit the layout
        MainWindow.setCentralWidget(frame)
        MainWindow.setFixedSize(frame.sizeHint())
