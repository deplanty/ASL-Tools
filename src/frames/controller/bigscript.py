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
from src.frames.ui import Ui_BigScript


class BigScript(QMainWindow):
    def __init__(self, parent:QWidget=None):
        QMainWindow.__init__(self, parent)

        self.ui = Ui_BigScript(self)

        # Menu
        self.ui.action_file_new.triggered.connect(self.menu_file_new)
        self.ui.action_file_save.triggered.connect(self.menu_file_save)
        self.ui.action_file_saveas.triggered.connect(self.menu_file_saveas)
        self.ui.action_file_export.triggered.connect(self.menu_file_export)
        self.ui.action_file_quit.triggered.connect(self.destroy)

        # Events

    # =========================================================================
    # = Menu
    # =========================================================================

    def menu_file_new(self):
        """
        Reset all the elements to their default values
        """

        ...

    def menu_file_save(self):
        """
        Save the current dashboard to the current file
        """

        if os.path.exists(self.file_current):
            try:
                # Save the dashboard
                self.save_bigscript()
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
        Ask where to save the current script
        """

        file_dash, _ = QFileDialog.getSaveFileName(
            self,
            "Save ASL custom script file",
            os.path.dirname(self.file_current),
            "ASL custom script file (*.scpdata)"
        )
        if not file_dash:
            return
        # Update the title
        self.file_current = file_dash
        self.file_to_title(file_script)
        try:
            # Save the script
            self.save_bigscript()
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
            "Save ASL script files",
            os.path.dirname(self.file_current)
        )
        if not dir_dash:
            return

        raise NotImplementedError()

        popup.done(self, message="Exportation terminée")

    # =========================================================================
    # = Save
    # =========================================================================

    def save_bigscript(self):
        """
        Save the bigscript as scpdata
        """

        raise NotImplementedError()
