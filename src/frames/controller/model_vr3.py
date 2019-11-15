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

from src.common import io
from src.common import qt_utils
import src.common.qt_utils.popup
from src.config import Paths
from src.common.objects import DashVr3
from src.frames.ui import Ui_ModelVr3


class ModelVr3(QWidget):
    def __init__(self, parent:QWidget=None):
        QWidget.__init__(self, parent)

        self.ui = Ui_ModelVr3(self)
