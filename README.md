﻿[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/itsAiham/dice_game/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/itsAiham/dice_game/?branch=master) [![Code Coverage](https://scrutinizer-ci.com/g/itsAiham/dice_game/badges/coverage.png?b=master)](https://scrutinizer-ci.com/g/itsAiham/dice_game/?branch=master) [![Build Status](https://scrutinizer-ci.com/g/itsAiham/dice_game/badges/build.png?b=master)](https://scrutinizer-ci.com/g/itsAiham/dice_game/build-status/master) [![Code Intelligence Status](https://scrutinizer-ci.com/g/itsAiham/dice_game/badges/code-intelligence.svg?b=master)](https://scrutinizer-ci.com/code-intelligence) [![Documentation Status](https://readthedocs.org/projects/dice-game/badge/?version=latest)](https://dice-game.readthedocs.io/en/latest/?badge=latest)

<br>

# Welcome in Dice Game!

<br>
Bellow are steps and setups you need to follow all features.

The basic goal of the project, is to reach clean, bugs free code.

Game has been developed using python OOP. The way to approach clean code with no (unaware dimensions) has been reach by writing unittest for classes used in project.

<br>

## Setup you need

I am expecting you to have _make_ installed

Have _Make_ on your environment (in case you want to enter short command lines)

```bash
www.chocolatey.org/packages/make
```

Check pip by running:

on mac:

```bash
pip3 --version
```

on win:

```bash
pip --version
```

and finally

To be able to try all features, it is preferred to create Virtual Environment.

<br>

## Make

To get advance of using make easily:

- Open Makefile

  - On Windows:

    - comment line 4 and uncommnet line 5

  - On Mac:
    - comment line 5 and uncommnet line 4

## Create venv

Navigate into repo
if you are a windows user, use always **python** insteade of **python3**

_.venv_ is the name of the VE you are going to create

```bash
make venv
```

To activate it VE in mac:

```bash
. .venv/bin/activate
```

To activate it on windows:

```bash
. .venv/Scripts/activate
```

To deactivate it on both operating system:

```bash
deactivate
```

Notice that if you are a windows user, use _GIT-bash_.

If you want to avoid creating VE. You may use command line mentioned in section bellow.

<br>

## Download requirements

After activating enter the following command:

```bash
make install
```

check libs list

```bash
pip3 list
```

If the list does not have more that three lines.
Then your installation faild.

You need to upgrade your pip using the following command

```bash
pip3 install pip --upgrade
```

**_pip if you are on windows_**

## Now, let gets start

### Run the game:

```bash
python main.py
```

Notice that you enter another terminal, and you would not exit it unless you enter **q** or other exit commands.

You can always press ? or help to get the introductions within game terminal.

### Testing:

After you are done with the game, let us trying tests some code.

Enter:

To run unittest and get the report about testing.

```bash
make coverage
```

To get a visual report about which lines have been covered and which not.

```bash
make html
```

A new folder is created **htmlcov**.
You find the reports in it

Run flake8, code cleaner.

```bash
make flake8
```

Run code analysis.

```bash
make pylint
```

Run both tests.

```bash
make test
```

### UML

Create uml for whole the package.

```bash
make pyreverse
```

Follow doc/ where you can find separate subfolders, each include UMLs

### Documentation:

[You can read the Documentation from here](https://dice-game.readthedocs.io)

Also, you can create the documentation locally, navigate to dice_game/docs/ and enter

```bash
make html
```

And by now, the documentation for the project has been created
to open it:

```bash
cd _build/html
```

you need to open **index.html**

If you are on windows:

```bash
start index.html
```

mac:

```bash
open index.html
```

## Manualy comman lines

If you do not have choco

Inside dice_game folder:

To test all module within the pachage:

```bash
coverage  run -m unittest discover . “test_*.py”
```

Create report AFTER running tests:

```bash
coverage report -m
```

Create HTML report:

```bash
coverage html
```

Run flake8:

```bash
 flake8
```

To run pylint on all file:

```bash
pylint *.py
```
