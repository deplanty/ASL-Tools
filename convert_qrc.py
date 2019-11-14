import os


dir_this = os.path.dirname(__file__)
rcc = os.path.join(dir_this, "venv\\Scripts\\pyside2-rcc.exe")
qrc = os.path.join(dir_this, "resources\\resources.qrc")
py = os.path.join(dir_this, "resources.py")
cmd = f"{rcc} {qrc} -o {py}"
os.system(cmd)
