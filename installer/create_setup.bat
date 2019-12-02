@echo off

echo 1. Change to installer directory
set INITDIR=%CD%
cd %~dp0

echo Compile resources
..\venv\Scripts\pyside2-rcc.exe ..\resources\resources.qrc -o ..\src\common\resources.py

echo Compile the Python project
..\venv\Scripts\pyinstaller ASL-Tools.spec 2>nul

echo Create the installer
makensis installer.nsi 1>nul

echo 5. Change to initial directory
cd %INITDIR%
