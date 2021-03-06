"""
A script object to load, save and show data
"""

import os
import re

from PySide2 import QtCore, QtWidgets

from src.common import io
from src.common import qt_utils
from src.config import Paths
from .vr3 import Vr3Var


class ModelVr3(Vr3Var):
    def __init__(self):
        Vr3Var.__init__(self)

    # =========================================================================
    # = Data
    # =========================================================================

    def load_new(self):
        """
        Load the default parameters for a script
        """

        data = io.json_load(Paths.file("new_model"))
        self.from_dict(data)

    # =========================================================================
    # = UI interaction
    # =========================================================================

    def setup_ui(self, ui):
        """
        Setup the values in the ui

        Args:
            ui (Ui_ModelVr3): Qt UI
        """

        # Is time varying enabled
        ui.check_time_constant.setChecked(self.time_var is False)

        # Set in tree
        ui.tree.clear()
        if self.time_var:
            ui.tree.setColumnCount(4)
            ui.tree.setHeaderLabels(["Variable", "Début", "Fin", "Répétitions"])
        else:
            ui.tree.setColumnCount(2)
            ui.tree.setHeaderLabels(["Variable", "Valeur"])

        # Set varying parameters
        for label, values in self.get_varying().items():
            item_main = QtWidgets.QTreeWidgetItem()
            item_main.setText(0, label)
            if self.time_var:
                for endpoints in values:
                    item = QtWidgets.QTreeWidgetItem(item_main)
                    for i, x in enumerate(endpoints, 1):
                        item.setText(i, str(x))
                    item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
                    ui.tree.addTopLevelItem(item)
            else:
                value = values[0][0]
                item_main.setText(1, str(value))
                item_main.setFlags(item_main.flags() | QtCore.Qt.ItemIsEditable)
            ui.tree.addTopLevelItem(item_main)

        # Set constant parameters
        for label, value in self.get_constant().items():
            item_main = QtWidgets.QTreeWidgetItem()
            item_main.setText(0, label)
            item_main.setText(1, str(value))
            item_main.setFlags(item_main.flags() | QtCore.Qt.ItemIsEditable)
            ui.tree.addTopLevelItem(item_main)

    def from_ui(self, ui):
        """
        Get data from the ui

        Args:
            ui (Ui_ModelVr3): Qt UI
        """

        data = self.to_dict()

        # If the parameters are time varying
        if self.time_var:
            for item in qt_utils.iter_tree(ui.tree):
                key = item.text(0)
                # If its a varying parameter
                if key in self.get_varying():
                    data["parameters"]["varying"][key].clear()
                    for child in qt_utils.iter_treeitem(item):
                        values = [child.text(i+1) for i in range(3)]
                        data["parameters"]["varying"][key].append(values)
                # If its a constant parameter
                else:
                    value = item.text(1)
                    data["parameters"]["constant"][key] = value

        # If the parameters are constants
        else:
            for item in qt_utils.iter_tree(ui.tree):
                key = item.text(0)
                value = item.text(1)
                # If its a varying parameter
                if key in self.get_varying():
                    data["parameters"]["varying"][key][0][0] = value
                # If its a constant parameter
                else:
                    data["parameters"]["constant"][key] = value

        self.from_dict(data)

        self.time_var = not ui.check_time_constant.isChecked()
