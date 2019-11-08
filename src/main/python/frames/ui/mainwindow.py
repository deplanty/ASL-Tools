from PySide2.QtCore import (
    QSize,
)
from PySide2.QtGui import (
    QIcon,
)
from PySide2.QtWidgets import (
    QMainWindow,
    QToolButton,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow():
    def __init__(self, MainWindow:QMainWindow):

        MainWindow = MainWindow
        MainWindow.setWindowTitle("ASL Tools")
        MainWindow.setWindowIcon(QIcon(":/images/icon.png"))
        MainWindow.resize(400, 300)

        frame = QWidget()

        self.btn_1 = QToolButton()
        self.btn_1.setIcon(QIcon(":/images/model-vr3.svg"))
        self.btn_1.setIconSize(QSize(32, 32))
        self.btn_2 = QToolButton()
        self.btn_2.setIcon(QIcon(":/images/script.svg"))
        self.btn_2.setIconSize(QSize(32, 32))
        self.btn_3 = QToolButton()
        self.btn_3.setIcon(QIcon(":/images/dashboard.svg"))
        self.btn_3.setIconSize(QSize(32, 32))

        self.h_layout = QVBoxLayout()
        self.h_layout.addWidget(self.btn_1)
        self.h_layout.addWidget(self.btn_2)
        self.h_layout.addWidget(self.btn_3)

        frame.setLayout(self.h_layout)
        MainWindow.setCentralWidget(frame)
