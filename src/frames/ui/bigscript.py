from PySide2 import QtCore, QtGui, QtWidgets

from PySide2.QtCore import (
    Qt
)
from PySide2.QtGui import (
    QIcon
)
from PySide2.QtWidgets import (
    QAction,
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMenu,
    QMenuBar,
    QProgressBar,
    QSpacerItem,
    QWidget
)


class Ui_BigScript:
    def __init__(self, BigScript:QMainWindow):

        # Set Window parameters
        BigScript.setWindowTitle("ASL Tools - Big Script")
        BigScript.setWindowFlag(Qt.Window)

        # Main frame
        frame = QWidget(BigScript)
        self.h_layout = QHBoxLayout(frame)

        # Menubar
        menubar = BigScript.menuBar()
        menu_file:QMenu = menubar.addMenu("Fichier")
        self.action_file_new = QAction("Nouveau", menubar)
        self.action_file_new.setIcon(QIcon(":/images/new-file.svg"))
        self.action_file_new.setShortcut("Ctrl+N")
        menu_file.addAction(self.action_file_new)
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

        # Spacer
        spacerItem = QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_layout.addItem(spacerItem)

        # Grid layout
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(15)
        # File
        self.label_file = QtWidgets.QLabel(frame)
        self.label_file.setTextFormat(QtCore.Qt.PlainText)
        self.label_file.setAlignment(QtCore.Qt.AlignCenter)
        self.label_file.setObjectName("label_file")
        self.gridLayout.addWidget(self.label_file, 0, 0, 1, 4)
        # Header
        self.label_from = QLabel(frame)
        self.gridLayout.addWidget(self.label_from, 1, 1, 1, 1)
        self.label_to = QLabel(frame)
        self.gridLayout.addWidget(self.label_to, 1, 2, 1, 1)
        self.label_step = QLabel(frame)
        self.gridLayout.addWidget(self.label_step, 1, 3, 1, 1)
        # Resistance
        self.label_r = QLabel(frame)
        self.gridLayout.addWidget(self.label_r, 2, 0, 1, 1)
        self.r_from = QtWidgets.QSpinBox(frame)
        self.r_from.setObjectName("grid-spin")
        self.r_from.setMinimum(0)
        self.r_from.setMaximum(200)
        self.gridLayout.addWidget(self.r_from, 2, 1, 1, 1)
        self.r_to = QtWidgets.QSpinBox(frame)
        self.r_to.setObjectName("grid-spin")
        self.r_to.setMinimum(0)
        self.r_to.setMaximum(200)
        self.gridLayout.addWidget(self.r_to, 2, 2, 1, 1)
        self.r_step = QtWidgets.QSpinBox(frame)
        self.r_step.setObjectName("grid-spin")
        self.r_step.setMinimum(1)
        self.gridLayout.addWidget(self.r_step, 2, 3, 1, 1)
        # Compliance
        self.label_c = QLabel(frame)
        self.gridLayout.addWidget(self.label_c, 3, 0, 1, 1)
        self.c_from = QtWidgets.QSpinBox(frame)
        self.c_from.setObjectName("grid-spin")
        self.c_from.setMinimum(0)
        self.c_from.setMaximum(200)
        self.gridLayout.addWidget(self.c_from, 3, 1, 1, 1)
        self.c_to = QtWidgets.QSpinBox(frame)
        self.c_to.setObjectName("grid-spin")
        self.c_to.setMinimum(0)
        self.c_to.setMaximum(200)
        self.gridLayout.addWidget(self.c_to, 3, 2, 1, 1)
        self.c_step = QtWidgets.QSpinBox(frame)
        self.c_step.setObjectName("grid-spin")
        self.c_step.setMinimum(1)
        self.gridLayout.addWidget(self.c_step, 3, 3, 1, 1)
        # Breath rate
        self.label_br = QLabel(frame)
        self.gridLayout.addWidget(self.label_br, 4, 0, 1, 1)
        self.br_from = QtWidgets.QSpinBox(frame)
        self.br_from.setObjectName("grid-spin")
        self.br_from.setMinimum(1)
        self.br_from.setMaximum(100)
        self.gridLayout.addWidget(self.br_from, 4, 1, 1, 1)
        self.br_to = QtWidgets.QSpinBox(frame)
        self.br_to.setObjectName("grid-spin")
        self.br_to.setMinimum(1)
        self.br_to.setMaximum(100)
        self.gridLayout.addWidget(self.br_to, 4, 2, 1, 1)
        self.br_step = QtWidgets.QSpinBox(frame)
        self.br_step.setObjectName("grid-spin")
        self.br_step.setMinimum(1)
        self.gridLayout.addWidget(self.br_step, 4, 3, 1, 1)
        # Pmus
        self.label_i_pmus = QLabel(frame)
        self.gridLayout.addWidget(self.label_i_pmus, 5, 0, 1, 1)
        self.i_pmus_from = QtWidgets.QSpinBox(frame)
        self.i_pmus_from.setObjectName("grid-spin")
        self.i_pmus_from.setMinimum(0)
        self.i_pmus_from.setMaximum(100)
        self.gridLayout.addWidget(self.i_pmus_from, 5, 1, 1, 1)
        self.i_pmus_to = QtWidgets.QSpinBox(frame)
        self.i_pmus_to.setObjectName("grid-spin")
        self.i_pmus_to.setMinimum(0)
        self.i_pmus_to.setMaximum(100)
        self.gridLayout.addWidget(self.i_pmus_to, 5, 2, 1, 1)
        self.i_pmus_step = QtWidgets.QSpinBox(frame)
        self.i_pmus_step.setObjectName("grid-spin")
        self.i_pmus_step.setMinimum(1)
        self.gridLayout.addWidget(self.i_pmus_step, 5, 3, 1, 1)
        # Pmus increase
        self.label_i_pmus_inc = QLabel(frame)
        self.gridLayout.addWidget(self.label_i_pmus_inc, 6, 0, 1, 1)
        self.i_pmus_inc_from = QtWidgets.QSpinBox(frame)
        self.i_pmus_inc_from.setObjectName("grid-spin")
        self.i_pmus_inc_from.setMinimum(0)
        self.i_pmus_inc_from.setMaximum(100)
        self.gridLayout.addWidget(self.i_pmus_inc_from, 6, 1, 1, 1)
        self.i_pmus_inc_to = QtWidgets.QSpinBox(frame)
        self.i_pmus_inc_to.setObjectName("grid-spin")
        self.i_pmus_inc_to.setMinimum(0)
        self.i_pmus_inc_to.setMaximum(100)
        self.gridLayout.addWidget(self.i_pmus_inc_to, 6, 2, 1, 1)
        self.i_pmus_inc_step = QtWidgets.QSpinBox(frame)
        self.i_pmus_inc_step.setObjectName("grid-spin")
        self.i_pmus_inc_step.setMinimum(1)
        self.gridLayout.addWidget(self.i_pmus_inc_step, 6, 3, 1, 1)
        # Pmus hold
        self.label_i_pmus_hld = QLabel(frame)
        self.gridLayout.addWidget(self.label_i_pmus_hld, 7, 0, 1, 1)
        self.i_pmus_hld_from = QtWidgets.QSpinBox(frame)
        self.i_pmus_hld_from.setObjectName("grid-spin")
        self.i_pmus_hld_from.setMinimum(0)
        self.i_pmus_hld_from.setMaximum(100)
        self.gridLayout.addWidget(self.i_pmus_hld_from, 7, 1, 1, 1)
        self.i_pmus_hld_to = QtWidgets.QSpinBox(frame)
        self.i_pmus_hld_to.setObjectName("grid-spin")
        self.i_pmus_hld_to.setMinimum(0)
        self.i_pmus_hld_to.setMaximum(100)
        self.gridLayout.addWidget(self.i_pmus_hld_to, 7, 2, 1, 1)
        self.i_pmus_hld_step = QtWidgets.QSpinBox(frame)
        self.i_pmus_hld_step.setObjectName("grid-spin")
        self.i_pmus_hld_step.setMinimum(1)
        self.gridLayout.addWidget(self.i_pmus_hld_step, 7, 3, 1, 1)
        # Pmus hold
        self.label_i_pmus_rel = QLabel(frame)
        self.gridLayout.addWidget(self.label_i_pmus_rel, 8, 0, 1, 1)
        self.i_pmus_rel_from = QtWidgets.QSpinBox(frame)
        self.i_pmus_rel_from.setObjectName("grid-spin")
        self.i_pmus_rel_from.setMinimum(0)
        self.i_pmus_rel_from.setMaximum(100)
        self.gridLayout.addWidget(self.i_pmus_rel_from, 8, 1, 1, 1)
        self.i_pmus_rel_to = QtWidgets.QSpinBox(frame)
        self.i_pmus_rel_to.setObjectName("grid-spin")
        self.i_pmus_rel_to.setMinimum(0)
        self.i_pmus_rel_to.setMaximum(100)
        self.gridLayout.addWidget(self.i_pmus_rel_to, 8, 2, 1, 1)
        self.i_pmus_rel_step = QtWidgets.QSpinBox(frame)
        self.i_pmus_rel_step.setObjectName("grid-spin")
        self.i_pmus_rel_step.setMinimum(1)
        self.gridLayout.addWidget(self.i_pmus_rel_step, 8, 3, 1, 1)
        # Repetitions
        self.label_n_cycles = QLabel(frame)
        self.gridLayout.addWidget(self.label_n_cycles, 9, 0, 1, 1)
        self.n_cycles = QtWidgets.QSpinBox(frame)
        self.n_cycles.setObjectName("grid-spin")
        self.n_cycles.setMinimum(0)
        self.n_cycles.setMaximum(100)
        self.gridLayout.addWidget(self.n_cycles, 9, 1, 1, 1)
        # Informations
        separator = QtWidgets.QFrame(frame)
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(separator, 10, 0, 1, 4)
        self.label_tot_simus = QLabel(frame)
        self.gridLayout.addWidget(self.label_tot_simus, 11, 0, 1, 1)
        self.tot_simus = QLabel(frame)
        self.gridLayout.addWidget(self.tot_simus, 11, 1, 1, 1)
        self.label_tot_time = QLabel(frame)
        self.gridLayout.addWidget(self.label_tot_time, 12, 0, 1, 3)
        self.tot_time = QLabel(frame)
        self.gridLayout.addWidget(self.tot_time, 12, 1, 1, 3)
        # Progress
        self.progress = QProgressBar(frame)
        self.progress.setMaximumHeight(10)
        self.progress.setTextVisible(False)
        self.gridLayout.addWidget(self.progress, 13, 0, 1, 4)
        # Spacer
        spacerItem = QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 14, 0, 1, 4)

        self.h_layout.addLayout(self.gridLayout)
        spacerItem5 = QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_layout.addItem(spacerItem5)

        # Set size and position
        w, h = self.h_layout.sizeHint().toTuple()
        w_s, h_s = QApplication.primaryScreen().size().toTuple()
        x = round(w_s/2 - w/2)
        y = round(h_s/2 - h/2)
        BigScript.setCentralWidget(frame)
        BigScript.resize(w, h)
        BigScript.setMinimumSize(w, h)
        BigScript.move(x, y)

        # Hide the progress bar
        self.progress.setVisible(False)

        self.retranslateUi(BigScript)
        QtCore.QMetaObject.connectSlotsByName(BigScript)

    def retranslateUi(self, BigScript):
        self.label_from.setText(QtWidgets.QApplication.translate("BigScript", "Début", None, -1))
        self.label_to.setText(QtWidgets.QApplication.translate("BigScript", "Fin", None, -1))
        self.label_step.setText(QtWidgets.QApplication.translate("BigScript", "Pas", None, -1))

        self.label_r.setText(QtWidgets.QApplication.translate("BigScript", "Résistance", None, -1))
        self.label_c.setText(QtWidgets.QApplication.translate("BigScript", "Compliance", None, -1))
        self.label_br.setText(QtWidgets.QApplication.translate("BigScript", "Fréquence respi", None, -1))
        self.label_i_pmus.setText(QtWidgets.QApplication.translate("BigScript", "Pmus", None, -1))
        self.label_i_pmus_inc.setText(QtWidgets.QApplication.translate("BigScript", "Augmentation de Pmus", None, -1))
        self.label_i_pmus_hld.setText(QtWidgets.QApplication.translate("BigScript", "Plateau de Pmus", None, -1))
        self.label_i_pmus_rel.setText(QtWidgets.QApplication.translate("BigScript", "Diminution de Pmus", None, -1))

        self.label_n_cycles.setText(QtWidgets.QApplication.translate("BigScript", "Nombre de cycles", None, -1))

        self.label_tot_simus.setText(QtWidgets.QApplication.translate("BigScript", "Nombre de simulations", None, -1))
        self.label_tot_time.setText(QtWidgets.QApplication.translate("BigScript", "Temps total", None, -1))

    def hide_progress(self, reset=True):
        """
        Hide the progressbar

        Args:
            reset (bool): set the value to zero
        """

        if reset:
            self.progress.setValue(0)
        self.progress.setVisible(False)

    def show_progress(self, reset=True):
        """
        Show the progressbar

        Args:
            reset (bool): set the value to zero
        """

        if reset:
            self.progress.setValue(0)
        self.progress.setVisible(True)
