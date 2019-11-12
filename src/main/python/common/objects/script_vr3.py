"""
A script object to load, save and show data
"""

import os
import re

from common import io
from config import Paths
from .vr3 import Vr3


class ScriptVr3(Vr3):
    def __init__(self):
        Vr3.__init__(self)

        self.extpmus = str()
        self.name = str()
        self.n = int()

    # =========================================================================
    # = Data
    # =========================================================================

    def from_dict(self, data:dict):
        """
        Load the data from a dictionnary

        Args:
            data (dict): the data
        """

        self.extpmus = data["extpmus"]
        self.name = data["name"]
        self.n = data["n"]

        vr3 = data["vr3"]
        Vr3.from_dict(self, vr3)

    def to_dict(self):
        """
        Return the data as a dict

        Returns:
            dict: the data
        """

        return {
            "extpmus": "",
            "name": self.name,
            "n": self.n,
            "vr3": Vr3.to_dict(self)
        }

    def load_new(self):
        """
        Load the default parameters for a script
        """

        data = io.json_load(Paths.file("new_script"))
        self.from_dict(data)

    # =========================================================================
    # = UI interaction
    # =========================================================================

    def setup_ui(self, ui):
        """
        Setup the values in the ui

        Args:
            ui (Ui_Script): Qt UI
        """

        item = ui.list.currentItem()
        if not item:
            return

        item.setText(self.name)
        ui.repetitions.setValue(self.n)

        ui.compliance.setValue(self.c)
        ui.resistance.setValue(self.r)
        ui.respi_rate.setValue(self.br)
        ui.i_pmus.setValue(self.i_pmus)
        ui.i_pmus_inc.setValue(self.i_pmus_inc)
        ui.i_pmus_hld.setValue(self.i_pmus_hld)
        ui.i_pmus_rel.setValue(self.i_pmus_rel)
        ui.e_pmus.setValue(self.e_pmus)
        ui.e_pmus_inc.setValue(self.e_pmus_inc)
        ui.e_pmus_hld.setValue(self.e_pmus_hld)
        ui.e_pmus_rel.setValue(self.e_pmus_rel)
        ui.crf.setValue(self.crf)

    def from_ui(self, ui, name):
        item = ui.list.currentItem()
        if not item:
            return

        self.name = name
        self.n = ui.repetitions.value()

        self.c = ui.compliance.value()
        self.r = ui.resistance.value()
        self.br = ui.respi_rate.value()
        self.i_pmus = ui.i_pmus.value()
        self.i_pmus_inc = ui.i_pmus_inc.value()
        self.i_pmus_hld = ui.i_pmus_hld.value()
        self.i_pmus_rel = ui.i_pmus_rel.value()
        self.e_pmus = ui.e_pmus.value()
        self.e_pmus_inc = ui.e_pmus_inc.value()
        self.e_pmus_hld = ui.e_pmus_hld.value()
        self.e_pmus_rel = ui.e_pmus_rel.value()
        self.crf = ui.crf.value()

    # =========================================================================
    # = Exportation
    # =========================================================================

    def export(self, folder, number=None):
        """
        Export the vr3 to the folder

        Args:
            folder (str): path to the folder
            number (int, optional): number of the simulation

        Returns:
            str: name of the exported file
        """

        name = re.sub(r"\s+", "_", self.name)
        if number is not None:
            filename = f"{number:04d}_{name}.vr3"
        else:
            filename = f"{name}.vr3"

        path = os.path.join(folder, filename)
        Vr3.export(self, path)

        return os.path.basename(path)

    # =========================================================================
    # = Magics
    # =========================================================================

    def __str__(self):
        return f"ScriptVr3 {self.name}: R{self.r} C{self.c} x{self.n}"
