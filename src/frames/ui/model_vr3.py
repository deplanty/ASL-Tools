from PySide2 import QtCore, QtGui, QtWidgets

from PySide2.QtCore import (
    Qt
)
from PySide2.QtGui import (
    QIcon
)
from PySide2.QtWidgets import (
    QAction,
    QDesktopWidget,
    QHBoxLayout,
    QMainWindow,
    QMenu,
    QMenuBar,
    QSizePolicy,
    QSpacerItem,
    QWidget
)


class Ui_ModelVr3:
    def __init__(self, ModelVr3:QMainWindow):

        # Set Window parameters
        ModelVr3.setWindowTitle("ASL Tools - Tableau de bord")
        ModelVr3.setWindowIcon(QIcon(":/images/icon.png"))
        ModelVr3.setWindowFlag(Qt.Window)

        # Main frame
        frame = QtWidgets.QWidget(ModelVr3)
        self.h_layout = QHBoxLayout(frame)

        # Menubar
        menubar = ModelVr3.menuBar()
        menu_file:QMenu = menubar.addMenu("Fichier")
        self.action_file_new = QAction("Nouveau", menubar)
        self.action_file_new.setIcon(QIcon(":/images/new-file.svg"))
        self.action_file_new.setShortcut("Ctrl+N")
        menu_file.addAction(self.action_file_new)
        self.action_file_open = QAction("Ouvrir", menubar)
        self.action_file_open.setIcon(QIcon(":/images/open-file.svg"))
        self.action_file_open.setShortcut("Ctrl+O")
        menu_file.addAction(self.action_file_open)
        self.action_file_save = QAction("Enregistrer", menubar)
        self.action_file_save.setIcon(QIcon(":/images/save.svg"))
        self.action_file_save.setShortcut("Ctrl+S")
        menu_file.addAction(self.action_file_save)
        self.action_file_saveas = QAction("Enregistrer sous", menubar)
        self.action_file_saveas.setIcon(QIcon(":/images/save-as.svg"))
        self.action_file_saveas.setShortcut("Ctrl+Shift+S")
        menu_file.addAction(self.action_file_saveas)
        menu_file.addSeparator()
        self.action_file_export = QAction("Exporter", menubar)
        self.action_file_export.setIcon(QIcon(":/images/export.svg"))
        menu_file.addAction(self.action_file_export)
        menu_file.addSeparator()
        self.action_file_quit = QAction("Quitter", menubar)
        self.action_file_quit.setIcon(QIcon(":/images/quit.svg"))
        menu_file.addAction(self.action_file_quit)
        # self.h_layout.setMenuBar(menubar)

        # Spacer
        spacerItem = QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_layout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_file = QtWidgets.QLabel(frame)
        self.label_file.setAlignment(QtCore.Qt.AlignCenter)
        self.label_file.setObjectName("label_file")
        self.verticalLayout.addWidget(self.label_file)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.check_time_constant = QtWidgets.QCheckBox(frame)
        self.check_time_constant.setCheckable(True)
        self.check_time_constant.setChecked(True)
        self.check_time_constant.setObjectName("check_time_constant")
        self.horizontalLayout_2.addWidget(self.check_time_constant)
        self.label_repetitions = QtWidgets.QLabel(frame)
        self.label_repetitions.setObjectName("label_repetitions")
        self.horizontalLayout_2.addWidget(self.label_repetitions)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_add = QtWidgets.QToolButton(frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add.setIcon(icon)
        self.btn_add.setIconSize(QtCore.QSize(24, 24))
        self.btn_add.setAutoRaise(True)
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout.addWidget(self.btn_add)
        self.btn_remove = QtWidgets.QToolButton(frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_remove.setIcon(icon1)
        self.btn_remove.setIconSize(QtCore.QSize(24, 24))
        self.btn_remove.setAutoRaise(True)
        self.btn_remove.setObjectName("btn_remove")
        self.horizontalLayout.addWidget(self.btn_remove)
        self.btn_move_up = QtWidgets.QToolButton(frame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/arrow-up.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_move_up.setIcon(icon2)
        self.btn_move_up.setIconSize(QtCore.QSize(24, 24))
        self.btn_move_up.setAutoRaise(True)
        self.btn_move_up.setObjectName("btn_move_up")
        self.horizontalLayout.addWidget(self.btn_move_up)
        self.btn_move_down = QtWidgets.QToolButton(frame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/arrow-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_move_down.setIcon(icon3)
        self.btn_move_down.setIconSize(QtCore.QSize(24, 24))
        self.btn_move_down.setAutoRaise(True)
        self.btn_move_down.setObjectName("btn_move_down")
        self.horizontalLayout.addWidget(self.btn_move_down)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tree = QtWidgets.QTreeWidget(frame)
        self.tree.setMinimumSize(QtCore.QSize(420, 500))
        self.tree.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.verticalLayout.addWidget(self.tree)
        spacerItem = QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.h_layout.addLayout(self.verticalLayout)
        spacer = QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_layout.addItem(spacer)

        # Set size and position
        w, h = self.h_layout.sizeHint().toTuple()
        w_s, h_s = QDesktopWidget().size().toTuple()
        x = round(w_s/2 - w/2)
        y = round(h_s/2 - h/2)
        ModelVr3.setCentralWidget(frame)
        ModelVr3.resize(w, h)
        ModelVr3.move(x, y)

        self.retranslateUi(ModelVr3)
        QtCore.QMetaObject.connectSlotsByName(ModelVr3)

    def retranslateUi(self, ModelVr3):
        self.label_file.setText(QtWidgets.QApplication.translate("ModelVr3", "<aucun>", None, -1))
        self.check_time_constant.setText(QtWidgets.QApplication.translate("ModelVr3", "Paramètres constants", None, -1))
        self.label_repetitions.setText(QtWidgets.QApplication.translate("ModelVr3", "", None, -1))
        self.btn_add.setText(QtWidgets.QApplication.translate("ModelVr3", "...", None, -1))
        self.btn_remove.setText(QtWidgets.QApplication.translate("ModelVr3", "...", None, -1))
        self.btn_move_up.setText(QtWidgets.QApplication.translate("ModelVr3", "...", None, -1))
        self.btn_move_down.setText(QtWidgets.QApplication.translate("ModelVr3", "...", None, -1))
