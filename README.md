# ASL-Tools

<p align="center"><img src="resources/images/logo-big.png?raw=true" alt="Logo"></p>

## What's the ASL?

The __ASL 5000&trade;__ is a breathing simulator capable of simulating a wide range of patients, produced by __IngMar Medical&copy;__.
It is mainly used for educational purpose, developing products and testing ventilators. Check the IngMar Medical [website](https://www.ingmarmed.com/product/asl-5000-breathing-simulator/) for more information.

## What's the purpose of this tool?

The ASL 5000 comes with a software to manage the simulator.
As the ASL 5000 can simulate very complex patients, the software has a lot of tabs, settings and it takes quite a long time to create the desired scripts.

**&rArr; The goal of this tool is to create a friendly interface with the most used parameters.**

With the ASL 5000 software, and this tool, 3 different kind of simulations can be developed:
- a single simulation file (`vr3`): the simulation will run indefinitely, until the user ends it;
- a script: runs a bunch of `vr3` with an explicit amount of cycles for each simulation file;
- a dashboard: 25 predefined `vr3` that can be easily launched.

# Installation

This toolbox is written using [Python3](https://www.python.org/downloads/).

Initializing the environment:
```cmd
ASL-Tools> pip install virtualenv
ASL-Tools> virtualenv venv
ASL-Tools> venv/Scripts/activate
```

Loading the packages:
```cmd
ASL-Tools> pip install -r requirements.txt
```

# Usage

Launch ASL-Tools:
```cmd
python main.py
```

If you want to "compile" this tool, you can use [PyInstaller](https://www.pyinstaller.org) on `ASL-Tools.spec`:
```cmd
ASL-Tools> pip install PyInstaller
ASL-Tools> pyinstaller ASL-Tools.spec
```

# Creating an installer

The installer is created using [NSIS](https://nsis.sourceforge.io/Download), so it should be installed and added in Windows `PATH` variable.
To create the installer, you can use the following command:
```cmd
ASL-Tools> installer\install.bat
```

This script will:
- compile the Qt ressources;
- compile the tool to `target\ASL-Tools`;
- create the installer using NSIS;
