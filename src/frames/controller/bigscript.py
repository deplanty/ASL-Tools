import itertools
import json
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
from src.common.objects import ScriptVr3
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

        self.file_current = self.ui.label_file.text()
        self.menu_file_new()
        self.evt_set_info()

        # Events
        self.ui.r_from.valueChanged.connect(self.evt_set_info)
        self.ui.r_to.valueChanged.connect(self.evt_set_info)
        self.ui.r_step.valueChanged.connect(self.evt_set_info)
        self.ui.c_from.valueChanged.connect(self.evt_set_info)
        self.ui.c_to.valueChanged.connect(self.evt_set_info)
        self.ui.c_step.valueChanged.connect(self.evt_set_info)
        self.ui.br_from.valueChanged.connect(self.evt_set_info)
        self.ui.br_to.valueChanged.connect(self.evt_set_info)
        self.ui.br_step.valueChanged.connect(self.evt_set_info)
        self.ui.i_pmus_from.valueChanged.connect(self.evt_set_info)
        self.ui.i_pmus_to.valueChanged.connect(self.evt_set_info)
        self.ui.i_pmus_step.valueChanged.connect(self.evt_set_info)
        self.ui.i_pmus_inc_from.valueChanged.connect(self.evt_set_info)
        self.ui.i_pmus_inc_to.valueChanged.connect(self.evt_set_info)
        self.ui.i_pmus_inc_step.valueChanged.connect(self.evt_set_info)
        self.ui.i_pmus_hld_from.valueChanged.connect(self.evt_set_info)
        self.ui.i_pmus_hld_to.valueChanged.connect(self.evt_set_info)
        self.ui.i_pmus_hld_step.valueChanged.connect(self.evt_set_info)
        self.ui.i_pmus_rel_from.valueChanged.connect(self.evt_set_info)
        self.ui.i_pmus_rel_to.valueChanged.connect(self.evt_set_info)
        self.ui.i_pmus_rel_step.valueChanged.connect(self.evt_set_info)
        self.ui.n_cycles.valueChanged.connect(self.evt_set_info)

    # =========================================================================
    # = Menu
    # =========================================================================

    def menu_file_new(self):
        """
        Reset all the elements to their default values
        """

        self.ui.r_from.setValue(5)
        self.ui.r_to.setValue(5)
        self.ui.r_step.setValue(1)
        self.ui.c_from.setValue(60)
        self.ui.c_to.setValue(60)
        self.ui.c_step.setValue(1)
        self.ui.br_from.setValue(20)
        self.ui.br_to.setValue(20)
        self.ui.br_step.setValue(1)
        self.ui.i_pmus_from.setValue(5)
        self.ui.i_pmus_to.setValue(5)
        self.ui.i_pmus_step.setValue(1)
        self.ui.i_pmus_inc_from.setValue(20)
        self.ui.i_pmus_inc_to.setValue(20)
        self.ui.i_pmus_inc_step.setValue(1)
        self.ui.i_pmus_rel_from.setValue(20)
        self.ui.i_pmus_rel_to.setValue(20)
        self.ui.i_pmus_rel_step.setValue(1)
        self.ui.i_pmus_hld_from.setValue(0)
        self.ui.i_pmus_hld_to.setValue(0)
        self.ui.i_pmus_hld_step.setValue(1)
        self.ui.n_cycles.setValue(4)

        self.file_current = "<aucun>"
        self.file_to_title(self.file_current)

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

        file_bigscript, _ = QFileDialog.getSaveFileName(
            self,
            "Save ASL custom script file",
            os.path.dirname(self.file_current),
            "ASL custom script file (*.scpdata)"
        )
        if not file_bigscript:
            return
        # Update the title
        self.file_current = file_bigscript
        self.file_to_title(file_bigscript)
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
    # = Events
    # =========================================================================

    def evt_set_info(self):
        """
        Set the information when modifying a parameter
        """

        comb = self.get_combs()
        n = len(comb)
        self.ui.tot_simus.setText(str(n))

        tot_time = float()
        list_br = self.get_range("br")
        n_br = len(list_br) - 1
        for br in list_br:
            tot_time += 60.0 / br * (n - n_br) * self.ui.n_cycles.value()

        m, s = divmod(tot_time, 60)
        h, m = divmod(m, 60)
        self.ui.tot_time.setText(f"{h:02.0f}:{m:02.0f}:{s:02.0f}")

    # =========================================================================
    # = Save
    # =========================================================================

    def save_bigscript(self):
        """
        Save the bigscript as scpdata
        """

        comb = self.get_combs()

        script = list()
        for i, line in enumerate(comb):
            vr3 = ScriptVr3()
            vr3.load_new()
            vr3.name = "%05d" % i
            vr3.n = self.ui.n_cycles.value()
            vr3.r = line[0]
            vr3.c = line[1]
            vr3.br = line[2]
            vr3.i_pmus = line[3]
            vr3.i_pmus_inc = line[4]
            vr3.i_pmus_hld = line[4]
            vr3.i_pmus_rel = line[4]
            script.append(vr3.to_dict())

        with open(self.file_current, "w", encoding="utf-8") as f:
            json.dump(script, f)

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

    def range(self, from_, to, step=1):
        """
        Return the range [`from_`, `to`] with a `step`

        Args:
            from_ (int): first value
            to (int): last value
            step (int): number of steps between the first and last value
        """

        n = int((to - from_) / step) + 1
        x = list()
        for i in range(n):
            x.append(from_ + step * i)
        return x

    def get_range(self, var:str):
        """
        Get the range [from, to, step] of the variable

        Args:
            var (str): name of the variable (r, c, br, i_pums, i_pmus_inc, i_pmus_hld, i_pmus_rel)

        Returns:
            list: range with from and to included
        """

        from_, to, step = {
            "r": [self.ui.r_from.value(), self.ui.r_to.value(), self.ui.r_step.value()],
            "c": [self.ui.c_from.value(), self.ui.c_to.value(), self.ui.c_step.value()],
            "br": [self.ui.br_from.value(), self.ui.br_to.value(), self.ui.br_step.value()],
            "i_pmus": [self.ui.i_pmus_from.value(), self.ui.i_pmus_to.value(), self.ui.i_pmus_step.value()],
            "i_pmus_inc": [self.ui.i_pmus_inc_from.value(), self.ui.i_pmus_inc_to.value(), self.ui.i_pmus_inc_step.value()],
            "i_pmus_hld": [self.ui.i_pmus_hld_from.value(), self.ui.i_pmus_hld_to.value(), self.ui.i_pmus_hld_step.value()],
            "i_pmus_rel": [self.ui.i_pmus_rel_from.value(), self.ui.i_pmus_rel_to.value(), self.ui.i_pmus_rel_step.value()],
        }.get(var)
        return self.range(from_, to, step)

    def get_combs(self):
        """
        Return the combinations of the parameters

        Returns:
            list: combinations
        """

        values = [
            self.get_range("r"),
            self.get_range("c"),
            self.get_range("br"),
            self.get_range("i_pmus"),
            self.get_range("i_pmus_inc"),
            self.get_range("i_pmus_hld"),
            self.get_range("i_pmus_rel"),
        ]
        return list(itertools.product(*values))
