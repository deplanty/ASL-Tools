from src.config import Paths


class Vr3:
    def __init__(self):
        self.c = int()
        self.r = int()
        self.br = int()
        self.i_pmus = int()
        self.i_pmus_inc = int()
        self.i_pmus_hld = int()
        self.i_pmus_rel = int()
        self.e_pmus = int()
        self.e_pmus_inc = int()
        self.e_pmus_hld = int()
        self.e_pmus_rel = int()
        self.crf = float()

    # =========================================================================
    # = Getter and setter
    # =========================================================================

    def from_dict(self, data:dict):
        """
        Load the data from a dictionnary

        Args:
            data (dict): the data
        """

        self.c = data["C"]
        self.r = data["R"]
        self.br = data["BR"]
        self.i_pmus = data["I_Pmus"]
        self.i_pmus_inc = data["I_increase"]
        self.i_pmus_hld = data["I_hold"]
        self.i_pmus_rel = data["I_release"]
        self.e_pmus = data["E_Pmus"]
        self.e_pmus_inc = data["E_increase"]
        self.e_pmus_hld = data["E_hold"]
        self.e_pmus_rel = data["E_release"]
        self.crf = data["CRF"]

    def to_dict(self):
        """
        Return the data as a dictionnary

        Returns:
            dict: the data
        """

        return {
            "C": self.c,
            "R": self.r,
            "BR": self.br,
            "I_Pmus": self.i_pmus,
            "I_increase": self.i_pmus_inc,
            "I_hold": self.i_pmus_hld,
            "I_release": self.i_pmus_rel,
            "E_Pmus": self.e_pmus,
            "E_increase": self.e_pmus_inc,
            "E_hold": self.e_pmus_hld,
            "E_release": self.e_pmus_rel,
            "CRF": self.crf
        }

    def export(self, path:str):
        """
        Export the vr3 at the given path

        Args:
            path (str): path to file
        """

        C = round(float(self.c)/2, 6)  # Compliance
        E = round(1000/C, 6)  # Elastance

        export = {
            "R_cst": float(self.r),
            "R_var": float(self.r),
            "C_cst": C,
            "C_var": C,
            "E_cst": E,
            "BR_cst": float(self.br),
            "BR_var": float(self.br),

            "I_Pmus_cst": float(self.i_pmus),
            "I_Pmus_var": float(self.i_pmus),
            "I_increase_cst": float(self.i_pmus_inc),
            "I_increase_var": float(self.i_pmus_inc),
            "I_hold_cst": float(self.i_pmus_hld),
            "I_hold_var": float(self.i_pmus_hld),
            "I_release_cst": float(self.i_pmus_rel),
            "I_release_var": float(self.i_pmus_rel),

            "E_Pmus_cst": float(self.e_pmus),
            "E_increase_cst": float(self.e_pmus_inc),
            "E_hold_cst": float(self.e_pmus_hld),
            "E_release_cst": float(self.e_pmus_rel),
            "CRF_cst": float(self.crf),

            "flag_timevar": 0,  # Constant
            "flag_extpmus": 0,  # No Pmus
            "extpmus_filename": "",  # No Pmus
            "extpmus_dirname": "",  # No Pmus
            "chest_model": 3  # Curved Pmus
        }

        with open(Paths.file("template_vr3")) as f:
            template = f.read()

        with open(path, "w") as f:
            f.write(template.format(**export))