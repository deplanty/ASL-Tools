# ASL-Tools

## What's the ASL?

The __ASL 5000&trade;__ is a breathing simulator capable of simulating a wide range of patients, produced by __IngMar Medical&copy;__.
It is mainly used for educational purpose, developing products and testing ventilators. Check the IngMar Medical [website](https://www.ingmarmed.com/product/asl-5000-breathing-simulator/) for more information.

## What's the purpose of this tool?

The ASL 5000 comes with a software to manage the simulator.
As the ASL 5000 can simulate very complex patients, the software has a lot of tabs, settings and it takes quite a long time to create the desired scripts.

&rArr; **The goal of this tool is to create a friendly interface with the most used parameters.**

With the ASL 5000 software, and this tool, 3 different kind of simulations can be developed:
- a single simulation file (`vr3`): the simulation will run indefinitely, until the user ends it;
- a script: runs a bunch of `vr3` with an explicit amount of cycles for each simulation file;
- a dashboard: 25 predefined `vr3` that can be easily launched;

# Installation

This toolbox is written using [Python3](https://www.python.org/downloads/).

Initializing the environment:
```cmd
pip install virtualenv
virtualenv venv
```

Loading the packages:
```cmd
pip install -r requirements.txt
```

# Usage

Launch ASL-Tools:
```cmd
python main.py
```

If you want to "compile" this tool, you can use [PyInstaller](https://www.pyinstaller.org).
