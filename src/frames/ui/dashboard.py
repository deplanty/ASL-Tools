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
    QMenu,
    QMenuBar,
    QSpacerItem,
    QWidget
)


class Ui_Dashboard:
    def __init__(self, Dashboard:QWidget):

        # Set Window parameters
        Dashboard.setWindowTitle("ASL Tools - Tableau de bord")
        Dashboard.setWindowIcon(QIcon(":/images/icon.png"))
        Dashboard.setWindowFlag(Qt.Window)

        # Main frame
        frame = QWidget(Dashboard)
        self.h_layout = QHBoxLayout(frame)

        # Menubar
        menubar = QMenuBar()
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
        menu_edit:QMenu = menubar.addMenu("Edition")
        self.action_edit_copy = QAction("Copier", menubar)
        self.action_edit_copy.setShortcut("Alt+C")
        menu_edit.addAction(self.action_edit_copy)
        self.action_edit_paste = QAction("Coller", menubar)
        self.action_edit_paste.setShortcut("Alt+V")
        menu_edit.addAction(self.action_edit_paste)
        self.h_layout.setMenuBar(menubar)

        # Spacer
        spacerItem = QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_layout.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.list = QtWidgets.QListWidget(frame)
        self.list.setObjectName("list")
        self.gridLayout.addWidget(self.list, 2, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_e_pmus_hld = QtWidgets.QLabel(frame)
        self.label_e_pmus_hld.setMinimumSize(QtCore.QSize(0, 20))
        self.label_e_pmus_hld.setObjectName("label_e_pmus_hld")
        self.gridLayout_4.addWidget(self.label_e_pmus_hld, 14, 0, 1, 1)
        self.e_pmus_inc = QtWidgets.QSpinBox(frame)
        self.e_pmus_inc.setMaximum(100)
        self.e_pmus_inc.setObjectName("e_pmus_inc")
        self.gridLayout_4.addWidget(self.e_pmus_inc, 13, 1, 1, 1)
        self.resistance = QtWidgets.QSpinBox(frame)
        self.resistance.setMaximum(500)
        self.resistance.setObjectName("resistance")
        self.gridLayout_4.addWidget(self.resistance, 3, 1, 1, 1)
        self.label_e_pmus = QtWidgets.QLabel(frame)
        self.label_e_pmus.setMinimumSize(QtCore.QSize(0, 20))
        self.label_e_pmus.setObjectName("label_e_pmus")
        self.gridLayout_4.addWidget(self.label_e_pmus, 12, 0, 1, 1)
        self.respi_rate = QtWidgets.QSpinBox(frame)
        self.respi_rate.setMaximum(500)
        self.respi_rate.setObjectName("respi_rate")
        self.gridLayout_4.addWidget(self.respi_rate, 4, 1, 1, 1)
        self.e_pmus_rel = QtWidgets.QSpinBox(frame)
        self.e_pmus_rel.setMaximum(100)
        self.e_pmus_rel.setObjectName("e_pmus_rel")
        self.gridLayout_4.addWidget(self.e_pmus_rel, 15, 1, 1, 1)
        self.e_pmus = QtWidgets.QSpinBox(frame)
        self.e_pmus.setMaximum(100)
        self.e_pmus.setObjectName("e_pmus")
        self.gridLayout_4.addWidget(self.e_pmus, 12, 1, 1, 1)
        self.label_e_pmus_inc = QtWidgets.QLabel(frame)
        self.label_e_pmus_inc.setMinimumSize(QtCore.QSize(0, 20))
        self.label_e_pmus_inc.setObjectName("label_e_pmus_inc")
        self.gridLayout_4.addWidget(self.label_e_pmus_inc, 13, 0, 1, 1)
        self.e_pmus_hld = QtWidgets.QSpinBox(frame)
        self.e_pmus_hld.setMaximum(100)
        self.e_pmus_hld.setObjectName("e_pmus_hld")
        self.gridLayout_4.addWidget(self.e_pmus_hld, 14, 1, 1, 1)
        self.enabled = QtWidgets.QCheckBox(frame)
        self.enabled.setText("")
        self.enabled.setObjectName("enabled")
        self.gridLayout_4.addWidget(self.enabled, 0, 1, 1, 1)
        spacerItem1 = QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 16, 0, 1, 1)
        self.label_i_pmus_inc = QtWidgets.QLabel(frame)
        self.label_i_pmus_inc.setMinimumSize(QtCore.QSize(0, 20))
        self.label_i_pmus_inc.setObjectName("label_i_pmus_inc")
        self.gridLayout_4.addWidget(self.label_i_pmus_inc, 8, 0, 1, 1)
        self.label_i_pmus_hld = QtWidgets.QLabel(frame)
        self.label_i_pmus_hld.setMinimumSize(QtCore.QSize(0, 20))
        self.label_i_pmus_hld.setObjectName("label_i_pmus_hld")
        self.gridLayout_4.addWidget(self.label_i_pmus_hld, 9, 0, 1, 1)
        self.label_i_pmus = QtWidgets.QLabel(frame)
        self.label_i_pmus.setMinimumSize(QtCore.QSize(0, 20))
        self.label_i_pmus.setObjectName("label_i_pmus")
        self.gridLayout_4.addWidget(self.label_i_pmus, 7, 0, 1, 1)
        spacerItem2 = QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 6, 0, 1, 1)
        self.i_pmus_inc = QtWidgets.QSpinBox(frame)
        self.i_pmus_inc.setMaximum(100)
        self.i_pmus_inc.setObjectName("i_pmus_inc")
        self.gridLayout_4.addWidget(self.i_pmus_inc, 8, 1, 1, 1)
        spacerItem3 = QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 11, 0, 1, 1)
        self.i_pmus_rel = QtWidgets.QSpinBox(frame)
        self.i_pmus_rel.setMaximum(100)
        self.i_pmus_rel.setObjectName("i_pmus_rel")
        self.gridLayout_4.addWidget(self.i_pmus_rel, 10, 1, 1, 1)
        self.i_pmus = QtWidgets.QSpinBox(frame)
        self.i_pmus.setMaximum(100)
        self.i_pmus.setObjectName("i_pmus")
        self.gridLayout_4.addWidget(self.i_pmus, 7, 1, 1, 1)
        self.i_pmus_hld = QtWidgets.QSpinBox(frame)
        self.i_pmus_hld.setMaximum(100)
        self.i_pmus_hld.setObjectName("i_pmus_hld")
        self.gridLayout_4.addWidget(self.i_pmus_hld, 9, 1, 1, 1)
        self.compliance = QtWidgets.QSpinBox(frame)
        self.compliance.setMaximum(500)
        self.compliance.setObjectName("compliance")
        self.gridLayout_4.addWidget(self.compliance, 2, 1, 1, 1)
        self.label_enabled = QtWidgets.QLabel(frame)
        self.label_enabled.setMinimumSize(QtCore.QSize(0, 20))
        self.label_enabled.setObjectName("label_enabled")
        self.gridLayout_4.addWidget(self.label_enabled, 0, 0, 1, 1)
        self.label_crf = QtWidgets.QLabel(frame)
        self.label_crf.setMinimumSize(QtCore.QSize(0, 20))
        self.label_crf.setObjectName("label_crf")
        self.gridLayout_4.addWidget(self.label_crf, 17, 0, 1, 1)
        self.label_resistance = QtWidgets.QLabel(frame)
        self.label_resistance.setMinimumSize(QtCore.QSize(0, 20))
        self.label_resistance.setObjectName("label_resistance")
        self.gridLayout_4.addWidget(self.label_resistance, 3, 0, 1, 1)
        self.label_respi_rate = QtWidgets.QLabel(frame)
        self.label_respi_rate.setMinimumSize(QtCore.QSize(0, 20))
        self.label_respi_rate.setObjectName("label_respi_rate")
        self.gridLayout_4.addWidget(self.label_respi_rate, 4, 0, 1, 1)
        self.label_e_pmus_rel = QtWidgets.QLabel(frame)
        self.label_e_pmus_rel.setMinimumSize(QtCore.QSize(0, 20))
        self.label_e_pmus_rel.setObjectName("label_e_pmus_rel")
        self.gridLayout_4.addWidget(self.label_e_pmus_rel, 15, 0, 1, 1)
        self.label_i_pmus_rel = QtWidgets.QLabel(frame)
        self.label_i_pmus_rel.setMinimumSize(QtCore.QSize(0, 20))
        self.label_i_pmus_rel.setObjectName("label_i_pmus_rel")
        self.gridLayout_4.addWidget(self.label_i_pmus_rel, 10, 0, 1, 1)
        self.crf = QtWidgets.QDoubleSpinBox(frame)
        self.crf.setDecimals(1)
        self.crf.setSingleStep(0.1)
        self.crf.setObjectName("crf")
        self.gridLayout_4.addWidget(self.crf, 17, 1, 1, 1)
        self.label_compliance = QtWidgets.QLabel(frame)
        self.label_compliance.setMinimumSize(QtCore.QSize(0, 20))
        self.label_compliance.setObjectName("label_compliance")
        self.gridLayout_4.addWidget(self.label_compliance, 2, 0, 1, 1)
        spacerItem4 = QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 2, 1, 1, 1)
        self.label_file = QtWidgets.QLabel(frame)
        self.label_file.setTextFormat(QtCore.Qt.PlainText)
        self.label_file.setAlignment(QtCore.Qt.AlignCenter)
        self.label_file.setObjectName("label_file")
        self.gridLayout.addWidget(self.label_file, 0, 0, 1, 3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(frame)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.comment = QtWidgets.QTextEdit(frame)
        self.comment.setObjectName("comment")
        self.verticalLayout_2.addWidget(self.comment)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 2, 1, 1)
        self.h_layout.addLayout(self.gridLayout)
        spacerItem5 = QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_layout.addItem(spacerItem5)

        # Set size and position
        w, h = self.h_layout.sizeHint().toTuple()
        frame.resize(w, h)
        w_s, h_s = QDesktopWidget().size().toTuple()
        x = round(w_s/2 - w/2)
        y = round(h_s/2 - h/2)
        Dashboard.move(x, y)

        self.retranslateUi(Dashboard)
        QtCore.QMetaObject.connectSlotsByName(Dashboard)
        Dashboard.setTabOrder(self.list, self.enabled)
        Dashboard.setTabOrder(self.enabled, self.compliance)
        Dashboard.setTabOrder(self.compliance, self.resistance)
        Dashboard.setTabOrder(self.resistance, self.respi_rate)
        Dashboard.setTabOrder(self.respi_rate, self.i_pmus)
        Dashboard.setTabOrder(self.i_pmus, self.i_pmus_inc)
        Dashboard.setTabOrder(self.i_pmus_inc, self.i_pmus_hld)
        Dashboard.setTabOrder(self.i_pmus_hld, self.i_pmus_rel)
        Dashboard.setTabOrder(self.i_pmus_rel, self.e_pmus)
        Dashboard.setTabOrder(self.e_pmus, self.e_pmus_inc)
        Dashboard.setTabOrder(self.e_pmus_inc, self.e_pmus_hld)
        Dashboard.setTabOrder(self.e_pmus_hld, self.e_pmus_rel)
        Dashboard.setTabOrder(self.e_pmus_rel, self.crf)

    def retranslateUi(self, Dashboard):
        self.label_e_pmus_hld.setText(QtWidgets.QApplication.translate("Dashboard", "Pmus expi plateau (%)", None, -1))
        self.label_e_pmus.setText(QtWidgets.QApplication.translate("Dashboard", "Pmus expi (cmH2O)", None, -1))
        self.label_e_pmus_inc.setText(QtWidgets.QApplication.translate("Dashboard", "Pmus expi aug (%)", None, -1))
        self.label_i_pmus_inc.setText(QtWidgets.QApplication.translate("Dashboard", "Pmus inspi aug (%)", None, -1))
        self.label_i_pmus_hld.setText(QtWidgets.QApplication.translate("Dashboard", "Pmus inspi plateau (%)", None, -1))
        self.label_i_pmus.setText(QtWidgets.QApplication.translate("Dashboard", "Pmus inspi (cmH2O)", None, -1))
        self.label_enabled.setText(QtWidgets.QApplication.translate("Dashboard", "Activé", None, -1))
        self.label_crf.setText(QtWidgets.QApplication.translate("Dashboard", "CRF (L)", None, -1))
        self.label_resistance.setText(QtWidgets.QApplication.translate("Dashboard", "Résistances", None, -1))
        self.label_respi_rate.setText(QtWidgets.QApplication.translate("Dashboard", "Fréquence respi", None, -1))
        self.label_e_pmus_rel.setText(QtWidgets.QApplication.translate("Dashboard", "Pmus expi dim (%)", None, -1))
        self.label_i_pmus_rel.setText(QtWidgets.QApplication.translate("Dashboard", "Pmus inspi dim (%)", None, -1))
        self.label_compliance.setText(QtWidgets.QApplication.translate("Dashboard", "Compliance", None, -1))
        self.label_file.setToolTip(QtWidgets.QApplication.translate("Dashboard", "Nom du fichier courant", None, -1))
        self.label_file.setText(QtWidgets.QApplication.translate("Dashboard", "<aucun>", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dashboard", "Commentaire", None, -1))
