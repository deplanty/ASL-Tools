import sys

from PySide2.QtCore import QFile
from PySide2.QtWidgets import QApplication

import src.common.resources
from src.config import Paths
from src.frames.controller import MainWindow


class Application(QApplication):
    def __init__(self, argv:list):
        QApplication.__init__(self, argv)

        Paths.initialize("resources/config/paths.json")
        self.load_style()
        self.window = MainWindow()

    def load_style(self):
        file = QFile(":/styles/style.qss")
        file.open(QFile.ReadOnly)
        style = file.readAll()
        style = style.data().decode()
        file.close()
        self.setStyleSheet(style)

    def run(self):
        self.window.show()
        return self.exec_()


if __name__ == '__main__':
    app = Application(sys.argv)
    exit_code = app.run()
    sys.exit(exit_code)
