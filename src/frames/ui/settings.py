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
    QButtonGroup,
    QGridLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class Ui_Settings():
    def __init__(self, Settings:QMainWindow):

        # Set window parameters
        Settings.setWindowTitle("ASL Tools - Settings")
        Settings.setWindowFlag(Qt.Window)

        icon_size = QSize(48, 48)

        # Main frame
        frame = QWidget()
        frame.setObjectName("mainwindow")
        self.v_layout = QVBoxLayout(frame)

        # Select tool window location
        self.label_location = QLabel()
        self.v_layout.addWidget(self.label_location)
        self.group_corner = QButtonGroup()
        self.grid_layout = QGridLayout()
        # Top left corner
        self.btn_corner_tl = QPushButton()
        self.btn_corner_tl.setIcon(QIcon(":/images/corner-tl.svg"))
        self.btn_corner_tl.setIconSize(QSize(32, 32))
        self.btn_corner_tl.setCheckable(True)
        self.group_corner.addButton(self.btn_corner_tl)
        self.grid_layout.addWidget(self.btn_corner_tl, 0, 0)
        # Top right corner
        self.btn_corner_tr = QPushButton()
        self.btn_corner_tr.setIcon(QIcon(":/images/corner-tr.svg"))
        self.btn_corner_tr.setIconSize(QSize(32, 32))
        self.btn_corner_tr.setCheckable(True)
        self.group_corner.addButton(self.btn_corner_tr)
        self.grid_layout.addWidget(self.btn_corner_tr, 0, 1)
        # bottom left corner
        self.btn_corner_bl = QPushButton()
        self.btn_corner_bl.setIcon(QIcon(":/images/corner-bl.svg"))
        self.btn_corner_bl.setIconSize(QSize(32, 32))
        self.btn_corner_bl.setCheckable(True)
        self.group_corner.addButton(self.btn_corner_bl)
        self.grid_layout.addWidget(self.btn_corner_bl, 1, 0)
        # Bottom right corner
        self.btn_corner_br = QPushButton()
        self.btn_corner_br.setIcon(QIcon(":/images/corner-br.svg"))
        self.btn_corner_br.setIconSize(QSize(32, 32))
        self.btn_corner_br.setCheckable(True)
        self.group_corner.addButton(self.btn_corner_br)
        self.grid_layout.addWidget(self.btn_corner_br, 1, 1)

        self.v_layout.addLayout(self.grid_layout)

        # Window fit the layout
        self.retranslateUi(Settings)
        Settings.setCentralWidget(frame)
        Settings.setFixedSize(frame.sizeHint())

        # Set size and position
        w, h = self.v_layout.sizeHint().toTuple()
        w_s, h_s = QApplication.primaryScreen().size().toTuple()
        x = round(w_s/2 - w/2)
        y = round(h_s/2 - h/2)
        Settings.setCentralWidget(frame)
        Settings.resize(w, h)
        Settings.move(x, y)

        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        self.label_location.setText(QtWidgets.QApplication.translate("Settings", "Sélectionnez la position de la fenêtre :", None, -1))
