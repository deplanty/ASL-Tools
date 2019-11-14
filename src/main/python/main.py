import sys

from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtCore import (
    QByteArray,
    QFile
)

import resources
from config import Paths
from frames.controller import MainWindow


class Application(ApplicationContext):
    def __init__(self, *args, **kwargs):
        ApplicationContext.__init__(self, *args, **kwargs)

        Paths.initialize("src/main/resources/base/config/paths.json")

        file = QFile(":/styles/style.qss")
        file.open(QFile.ReadOnly)
        style = file.readAll()
        style = style.data().decode()
        file.close()
        self.app.setStyleSheet(style)
        self.window = MainWindow()

    def run(self):
        self.window.show()
        return self.app.exec_()


if __name__ == '__main__':
    app = Application()
    exit_code = app.run()
    sys.exit(exit_code)
