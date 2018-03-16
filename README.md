# CMPUT 302 Library Visualizer Hi-Fidelity Prototype

This might be good. This could be bad. All I know is that it'll be pretty rough, and not 100% perfect.

# To Install and Run on the command line:

- [Install Python 3.6.4](https://www.python.org/downloads/)
  
**Choose a directory and clone our repository:**

	$ git clone _insert repo here_
  
**Install virtual environment and create a virtualenv instance:**
	
	$ pip3 install virtualenv	
	$ python3 -m venv myvenv 
	(python -m venv myvenv in Windows)

**Activate virtual environment and install requirements:**

	$ source myvenv/bin/activate
	($ source myvenv/Scripts/activate on Windows)
	$ pip3 install -r requirements.txt
	
**Migrate the database to get model schema:**

	$ cd teaching_assignment/
	$ python manage.py migrate

**In virtual environment, start the project:**

	$ python3 manage.py runserver
	(On Windows: $ python manage.py runserver )
  
**In web browser, go to:**
  
	$ localhost:8000/login 
  
**To deactivate virtual environment:**

	$ deactivate