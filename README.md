#Welcome in Dice Game!
=====================


This project has been created by students in Kristianstad university in Sweden.

Bellow are steps, and setups you need to follow all features.




The basic goal of the project, is to reach clean, bugs free code.

Game has been developed using python OOP. The way to approach clean code with no (unaware dimensions) has been reach by writing unittest for classes used in project. 






Setup you need
--------------


I am expecting you to have _Choco_ installed.
Or you may follow the following path for installation.

www.chocolatey.org/install


Have _Make_ on your environment

linux - What are makefiles - make install - Stack Overflow



and finally


To be able to try all feature, it is preferred to create Virtual Environment.


In Repo directory, enter the equivalent command line according to your operating system:


If you are using Mac or Linux, python3 is used to approach python operation. Meanwhile,  python on windows.


To create venv
--------------


'python3 -m venv env'   Which is env the name of it and you may change it.


	To activate it write:	‘. .venv(bin/activate’	

        To deactivate it:	        ‘deactivate



'Python -m venv env'     If you are on windows
       

       To activate it write:	‘. .venv(bin/activate’

       To deactivate it:	        ‘deactivate



Notice that if you are a windows user, I am expecting you to use GIT-bash.




Download requirements
---------------------


After activating enter the following command:

‘Python -m pip install -r requirements.txt’  (python3 if you are on mac)




If you want to avoid any installation. You may find a section bellow to reach fetchers manually.








Now, let gets start
--------------------




##Run the game:


Navigate to dice_game file, using ‘cd dice_file’

And simply enter ‘python main.py’ 


Notice that you enter another terminal, and you want to be able to exit it unless you follow the approach.

You can always press ? or help to get the introduction.




##Testing:

After you are done with the game, let us trying tests some code.


Enter:


**make coverage**, to run unittest and get the report about testing.


**make html'**,  to get a visual report about which lines have been covered and which not.


**make flake8**, to run code cleaner.


**make pylint**, to run code analysis.


**make test**, to run both test.



##UML:


**make pyreverse**, to create uml for whoe packages.


**make game**, to create UML for game class


If you want to get UML for another class. Press the following command separately.


**pyreverse class.py**


**pyreverse -o png -p pyreverse class.py**


where class is the name of wanted class.



##Documentation:


To get the class, method documentations

Press:  **make pdoc**


You will get another folder ‘doc’ and you are able to find all documentation inside it.










##Manualy comman lines:


Inside dice_game folder:


**coverage  run -m unittest discover . “test_*py” ***		Test all modules within the package.

**coverage report -m **		Create report AFTER ran testing.

**cverage html** 			Create HTML report

**flake8**  		To run flake8

**pylint *.py ***       To run pylint on all files that have py extension.



##UML:


**pyreverse *.py	***


**pyreverse -o png -p pyreverse *.py  ***		To generate UML for whole package.





##Who are we:


Students in Kristianstad’s university


www.hkr.se











##Reference:


Some parts of code taken from:


https://gitlab.com/mikael-roos/sustainable-programming-exercise

https://stackoverflow.com/
