Welcome in Dice Game!
=====================



This project has been created by students in Kristianstad university in Sweden.

Bellow are steps and setups you need to follow all features.




The basic goal of the project, is to reach clean, bugs free code.

Game has been developed using python OOP. The way to approach clean code with no (unaware dimensions) has been reach by writing unittest for classes used in project.







Setup you need
--------------


I am expecting you to have _Choco_ installed.
Or you may follow the following path for installation.

www.chocolatey.org/install



Have _Make_ on your environment

www.chocolatey.org/packages/make



and finally


To be able to try all features, it is preferred to create Virtual Environment.


On Repo directory, enter the equivalent command line according to your operating system:


If you are using Mac or Linux, python3 is used to approach python operation. Meanwhile,  python on windows.



To create venv
--------------


**python3 -m venv env**   Where _env_ the name of it and you may change it.


	To activate it write:	". env/bin/activate"

        To deactivate it:	        "deactivate"



**Python -m venv env**     If you are on windows
       

       To activate it write:	". env/bin/activate"

       To deactivate it:	        "deactivate"



Notice that if you are a windows user, I am expecting you to use _GIT-bash_.


If you want to avoid creating VE. You may use comman line mentioned in section bellow.



Download requirements
---------------------


After activating enter the following command:



**Python -m pip install -r requirements.txt**  (python3 if you are on mac)






  
  
Now, let gets start
--------------------



  
#### Run the game:


Navigate to dice_game file, using **cd dice_file**

And simply enter ‘python main.py’ 


Notice that you enter another terminal, and you want to be able to exit it unless you follow the approach.

You can always press ? or help to get the introduction.



  
#### Testing:

After you are done with the game, let us trying tests some code.


Enter:


**make coverage**, to run unittest and get the report about testing.


**make html**,  to get a visual report about which lines have been covered and which not.


**make flake8**, to run code cleaner.


**make pylint**, to run code analysis.


**make test**, to run both tests.


  
#### UML:


**make pyreverse**, to create uml for whoe packages.


**make game**, to create UML for game class


If you want to get UML for another class. Press the following command separately.


**pyreverse class.py**


**pyreverse -o png -p pyreverse class.py**


where class is the name of wanted class.

  

#### Documentation:


Two ways to create docs for projects.


1: Navigate to repo/docs and enter **make html**

```bash
cd _build/html
``` 

If you are on windows:

```bash
start index.html
```

mac:

```bash
open index.html
```


2: To get docs within dice_game folder:


```bash
make pdoc
```



You will get another folder ‘doc’ and you are able to find all documentation inside it.


  
  






Manualy comman lines
--------------------
  
Inside dice_game folder:

To test all module within the pachage:

```bash
coverage  run -m unittest discover . “test_*.py” 
```


( coverage report -m )		Create report AFTER ran testing.

( coverage html )			Create HTML report

( flake8 )  		To run flake8

( pylint *.py )       To run pylint on all files that have py extension.


Feel free to COPY exactly what inside brackets


#### UML:


"pyreverse *.py "


"pyreverse -o png -p pyreverse *.py  " 	To generate UML for whole package.
 







#### Reference:


Some parts of code taken from:


https://gitlab.com/mikael-roos/sustainable-programming-exercise

https://stackoverflow.com/

