# CommunalTable, an web-application that connects you to your local community through food.

## A project developed for SI 660: Experimental Social Computing Systems

Communal Table is built with Python using a Flask framework that connects to a SQL database.

In order to run this project locally:
First, git clone this repository on your local system.  Navigate to this project folder in the command line.

Then, activate the virtual environment env1 in your console using the following command : `source env1/bin/activate`

Next, pip install the packages listed on the requirements.txt file with the command: `pip install -r requirements.txt`

Optional -  While there is already a DB in this directory, you can clean it by running the command: `python buildDB_V2.py`

Once your virtual environment is activated & packages are installed within that env1, you can then run a local server with the command: `python app.py`

Finally, a CommunaleTable prototype will be available for you to try at the address http://127.0.0.1:5000/
