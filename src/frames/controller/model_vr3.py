import copy
import os

from PySide2.QtCore import (
    Qt,
    QModelIndex
)
from PySide2.QtWidgets import (
    QFileDialog,
    QTreeWidgetItem,
    QMessageBox,
    QWidget
)

from src.common import io
from src.common import qt_utils
from src.config import Paths
from src.frames.ui import Ui_ModelVr3


class ModelVr3(QWidget):
    def __init__(self, parent:QWidget=None):
        QWidget.__init__(self, parent)

        self.ui = Ui_ModelVr3(self)

        # Menu
        self.ui.action_file_new.triggered.connect(self.menu_file_new)
        self.ui.action_file_open.triggered.connect(self.menu_file_open)
        self.ui.action_file_save.triggered.connect(self.menu_file_save)
        self.ui.action_file_saveas.triggered.connect(self.menu_file_saveas)
        self.ui.action_file_export.triggered.connect(self.menu_file_export)
        self.ui.action_file_quit.triggered.connect(self.destroy)

        # Buttons
        self.ui.btn_add.clicked.connect(self.btn_add)
        self.ui.btn_remove.clicked.connect(self.btn_remove)
        self.ui.btn_move_up.clicked.connect(self.btn_move_up)
        self.ui.btn_move_down.clicked.connect(self.btn_move_down)

        # Events
        self.ui.check_time_constant.clicked.connect(self.evt_time_constant)
        self.ui.tree.itemClicked.connect(self.evt_select_item)

        self.file_current = self.ui.label_file.text()
        self.current_data = dict()
        self.menu_file_new()

    # =========================================================================
    # = Menu
    # =========================================================================

    def menu_file_new(self):
        """
        Open a new lung model
        """

        self.file_current = "<aucun>"
        self.file_to_title(self.file_current)

        # Load data
        data = io.json_load(Paths.file("new_model"))
        # Set data in the ui
        self.set_in_ui(data)

    def menu_file_open(self):
        """
        Open an existing lung model
        """

        file_vr3, _ = QFileDialog.getOpenFileName(
            self,
            "Open ASL custom lung model file",
            "",
            "ASL custom lung model file (*.vr3data)"
        )
        if not file_vr3:
            return
        # Get data from file
        data = io.json_load(file_vr3)
        # Fill the ui
        self.set_in_ui(data)
        # Update the title
        self.file_current = "<aucun>"
        self.file_to_title(self.file_current)

    def menu_file_save(self):
        """
        Save the lung model as the current file
        If there is no file, ask where to save
        """

        if os.path.exists(self.file_current):
            try:
                # Save the script
                self.save_model()
                # Notify end of save
                qt_utils.popup.done(self, message="Sauvegarde terminée")
            except Exception as e:
                # Notify error
                # TODO: Popup error
                qt_utils.popup.done(self, message=str(e))
        else:
            self.menu_file_saveas()

    def menu_file_saveas(self):
        """
        Ask where to save the lung model and save it
        """

        file_vr3, _ = QFileDialog.getSaveFileName(
            self,
            "Save ASL custom lung model file",
            os.path.dirname(self.file_current),
            "ASL custom lung model file (*.vr3data)"
        )
        if not file_vr3:
            return
        # Update the title
        self.file_current = file_vr3
        self.file_to_title(file_vr3)
        try:
            # Save the script
            self.save_model()
            # Notify end of save
            qt_utils.popup.done(self, message="Sauvegarde terminée")
        except Exception as e:
            # Notify error
            # TODO: Popup error
            qt_utils.popup.done(self, message=str(e))

    def menu_file_export(self):
        ...

        # TODO: export Vr3 model

    # =========================================================================
    # = Buttons
    # =========================================================================

    def btn_add(self):
        """
        Add a new child for the time varying parameters
        """

        items = self.ui.tree.selectedItems()
        if not items:
            return
        item:QTreeWidgetItem = items[0]

        key = item.text(0)
        # Only for time varying parameters
        if key in self.current_data["parameters"]["constant"]:
            return

        # If select toplevel item
        if key:
            # Add item at the end
            new = QTreeWidgetItem(item)
            new.setText(1, "0")
            new.setText(2, "0")
            new.setText(3, "0")
            item.addChild(new)
        # If its a child
        else:
            # Add a new item to the parent
            parent:QTreeWidgetItem = item.parent()
            print("add")
            # Add item at the end
            new = QTreeWidgetItem(parent)
            new.setText(1, "0")
            new.setText(2, "0")
            new.setText(3, "0")
            parent.addChild(new)

        new.setFlags(new.flags() | Qt.ItemIsEditable)

        self.evt_select_item()

    def btn_remove(self):
        """
        Remove a step in the time varying parameters
        """

        items = self.ui.tree.selectedItems()
        if not items:
            return
        item:QTreeWidgetItem = items[0]

        # If a toplevel item
        if item.text(0):
            return

        # If there is no more child
        if item.parent().childCount() == 1:
            return

        ans = QMessageBox.question(
            self,
            "Confirmation",
            "Confirmez-vous la suppression de cet élément ?",
            QMessageBox.Yes,
            QMessageBox.No
        )
        if ans == QMessageBox.Yes:
            next_item = self.ui.tree.itemBelow(item) if self.ui.tree.itemAbove(item).text(0) else self.ui.tree.itemAbove(item)
            item.parent().removeChild(item)
            self.ui.tree.clearSelection()
            next_item.setSelected(True)

        self.evt_select_item()

    def btn_move_up(self):
        """
        Move the item one step up
        """

        items = self.ui.tree.selectedItems()
        if not items:
            return
        item:QTreeWidgetItem = items[0]

        # If toplevel item
        if item.text(0):
            return

        # Row of item
        row = item.parent().indexOfChild(item)
        if row > 0:
            parent = item.parent()
            parent.removeChild(item)
            parent.insertChild(row-1, item)

            self.ui.tree.clearSelection()
            item.setSelected(True)

        self.evt_select_item()

    def btn_move_down(self):
        """
        Move the item one step down
        """

        items = self.ui.tree.selectedItems()
        if not items:
            return
        item:QTreeWidgetItem = items[0]

        # If toplevel item
        if item.text(0):
            return

        # Row of item
        parent = item.parent()
        row = parent.indexOfChild(item)
        row_max = parent.childCount()
        if row < row_max-1:
            parent.removeChild(item)
            parent.insertChild(row+1, item)

            self.ui.tree.clearSelection()
            item.setSelected(True)

        self.evt_select_item()

    # =========================================================================
    # = Events
    # =========================================================================

    def evt_time_constant(self):
        constant = self.ui.check_time_constant.isChecked()

        buttons = (
            self.ui.btn_add,
            self.ui.btn_remove,
            self.ui.btn_move_up,
            self.ui.btn_move_down
        )
        for btn in buttons:
            btn.setEnabled(constant is False)

        data = self.as_dict()
        self.set_in_ui(data)

    def evt_select_item(self):
        """
        When an item is selected
        """

        print("Trigger event")

        items = self.ui.tree.selectedItems()
        if not items:
            return
        selected:QTreeWidgetItem = items[0]

        # If its a toplevel
        if selected.text(0):
            self.disable_btns("remove", "move_up", "move_down")
            self.enable_btns("add")
        # If its a child
        else:
            parent:QTreeWidgetItem = selected.parent()
            n_children = parent.childCount()
            row = parent.indexOfChild(selected)
            # If only child
            if n_children == 1:
                self.disable_btns("remove", "move_up", "move_down")
                self.enable_btns("add")
            # If first child
            elif row == 0:
                self.disable_btns("move_up")
                self.enable_btns("add", "remove", "move_down")
            # If last child
            elif row == n_children - 1:
                self.disable_btns("move_down")
                self.enable_btns("add", "remove", "move_up")
            # Else
            else:
                self.enable_btns("add", "remove", "move_up", "move_down")

    # =========================================================================
    # = Save
    # =========================================================================

    def save_model(self):
        """
        Save the current script at the current file
        """

        data = self.as_dict()
        io.json_save(data, self.file_current)

    # =========================================================================
    # = Misc
    # =========================================================================

    def set_in_ui(self, data:dict):
        """
        Set the data in the ui

        Args:
            data (dict): vr3 model as a dict
        """

        self.current_data = data

        # Is time varying enabled
        timevar = data["flags"]["timevar"]
        self.ui.check_time_constant.setChecked(timevar is False)

        # Set in tree
        tree = self.ui.tree
        tree.clear()
        if timevar:
            tree.setColumnCount(4)
            tree.setHeaderLabels(["Variable", "Début", "Fin", "Répétitions"])
        else:
            tree.setColumnCount(2)
            tree.setHeaderLabels(["Variable", "Valeur"])

        # Set varying parameters
        varying = data["parameters"]["varying"]
        for label, values in varying.items():
            item_main = QTreeWidgetItem()
            item_main.setText(0, label)
            if timevar:
                for endpoints in values:
                    item = QTreeWidgetItem(item_main)
                    for i, x in enumerate(endpoints, 1):
                        item.setText(i, str(x))
                    item.setFlags(item.flags() | Qt.ItemIsEditable)
                    tree.addTopLevelItem(item)
            else:
                value = values[0][0]
                item_main.setText(1, str(value))
                item_main.setFlags(item_main.flags() | Qt.ItemIsEditable)
            tree.addTopLevelItem(item_main)

        # Set constant parameters
        constants = data["parameters"]["constant"]
        for label, value in constants.items():
            item_main = QTreeWidgetItem()
            item_main.setText(0, label)
            item_main.setText(1, str(value))
            item_main.setFlags(item_main.flags() | Qt.ItemIsEditable)
            tree.addTopLevelItem(item_main)

    def as_dict(self):
        """
        Return the ui data as a dict
        """

        data = copy.deepcopy(self.current_data)
        constant = not data["flags"]["timevar"]

        var = data["parameters"]["varying"]
        con = data["parameters"]["constant"]
        for i in range(self.ui.tree.topLevelItemCount()):
            item:QTreeWidgetItem = self.ui.tree.topLevelItem(i)
            key = item.text(0)

            # If it's a constant parameter
            if key in con:
                tp = float if key == "CRF" else int
                con[key] = tp(item.text(1))
            # A varying parameter
            else:
                # Constant is set
                if constant:
                    var[key][0][0] = int(item.text(1))
                # Time varying is set
                else:
                    for j in range(item.childCount()):
                        child = item.child(j)
                        var[key][j][0] = int(child.text(1))
                        var[key][j][1] = int(child.text(2))
                        var[key][j][2] = int(child.text(3))

        constant = self.ui.check_time_constant.isChecked()
        data["flags"]["timevar"] = constant is False

        return data

    def file_to_title(self, path:str):
        """
        Set the current file path as the title

        Args:
            path (str): path to file
        """

        title = os.path.basename(path)
        self.ui.label_file.setText(title)

    def enable_btns(self, *btns):
        """
        Enable the given buttons

        Args:
            *btns (str): [add, remove, move_up, move_down]
        """

        if "add" in btns:
            self.ui.btn_add.setEnabled(True)
        if "remove" in btns:
            self.ui.btn_remove.setEnabled(True)
        if "move_up" in btns:
            self.ui.btn_move_up.setEnabled(True)
        if "move_down" in btns:
            self.ui.btn_move_down.setEnabled(True)

    def disable_btns(self, *btns):
        """
        Disable the given buttons

        Args:
            *btns (str): [add, remove, move_up, move_down]
        """

        if "add" in btns:
            self.ui.btn_add.setEnabled(False)
        if "remove" in btns:
            self.ui.btn_remove.setEnabled(False)
        if "move_up" in btns:
            self.ui.btn_move_up.setEnabled(False)
        if "move_down" in btns:
            self.ui.btn_move_down.setEnabled(False)
