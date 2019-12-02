@echo off

echo 1. Change to installer directory
set INITDIR=%CD%
cd %~dp0

echo 2. Compile resources
..\venv\Scripts\pyside2-rcc.exe ..\resources\resources.qrc -o ..\src\common\resources.py

echo 3. Compile the Python project
..\venv\Scripts\pyinstaller ASL-Tools.spec 2>nul

echo 4. Create the installer
makensis installer.nsi 1>nul

echo 5. Change to initial directory
cd %INITDIR%
