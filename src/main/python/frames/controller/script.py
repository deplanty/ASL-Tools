import os

from PySide2.QtCore import (
    Qt
)
from PySide2.QtWidgets import (
    QFileDialog,
    QListWidgetItem,
    QMessageBox,
    QWidget
)

from common import io
from common import qt_utils
import common.qt_utils.popup
from config import Paths
from common.objects import ScriptVr3
from frames.ui import Ui_Script


class Script(QWidget):
    def __init__(self, parent:QWidget=None):
        QWidget.__init__(self, parent)

        self.ui = Ui_Script(self)

        self.ui.btn_add.clicked.connect(self.btn_add)
        self.ui.btn_remove.clicked.connect(self.btn_remove)
        self.ui.btn_move_up.clicked.connect(self.btn_move_up)
        self.ui.btn_move_down.clicked.connect(self.btn_move_down)
        self.ui.btn_open.clicked.connect(self.btn_open)
        self.ui.btn_save.clicked.connect(self.btn_save)
        self.ui.btn_export.clicked.connect(self.btn_export)
        self.ui.list.itemSelectionChanged.connect(self.evt_list_click)
        self.ui.list.itemChanged.connect(self.evt_list_change)
        self.ui.repetitions.valueChanged.connect(self.evt_rep_change)

        self.item_current = qt_utils.ListWidgetItem()
        self.file_current = self.ui.label_file.text()
        self.add_new()

    # =========================================================================
    # = Data
    # =========================================================================

    def add_new(self, data:dict=None):
        """
        Load the default parameters
        """

        new = ScriptVr3()
        item = qt_utils.ListWidgetItem(data=new)
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.ui.list.addItem(item)
        self.ui.list.setCurrentItem(item)
        self.item_current = item

        if data:
            new.from_dict(data)
        else:
            new.load_new()
        new.setup_ui(self.ui)

    # =========================================================================
    # = Buttons
    # =========================================================================

    def btn_add(self):
        self.save_current_item()
        self.add_new()
        self.evt_rep_change()

    def btn_remove(self):
        item = self.ui.list.currentItem()
        if not item:
            return

        ans = QMessageBox.question(
            self,
            "Confirmation",
            "Confirmez-vous la suppression de cet élément ?",
            QMessageBox.Yes,
            QMessageBox.No
        )
        if ans == QMessageBox.Yes:
            self.ui.list.takeItem(self.ui.list.row(item))

    def btn_move_up(self):
        item = self.ui.list.currentItem()
        if not item:
            return

        row = self.ui.list.row(item)
        self.ui.list.takeItem(row)
        self.ui.list.insertItem(row-1, item)
        self.ui.list.setCurrentItem(item)

    def btn_move_down(self):
        item = self.ui.list.currentItem()
        if not item:
            return

        row = self.ui.list.row(item)
        self.ui.list.takeItem(row)
        self.ui.list.insertItem(row+1, item)
        self.ui.list.setCurrentItem(item)

    def btn_open(self):
        file_script, _ = QFileDialog.getOpenFileName(
            self,
            "Save ASL custom script file",
            "",
            "ASL custom script file (*.scpdata)"
        )
        if not file_script:
            return
        # Get data from file
        data = io.json_load(file_script)
        # Fill the list
        self.ui.list.clear()
        for dico in data:
            self.add_new(dico)
        # Update the title
        self.file_current = file_script
        self.file_to_title(file_script)

    def btn_save(self):
        file_script, _ = QFileDialog.getSaveFileName(
            self,
            "Save ASL custom script file",
            os.path.dirname(self.file_current),
            "ASL custom script file (*.scpdata)"
        )
        if not file_script:
            return
        # Get all item data
        data = list()
        for item in qt_utils.iter_list(self.ui.list):
            vr3 = item.get_data()
            data.append(vr3.to_dict())
        # Save them
        io.json_save(data, file_script)
        # Update the title
        self.file_current = file_script
        self.file_to_title(file_script)

        qt_utils.popup.done(self, message="Sauvegarde terminée")

    def btn_export(self):
        file_script, _ = QFileDialog.getSaveFileName(
            self,
            "Save ASL script file",
            os.path.dirname(self.file_current),
            "ASL script file (*.sct)"
        )
        if not file_script:
            return

        # Save current item
        self.save_current_item()
        # Get directory where vr3 are stored
        dir_vr3, _ = os.path.splitext(file_script)
        dirname = os.path.basename(dir_vr3)
        os.makedirs(dir_vr3, exist_ok=True)
        # Get directory where vr3 will be stored
        scenario = f"<ASLVarsDirectory>\\scenarios\\{dirname}"
        with open(file_script, "w") as f:
            for i, item in qt_utils.enumer_list(self.ui.list, 1):
                vr3:ScriptVr3 = item.get_data()
                filename = vr3.export(dir_vr3, i)
                f.write(f"{vr3.n}\t{scenario}\\{filename}\n")

    def evt_list_click(self):
        """
        When clicking on item in list
        """

        item = self.ui.list.currentItem()
        if not item or not item.text():
            return

        # Save current item
        self.save_current_item()
        # Set clicked item
        vr3 = item.get_data()
        vr3.setup_ui(self.ui)
        # Calculate new repetition total
        self.evt_rep_change()
        # Selected is now the current
        self.item_current = item

    def evt_list_change(self):
        """
        When item name in list change
        """

        item = self.ui.list.currentItem()
        if not item:
            return

        # Save given name
        vr3 = item.get_data()
        vr3.name = item.text()
        item.set_data(vr3)
        # Set the item as current
        self.item_current = item

    def evt_rep_change(self):
        """
        When the number of repetition change
        """

        self.update_total_repetitions()

    # =========================================================================
    # = Misc
    # =========================================================================

    def save_current_item(self):
        """
        Save current item
        """

        vr3 = self.item_current.get_data()
        vr3.from_ui(self.ui, self.item_current.text())
        self.item_current.set_data(vr3)

    def update_total_repetitions(self):
        """
        Update the total number of repetitions
        """

        n = 0
        for item in qt_utils.iter_list(self.ui.list):
            vr3:ScriptVr3 = item.get_data()
            n += vr3.n

        self.ui.label_repetitions_total.setText(f"/{n}")

    def file_to_title(self, path:str):
        """
        Set the current file path as the title

        Args:
            path (str): path to file
        """

        title = os.path.basename(path)
        self.ui.label_file.setText(title)
