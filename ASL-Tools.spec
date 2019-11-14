# -*- mode: python -*-

import os
import shutil

import PyInstaller.config

# Create and set working directories
os.makedirs("./target/PyInstaller", exist_ok=True)
PyInstaller.config.CONF["workpath"] = "./target/PyInstaller"
PyInstaller.config.CONF["distpath"] = "./target/"
PyInstaller.config.CONF["noconfirm"] = True

# Specs
block_cipher = None

a = Analysis(
    ['./main.py'],
    pathex=['./'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher
)
a.datas += Tree("./resources", prefix="resources")

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)

exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name='ASL-Tools',
    debug=False,
    strip=False,
    upx=True,
    console=True,
    icon="./resources/images/icon.ico"
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='ASL-Tools'
)

# Clear remaining PyInstaller folders
shutil.rmtree("./build/")
shutil.rmtree("./dist")
