Welcome in Dice Game!
=====================



This project has been created by students in Kristianstad university in Sweden.

Bellow are steps and setups you need to follow all features.




The basic goal of the project, is to reach clean, bugs free code.

Game has been developed using python OOP. The way to approach clean code with no (unaware dimensions) has been reach by writing unittest for classes used in project.







Setup you need
--------------


I am expecting you to have _make_ installed

Have _Make_ on your environment (in case you want to enter short comman lines)



```bash
www.chocolatey.org/packages/make
```


New version of pip, some features are not working with old one!

on mac:

```bash
pip3 install pip --upgrade
```

on win:
```bash
pip install pip --upgrade
```


and finally


To be able to try all features, it is preferred to create Virtual Environment.





Create venv
--------------

Navigate into repo
if you are a windows user, use always **python** insteade of **python3**


_env_ is the name of the VE you going to create

```bash
python3 -m venv env
```


To activate it write:	

```bash
. env/bin/activate
```



To activate it on windows:
```bash
. env/Scripts/activate
```
   

To deactivate it on both operating system:


```bash
deactivate
```




Notice that if you are a windows user, I am expecting you to use _GIT-bash_.


If you want to avoid creating VE. You may use comman line mentioned in section bellow.



Download requirements
---------------------


After activating enter the following command:




```bash
Python3 -m pip install -r requirements.txt
```

check that your pip list

```bash
pip3 list
```


If the list does not have more that three lines.
Then your installation faild.


You need to upgrade your pip using the following comman


```bash
pip3 install pip --upgrade
```
***pip  if you are on windows***

  
  
Now, let gets start
--------------------



  
### Run the game:


Navigate into dice_game the folder *where dice_gama a folder*, using **cd dice_file**

 
```bash
python3 main.py
```


Notice that you enter another terminal, and you would not exit it unless you enter **q** or other exit commands.

You can always press ? or help to get the introduction within game terminal.



  
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
You got ump with .png extension within dice_game folder.



To ganerate UML for only game class.


```bash
make game
```



If you want to ganerate an UML for another class. Enter the following:

**change class to the real name of class**


```bash
pyreverse class.py
```


```bash
pyreverse -o png -p pyreverse class.py
``` 





  

### Documentation:


Assume you are on repo directory
Navigate to dice_game/docs/ and enter

```bash
make html
```

And by now, the documentation for the project has created
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








Manualy comman lines
--------------------

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



### UML:


```bash
pyreverse *.py
``` 



To genetate UML for whole the pachage.

```bash
pyreverse -o png -p pyreverse *.py
```








### Reference:


Some parts of code taken from:

```bash
https://gitlab.com/mikael-roos/sustainable-programming-exercise
```


```bash
https://stackoverflow.com/
```
