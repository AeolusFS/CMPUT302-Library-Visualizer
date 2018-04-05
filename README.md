# CMPUT 302 Library Visualizer Hi-Fidelity Prototype


# To Install and Run on the command line:

- [Install Python 3.6.4](https://www.python.org/downloads/)
  
**Choose a directory and clone our repository:**

	$ git clone https://github.com/skaefer143/CMPUT302-Library-Visualizer


**Install virtual environment and create a virtualenv instance:**
	
	$ pip3 install virtualenv	
	$ python3 -m venv myvenv 
	(python -m venv myvenv in Windows)

**Activate virtual environment and install requirements:**

	On Linux:
	$ source myvenv/bin/activate
	On Windows:
	$ cd myvenv/Scripts/ 
	$ activate.bat

	Make sure your command line has a (myvenv) prefixed to your input line
	Then:
	Navigate back to main folder, and type
	$ pip3 install -r requirements.txt
	
**Migrate the database to get model schema: (not required, do it anyways)**

	$ cd library_visualizer_app/
	$ python manage.py migrate

**In virtual environment, start the project:**

	$ python3 manage.py runserver
	(On Windows: $ python manage.py runserver )
  
**In web browser, go to:**
  
	$ http://127.0.0.1:8000/
  
**To deactivate virtual environment:**

	$ deactivate