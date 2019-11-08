import sys

from fbs_runtime.application_context.PySide2 import ApplicationContext

from frames.controller import MainWindow


class Application(ApplicationContext):
    def __init__(self, *args, **kwargs):
        ApplicationContext.__init__(self, *args, **kwargs)

        self.window = MainWindow(self)

    def run(self):
        self.window.show()
        return self.app.exec_()


if __name__ == '__main__':
    app = Application()
    exit_code = app.run()
    sys.exit(exit_code)
