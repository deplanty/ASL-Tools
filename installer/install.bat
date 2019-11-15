@echo off

echo Going to root directory
cd %~dp0..

echo Compile resources
venv\Scripts\pyside2-rcc.exe resources\resources.qrc -o src\common\resources.py

echo Compile the Python project
venv\Scripts\pyinstaller ASL-Tools.spec

echo Create the installer
makensis installer\installer.nsi

setlocal
:PROMPT
set /P DO_INSTALL=Do you want to launch the installer (y/n) [n]?
if /I "%DO_INSTALL%" neq "y" goto END
target\installer\Setup_ASL-Tools.exe
:END
endlocal
