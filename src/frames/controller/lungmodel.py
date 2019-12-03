import copy
import os

from PySide2.QtCore import (
    Qt,
    QModelIndex
)
from PySide2.QtWidgets import (
    QFileDialog,
    QMessageBox,
    QMainWindow,
    QTreeWidgetItem,
    QWidget
)

from src.common import io
from src.common import qt_utils
from src.common.objects import ModelVr3
from src.config import Paths
from src.frames.ui import Ui_LungModel


class LungModel(QMainWindow):
    def __init__(self, parent:QWidget=None):
        QMainWindow.__init__(self, parent)

        self.ui = Ui_LungModel(self)

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

        self.vr3 = ModelVr3()

        self.file_current = self.ui.label_file.text()
        self.menu_file_new()

    # =========================================================================
    # = Menu
    # =========================================================================

    def menu_file_new(self):
        """
        Open a new lung model
        """

        # Set current filename
        self.file_current = "<aucun>"
        self.file_to_title(self.file_current)
        # Load data
        self.vr3.load_new()
        self.vr3.setup_ui(self.ui)
        # Set the buttons state
        self.set_buttons_state()

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
        # Update the title
        self.file_current = file_vr3
        self.file_to_title(self.file_current)
        # Get data from file
        data = io.json_load(file_vr3)
        # Fill the ui
        self.vr3.from_dict(data)
        self.vr3.setup_ui(self.ui)
        # Set the buttons state
        self.set_buttons_state()

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
                qt_utils.popup.error(self, message=str(e))
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
            qt_utils.popup.error(self, message=str(e))

    def menu_file_export(self):
        file_vr3, _ = QFileDialog.getSaveFileName(
            self,
            "Save ASL lung model file",
            os.path.dirname(self.file_current),
            "ASL lung model file (*.vr3)"
        )
        if not file_vr3:
            return

        # Get the data from ui
        self.vr3.from_ui(self.ui)
        # Export the data
        self.vr3.export(file_vr3)

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
        if key and key not in self.vr3.get_varying():
            return

        # If select toplevel item
        if key:
            parent = item
        # If its a child
        else:
            parent = item.parent()

        # Add item at the end
        new = QTreeWidgetItem(parent)
        new.setText(1, "0")
        new.setText(2, "0")
        new.setText(3, "0")
        new.setFlags(new.flags() | Qt.ItemIsEditable)
        parent.addChild(new)

        self.set_buttons_state()

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

        self.set_buttons_state()

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

        self.set_buttons_state()

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

        self.set_buttons_state()

    # =========================================================================
    # = Events
    # =========================================================================

    def evt_time_constant(self):
        """
        When clicking on time constant checkbox
        Setup the ui as constant or varying
        Define the state of the buttons
        """

        # Save ui
        self.vr3.from_ui(self.ui)
        # Setup ui with correct parameters
        self.vr3.setup_ui(self.ui)

        self.set_buttons_state()

    def evt_select_item(self):
        """
        When an item is selected
        Define the state of the buttons
        """

        self.set_buttons_state()

    # =========================================================================
    # = Save
    # =========================================================================

    def save_model(self):
        """
        Save the current script at the current file
        """
        self.vr3.from_ui(self.ui)
        data = self.vr3.to_dict()
        io.json_save(data, self.file_current)

    # =========================================================================
    # = Misc
    # =========================================================================

    def file_to_title(self, path:str):
        """
        Set the current file path as the title

        Args:
            path (str): path to file
        """

        title = os.path.basename(path)
        self.ui.label_file.setText(title)

    def set_buttons_state(self):
        """
        Set the state of the buttons according to the item selected and the time varying
        """

        constant = self.ui.check_time_constant.isChecked()

        # If the parameters are constants
        if constant:
            # Disable the buttons
            self.disable_buttons("all")
        # Else look at the selected item
        else:
            items = self.ui.tree.selectedItems()
            if not items:
                self.disable_buttons("all")
                return
            selected:QTreeWidgetItem = items[0]

            # If its a toplevel
            if selected.text(0):
                self.disable_buttons("remove", "move_up", "move_down")
                self.enable_buttons("add")
            # If its a child
            else:
                parent:QTreeWidgetItem = selected.parent()
                n_children = parent.childCount()
                row = parent.indexOfChild(selected)
                # If only child
                if n_children == 1:
                    self.disable_buttons("remove", "move_up", "move_down")
                    self.enable_buttons("add")
                # If first child
                elif row == 0:
                    self.disable_buttons("move_up")
                    self.enable_buttons("add", "remove", "move_down")
                # If last child
                elif row == n_children - 1:
                    self.disable_buttons("move_down")
                    self.enable_buttons("add", "remove", "move_up")
                # Else
                else:
                    self.enable_buttons("all")

    def enable_buttons(self, *btns):
        """
        Enable the given buttons

        Args:
            *btns (str): [add, remove, move_up, move_down, all]
        """

        if "add" in btns or "all" in btns:
            self.ui.btn_add.setEnabled(True)
        if "remove" in btns or "all" in btns:
            self.ui.btn_remove.setEnabled(True)
        if "move_up" in btns or "all" in btns:
            self.ui.btn_move_up.setEnabled(True)
        if "move_down" in btns or "all" in btns:
            self.ui.btn_move_down.setEnabled(True)

    def disable_buttons(self, *btns):
        """
        Disable the given buttons

        Args:
            *btns (str): [add, remove, move_up, move_down, all]
        """

        if "add" in btns or "all" in btns:
            self.ui.btn_add.setEnabled(False)
        if "remove" in btns or "all" in btns:
            self.ui.btn_remove.setEnabled(False)
        if "move_up" in btns or "all" in btns:
            self.ui.btn_move_up.setEnabled(False)
        if "move_down" in btns or "all" in btns:
            self.ui.btn_move_down.setEnabled(False)
