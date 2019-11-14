"""
A dash object to load, save and show data
"""

import os
import re

from src.common import io
from src.config import Paths
from .vr3 import Vr3


class DashVr3(Vr3):
    def __init__(self):
        Vr3.__init__(self)

        self.enabled = int()
        self.comment = str()

    # =========================================================================
    # = Data
    # =========================================================================

    def from_dict(self, data:dict):
        """
        Load the data from a dictionnary

        Args:
            data (dict): the data
        """

        # Misc
        self.enabled = data["active"]
        self.comment = data["comment"]
        # lung model
        vr3 = data["vr3"]
        Vr3.from_dict(self, vr3)

    def to_dict(self):
        """
        Return the data as a dict

        Returns:
            dict: the data
        """

        return {
            "active": self.enabled,
            "comment": self.comment,
            "vr3": Vr3.to_dict(self),
            "scope": {
                "HR": "",
                "BP_sys": "",
                "BP_dia": "",
                "SpO2": "",
                "EtCO2": ""
            },
            "ventilator": {
                "Mode": "",
                "Vt": "",
                "BR": "",
                "PEEP": "",
                "Rate": "",
                "Trig_insp": "",
                "FiO2": ""
            }
        }

    def load_new(self):
        """
        Load the default parameters for a script
        """

        data = io.json_load(Paths.file("new_dash"))
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

        # Misc
        ui.enabled.setChecked(self.enabled)
        ui.comment.setText(self.comment)
        # Lung model
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

    def from_ui(self, ui):
        item = ui.list.currentItem()
        if not item:
            return

        # Misc
        self.enabled = int(ui.enabled.isChecked())
        self.comment = ui.comment.toPlainText()
        # Lung model
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
    # = Magics
    # =========================================================================

    def __str__(self):
        return f"ScriptVr3 ({bool(self.enabled)}): R{self.r} C{self.c}"
