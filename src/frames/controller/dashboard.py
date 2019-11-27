import os

from PySide2.QtCore import (
    Qt
)
from PySide2.QtWidgets import (
    QFileDialog,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QWidget
)

from src.common import io
from src.common import qt_utils
import src.common.qt_utils.popup
from src.config import Paths
from src.common.objects import DashVr3
from src.frames.ui import Ui_Dashboard


class Dashboard(QMainWindow):
    def __init__(self, parent:QWidget=None):
        QMainWindow.__init__(self, parent)

        self.ui = Ui_Dashboard(self)

        # Menu
        self.ui.action_file_new.triggered.connect(self.menu_file_new)
        self.ui.action_file_open.triggered.connect(self.menu_file_open)
        self.ui.action_file_save.triggered.connect(self.menu_file_save)
        self.ui.action_file_saveas.triggered.connect(self.menu_file_saveas)
        self.ui.action_file_export.triggered.connect(self.menu_file_export)
        self.ui.action_file_quit.triggered.connect(self.destroy)
        self.ui.action_edit_copy.triggered.connect(self.menu_edit_copy)
        self.ui.action_edit_paste.triggered.connect(self.menu_edit_paste)

        # Setup items in the list
        for i in range(25):
            event = self.index_to_event_number(i)
            new = DashVr3()
            item = qt_utils.ListWidgetItem(event, new)
            self.ui.list.addItem(item)
            new.load_new()
        # Select first item
        item = self.ui.list.item(0)
        dash = item.get_data()
        self.ui.list.setCurrentItem(item)
        dash.setup_ui(self.ui)
        self.item_current = item
        self.file_current = self.ui.label_file.text()

        # Events
        self.ui.list.itemSelectionChanged.connect(self.evt_list_click)

    # =========================================================================
    # = Menu
    # =========================================================================

    def menu_file_new(self):
        """
        Reset all the elements to their default values
        """

        for item in qt_utils.iter_list(self.ui.list):
            data = item.get_data()
            data.load_new()

    def menu_file_open(self):
        """
        Open an existing dashboard file
        """

        file_dash, _ = QFileDialog.getOpenFileName(
            self,
            "Save ASL custom dashboard file",
            "",
            "ASL custom dashboard file (*.dashdata)"
        )
        if not file_dash:
            return
        # Get data from file
        data = io.json_load(file_dash)
        # Fill the list
        for row, dico in enumerate(data):
            item = self.ui.list.item(row)
            dash:DashVr3 = item.get_data()
            dash.from_dict(dico)
            item.set_data(dash)
        # Select first item
        item = self.ui.list.item(0)
        dash = item.get_data()
        self.item_current = item
        dash.setup_ui(self.ui)
        item.setSelected(True)
        # Update the title
        self.file_current = file_dash
        self.file_to_title(file_dash)

    def menu_file_save(self):
        """
        Save the current dashboard to the current file
        """

        if os.path.exists(self.file_current):
            try:
                # Save the dashboard
                self.save_dashboard()
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
        Ask where to save the current dashboard
        """

        file_dash, _ = QFileDialog.getSaveFileName(
            self,
            "Save ASL custom dashboard file",
            os.path.dirname(self.file_current),
            "ASL custom dashboard file (*.dashdata)"
        )
        if not file_dash:
            return
        # Update the title
        self.file_current = file_dash
        self.file_to_title(file_script)
        try:
            # Save the script
            self.save_dashboard()
            # Notify end of save
            qt_utils.popup.done(self, message="Sauvegarde terminée")
        except Exception as e:
            # Notify error
            # TODO: Popup error
            qt_utils.popup.done(self, message=str(e))

    def menu_file_export(self):
        """
        Ask where to export the dashboard
        """

        dir_dash = QFileDialog.getExistingDirectory(
            self,
            "Save ASL dashboard files",
            os.path.dirname(self.file_current)
        )
        if not dir_dash:
            return

        # Save current item
        self.save_current_item()
        # Get directory where vr3 are stored
        name = os.path.basename(dir_dash)
        dir_vr3 = os.path.join(dir_dash, f"{name} support files")
        os.makedirs(dir_vr3, exist_ok=True)
        # Get directory where vr3 will be stored
        path_support_vr3 = "C:\\Program Files (x86)\\ASL Software 3.6\\RespiSim_Modules\\{name}\\{name} support files\\{vr3}.vr3"
        path_support_rsp = "C:\\Program Files (x86)\\ASL Software 3.6\\RespiSim_Modules\\{name}\\{name} support files\\{name}.rsp"

        # Save vr3
        for i, item in qt_utils.enumer_list(self.ui.list, 1):
            vr3:DashVr3 = item.get_data()
            if vr3.enabled:
                path = os.path.join(dir_vr3, f"{item.text()}.vr3")
                vr3.export(path)

        # Save rsp
        with open(Paths.file("template_rsp")) as f:
            txt = f.read()
        file = f"{dir_vr3}/{name}.rsp"
        with open(file, "w") as f:
            f.write(txt.format(name=name))

        # Save xml
        export = dict()
        for i, item in qt_utils.enumer_list(self.ui.list):
            data = item.get_data().to_dict()
            vr3 = item.text()
            # > Extract a dict with only the parameters
            settings = {
                "vr3": f"{vr3}.vr3",
                **data["ventilator"],
                **data["scope"],
                "comment": data["comment"],
                "vr3path": path_support_vr3.format(name=name, vr3=vr3)
            }
            # If this simulation is not activated
            if data["active"] == 0:
                for k in settings.keys():
                    settings[k] = ""
            export[i] = settings
        # set rsp file
        export["rsppath"] = path_support_rsp.format(name=name)
        # Get template and fill it
        with open(Paths.file("template_xml")) as f:
            txt = f.read()
        file = f"{dir_dash}/{name}.xml"
        with open(file, "w") as f:
            # from pprint import pprint
            # pprint(export)
            f.write(txt.format(d=export))

        popup.done(self, message="Exportation terminée")

    def menu_edit_copy(self):
        """
        Copy the settings for the current event
        """

        self.vr3_copy.from_ui(self.ui, self.item_current.text())

    def menu_edit_paste(self):
        """
        Paste the saved settings to the current event
        """

        # If there is a copied vr3
        if self.vr3_copy.n > 0:
            vr3 = self.item_current.get_data()
            name = vr3.name
            vr3.from_dict(self.vr3_copy.to_dict())
            vr3.name = name
            vr3.setup_ui(self.ui)
            self.item_current.set_data(vr3)

    # =========================================================================
    # = Events
    # =========================================================================

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
        # Selected is now the current
        self.item_current = item

    # =========================================================================
    # = Save
    # =========================================================================

    def save_dashboard(self):
        """
        Save the current dashboad at the current file
        """

        # Get all item data
        data = list()
        self.save_current_item()
        for item in qt_utils.iter_list(self.ui.list):
            vr3 = item.get_data()
            data.append(vr3.to_dict())
        # Save them
        io.json_save(data, self.file_current)

    # =========================================================================
    # = Misc
    # =========================================================================

    def save_current_item(self):
        """
        Save current item
        """

        vr3 = self.item_current.get_data()
        vr3.from_ui(self.ui)
        self.item_current.set_data(vr3)

    def index_to_event_number(self, index:int) -> str:
        """
        Return the corresponding name for the index

        Args:
            index (int): row index

        Returns:
            str: name of the index
        """

        if index == 0:
            return "Initial event"
        else:
            stg = index - 1
            n = stg % 6 + 1
            event = stg // 6 + 1
            return f"Event {event} - Parameter {n}"

    def file_to_title(self, path:str):
        """
        Set the current file path as the title

        Args:
            path (str): path to file
        """

        title = os.path.basename(path)
        self.ui.label_file.setText(title)
