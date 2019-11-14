import sys

from PySide2.QtCore import QFile
from PySide2.QtWidgets import QApplication

import src.common.resources  # Register resources
from src.config import Paths
from src.frames.controller import MainWindow


class Application(QApplication):
    """
    Application for the ASL Toolbox
    """

    def __init__(self, argv:list):
        QApplication.__init__(self, argv)
        # Load configs and styles
        self.load_configs()
        self.load_style()
        # Create the mainwindow
        self.window = MainWindow()

    def load_style(self):
        """
        The style is a css-like file
        """

        file = QFile(":/styles/style.qss")
        file.open(QFile.ReadOnly)
        style = file.readAll()
        style = style.data().decode()
        file.close()
        self.setStyleSheet(style)

    def load_configs(self):
        """
        Initialize the configs
        """

        Paths.initialize("resources/config/paths.json")

    def run(self):
        """
        Main method to run the application

        Returns:
            int: exit code
        """

        self.window.show()
        return self.exec_()


if __name__ == '__main__':
    with open("ASL-Tools.traceback.log", "w") as log:
        sys.stderr = log
        app = Application(sys.argv)
        exit_code = app.run()
        sys.exit(exit_code)
