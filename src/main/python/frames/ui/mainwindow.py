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
        icon = QIcon(":/images/icon.png")
        MainWindow.setWindowIcon(icon)
        MainWindow.resize(400, 300)

        frame = QWidget()

        self.btn_1 = QToolButton()
        icon = QIcon(":/images/icon.png")
        self.btn_1.setIcon(icon)
        self.btn_1.setIconSize(QSize(32, 32))
        self.btn_2 = QToolButton()
        self.btn_3 = QToolButton()

        self.h_layout = QVBoxLayout()
        self.h_layout.addWidget(self.btn_1)
        self.h_layout.addWidget(self.btn_2)
        self.h_layout.addWidget(self.btn_3)

        frame.setLayout(self.h_layout)
        MainWindow.setCentralWidget(frame)
