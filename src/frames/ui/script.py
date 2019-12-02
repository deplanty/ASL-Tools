from PySide2 import QtCore, QtGui, QtWidgets

from PySide2.QtCore import (
    Qt,
)
from PySide2.QtGui import (
    QIcon,
)
from PySide2.QtWidgets import (
    QAction,
    QHBoxLayout,
    QMainWindow,
    QMenu,
    QMenuBar,
    QSizePolicy,
    QSpacerItem,
    QWidget
)


class Ui_Script:
    def __init__(self, Script:QMainWindow):

        # Set window parameters
        Script.setWindowTitle("ASL Tools - Script")
        Script.setWindowFlag(Qt.Window)

        # Main frame
        frame = QWidget(Script)
        self.h_layout = QHBoxLayout(frame)

        # Menubar
        menubar = Script.menuBar()
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

        # Spacer
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.h_layout.addItem(spacer)

        # Main grid
        self.grid_layout = QtWidgets.QGridLayout()
        # Filename
        self.label_file = QtWidgets.QLabel(frame)
        self.label_file.setAlignment(QtCore.Qt.AlignCenter)
        self.label_file.setObjectName("label_file")
        self.grid_layout.addWidget(self.label_file, 0, 0, 1, 2)
        # Action widgets
        self.h_layout_actions = QtWidgets.QHBoxLayout()
        self.btn_add = QtWidgets.QToolButton(frame)
        self.btn_add.setEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add.setIcon(icon)
        self.btn_add.setIconSize(QtCore.QSize(24, 24))
        self.btn_add.setAutoRaise(True)
        self.h_layout_actions.addWidget(self.btn_add)
        self.btn_remove = QtWidgets.QToolButton(frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_remove.setIcon(icon)
        self.btn_remove.setIconSize(QtCore.QSize(24, 24))
        self.btn_remove.setAutoRaise(True)
        self.h_layout_actions.addWidget(self.btn_remove)
        self.btn_move_up = QtWidgets.QToolButton(frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/arrow-up.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_move_up.setIcon(icon)
        self.btn_move_up.setIconSize(QtCore.QSize(24, 24))
        self.btn_move_up.setAutoRaise(True)
        self.h_layout_actions.addWidget(self.btn_move_up)
        self.btn_move_down = QtWidgets.QToolButton(frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/arrow-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_move_down.setIcon(icon)
        self.btn_move_down.setIconSize(QtCore.QSize(24, 24))
        self.btn_move_down.setAutoRaise(True)
        self.h_layout_actions.addWidget(self.btn_move_down)
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.h_layout_actions.addItem(spacer)
        self.grid_layout.addLayout(self.h_layout_actions, 1, 0, 1, 1)
        # List widget
        self.list = QtWidgets.QListWidget(frame)
        self.grid_layout.addWidget(self.list, 2, 0, 1, 1)

        # Form
        self.grid_layout_form = QtWidgets.QGridLayout()
        # Compliance
        self.label_compliance = QtWidgets.QLabel(frame)
        self.grid_layout_form.addWidget(self.label_compliance, 0, 0, 1, 1)
        self.compliance = QtWidgets.QSpinBox(frame)
        self.compliance.setMaximum(500)
        self.grid_layout_form.addWidget(self.compliance, 0, 1, 1, 1)
        # Resistance
        self.label_resistance = QtWidgets.QLabel(frame)
        self.grid_layout_form.addWidget(self.label_resistance, 1, 0, 1, 1)
        self.resistance = QtWidgets.QSpinBox(frame)
        self.resistance.setMaximum(500)
        self.grid_layout_form.addWidget(self.resistance, 1, 1, 1, 1)
        # Respiratory rate
        self.label_respi_rate = QtWidgets.QLabel(frame)
        self.grid_layout_form.addWidget(self.label_respi_rate, 2, 0, 1, 1)
        self.respi_rate = QtWidgets.QSpinBox(frame)
        self.respi_rate.setMaximum(500)
        self.grid_layout_form.addWidget(self.respi_rate, 2, 1, 1, 1)
        # Spacer
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.grid_layout_form.addItem(spacerItem1, 4, 0, 1, 1)
        # Pmus insp
        self.label_i_pmus = QtWidgets.QLabel(frame)
        self.grid_layout_form.addWidget(self.label_i_pmus, 5, 0, 1, 1)
        self.i_pmus = QtWidgets.QSpinBox(frame)
        self.i_pmus.setMaximum(100)
        self.grid_layout_form.addWidget(self.i_pmus, 5, 1, 1, 1)
        # Pmus insp inc
        self.label_i_pmus_inc = QtWidgets.QLabel(frame)
        self.grid_layout_form.addWidget(self.label_i_pmus_inc, 6, 0, 1, 1)
        self.i_pmus_inc = QtWidgets.QSpinBox(frame)
        self.i_pmus_inc.setMaximum(100)
        self.grid_layout_form.addWidget(self.i_pmus_inc, 6, 1, 1, 1)
        # Pmus insp hold
        self.label_i_pmus_hld = QtWidgets.QLabel(frame)
        self.grid_layout_form.addWidget(self.label_i_pmus_hld, 7, 0, 1, 1)
        self.i_pmus_hld = QtWidgets.QSpinBox(frame)
        self.i_pmus_hld.setMaximum(100)
        self.grid_layout_form.addWidget(self.i_pmus_hld, 7, 1, 1, 1)
        # Pmus insp rel
        self.label_i_pmus_rel = QtWidgets.QLabel(frame)
        self.grid_layout_form.addWidget(self.label_i_pmus_rel, 8, 0, 1, 1)
        self.i_pmus_rel = QtWidgets.QSpinBox(frame)
        self.i_pmus_rel.setMaximum(100)
        self.grid_layout_form.addWidget(self.i_pmus_rel, 8, 1, 1, 1)
        # Spacer
        spacerItem4 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.grid_layout_form.addItem(spacerItem4, 9, 0, 1, 1)
        # Pmus exp
        self.label_e_pmus = QtWidgets.QLabel(frame)
        self.grid_layout_form.addWidget(self.label_e_pmus, 10, 0, 1, 1)
        self.e_pmus = QtWidgets.QSpinBox(frame)
        self.e_pmus.setMaximum(100)
        self.grid_layout_form.addWidget(self.e_pmus, 10, 1, 1, 1)
        # Pmus exp inc
        self.label_e_pmus_inc = QtWidgets.QLabel(frame)
        self.grid_layout_form.addWidget(self.label_e_pmus_inc, 11, 0, 1, 1)
        self.e_pmus_inc = QtWidgets.QSpinBox(frame)
        self.e_pmus_inc.setMaximum(100)
        self.grid_layout_form.addWidget(self.e_pmus_inc, 11, 1, 1, 1)
        # Pmus exp hold
        self.label_e_pmus_hld = QtWidgets.QLabel(frame)
        self.grid_layout_form.addWidget(self.label_e_pmus_hld, 12, 0, 1, 1)
        self.e_pmus_hld = QtWidgets.QSpinBox(frame)
        self.e_pmus_hld.setMaximum(100)
        self.grid_layout_form.addWidget(self.e_pmus_hld, 12, 1, 1, 1)
        # Pmus exp rel
        self.label_e_pmus_rel = QtWidgets.QLabel(frame)
        self.grid_layout_form.addWidget(self.label_e_pmus_rel, 13, 0, 1, 1)
        self.e_pmus_rel = QtWidgets.QSpinBox(frame)
        self.e_pmus_rel.setMaximum(100)
        self.grid_layout_form.addWidget(self.e_pmus_rel, 13, 1, 1, 1)
        # Spacer
        spacerItem3 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.grid_layout_form.addItem(spacerItem3, 14, 0, 1, 1)
        # CRF
        self.label_crf = QtWidgets.QLabel(frame)
        self.grid_layout_form.addWidget(self.label_crf, 15, 0, 1, 1)
        self.crf = QtWidgets.QDoubleSpinBox(frame)
        self.crf.setDecimals(1)
        self.crf.setSingleStep(0.1)
        self.grid_layout_form.addWidget(self.crf, 15, 1, 1, 1)
        # Spacer
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.grid_layout_form.addItem(spacerItem2, 16, 0, 1, 1)
        # Repetions
        self.label_repetitions = QtWidgets.QLabel(frame)
        self.grid_layout_form.addWidget(self.label_repetitions, 17, 0, 1, 1)
        self.repetitions = QtWidgets.QSpinBox(frame)
        self.repetitions.setMaximum(9999)
        self.grid_layout_form.addWidget(self.repetitions, 17, 1, 1, 1)
        self.label_repetitions_total = QtWidgets.QLabel(frame)
        self.label_repetitions_total.setMinimumWidth(30)
        self.grid_layout_form.addWidget(self.label_repetitions_total, 17, 2, 1, 1)
        # Spacer
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_layout_form.addItem(spacerItem2, 18, 0, 1, 1)
        # Set form layout in the main grid
        self.grid_layout.addLayout(self.grid_layout_form, 2, 1, 1, 1)
        self.h_layout.addLayout(self.grid_layout)

        # Spacer
        spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_layout.addItem(spacer)

        # Set size and position
        w, h = self.h_layout.sizeHint().toTuple()
        w_s, h_s = QApplication.primaryScreen().size().toTuple()
        x = round(w_s/2 - w/2)
        y = round(h_s/2 - h/2)
        Script.setCentralWidget(frame)
        Script.resize(w, h)
        Script.move(x, y)

        self.retranslateUi(Script)
        QtCore.QMetaObject.connectSlotsByName(Script)
        Script.setTabOrder(self.btn_add, self.btn_remove)
        Script.setTabOrder(self.btn_remove, self.btn_move_up)
        Script.setTabOrder(self.btn_move_up, self.btn_move_down)
        Script.setTabOrder(self.btn_move_down, self.list)
        Script.setTabOrder(self.list, self.compliance)
        Script.setTabOrder(self.compliance, self.resistance)
        Script.setTabOrder(self.resistance, self.respi_rate)
        Script.setTabOrder(self.respi_rate, self.i_pmus)
        Script.setTabOrder(self.i_pmus, self.i_pmus_inc)
        Script.setTabOrder(self.i_pmus_inc, self.i_pmus_hld)
        Script.setTabOrder(self.i_pmus_hld, self.i_pmus_rel)
        Script.setTabOrder(self.i_pmus_rel, self.e_pmus)
        Script.setTabOrder(self.e_pmus, self.e_pmus_inc)
        Script.setTabOrder(self.e_pmus_inc, self.e_pmus_hld)
        Script.setTabOrder(self.e_pmus_hld, self.e_pmus_rel)
        Script.setTabOrder(self.e_pmus_rel, self.crf)
        Script.setTabOrder(self.crf, self.repetitions)

    def retranslateUi(self, Script):
        self.label_i_pmus_inc.setText(QtWidgets.QApplication.translate("Script", "Pmus inspi aug (%)", None, -1))
        self.label_i_pmus.setText(QtWidgets.QApplication.translate("Script", "Pmus inspi (cmH2O)", None, -1))
        self.label_i_pmus_hld.setText(QtWidgets.QApplication.translate("Script", "Pmus inspi plateau (%)", None, -1))
        self.label_repetitions.setText(QtWidgets.QApplication.translate("Script", "Répétitions", None, -1))
        self.label_e_pmus.setText(QtWidgets.QApplication.translate("Script", "Pmus expi (cmH2O)", None, -1))
        self.label_e_pmus_inc.setText(QtWidgets.QApplication.translate("Script", "Pmus expi aug (%)", None, -1))
        self.label_e_pmus_hld.setText(QtWidgets.QApplication.translate("Script", "Pmus expi plateau (%)", None, -1))
        self.label_e_pmus_rel.setText(QtWidgets.QApplication.translate("Script", "Pmus expi dim (%)", None, -1))
        self.label_resistance.setText(QtWidgets.QApplication.translate("Script", "Résistances", None, -1))
        self.label_i_pmus_rel.setText(QtWidgets.QApplication.translate("Script", "Pmus inspi dim (%)", None, -1))
        self.label_crf.setText(QtWidgets.QApplication.translate("Script", "CRF (L)", None, -1))
        self.label_respi_rate.setText(QtWidgets.QApplication.translate("Script", "Fréquence respi", None, -1))
        self.label_compliance.setText(QtWidgets.QApplication.translate("Script", "Compliance", None, -1))
        self.label_repetitions_total.setText(QtWidgets.QApplication.translate("Script", "/20", None, -1))
        self.btn_add.setToolTip(QtWidgets.QApplication.translate("Script", "Ajouter une simulation", None, -1))
        self.btn_add.setText(QtWidgets.QApplication.translate("Script", "Ajouter", None, -1))
        self.btn_remove.setToolTip(QtWidgets.QApplication.translate("Script", "Supprimer une simulation", None, -1))
        self.btn_remove.setText(QtWidgets.QApplication.translate("Script", "Supprimer", None, -1))
        self.btn_move_up.setToolTip(QtWidgets.QApplication.translate("Script", "Déplacer une simulation vers le haut", None, -1))
        self.btn_move_up.setText(QtWidgets.QApplication.translate("Script", "Monter", None, -1))
        self.btn_move_down.setToolTip(QtWidgets.QApplication.translate("Script", "Déplacer ue simulation vers le bas", None, -1))
        self.btn_move_down.setText(QtWidgets.QApplication.translate("Script", "Descendre", None, -1))
        self.label_file.setToolTip(QtWidgets.QApplication.translate("Script", "Nom du fichier courant", None, -1))
        self.label_file.setText(QtWidgets.QApplication.translate("Script", "<aucun>", None, -1))
