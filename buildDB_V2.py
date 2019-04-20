####################################################################################
#######################  -----  SI 660 // WINTER 2019-----  ########################
############  -----  Mandy Shen, Rahul Bonnerjee, Tammy Nguyen  -----  #############
######################  -----  DATABASE DEVELOPMENT  -----  ########################
####################################################################################

### --- INFO -----------------------------------------------------------------------

### Creating User & Event databases
	## Creating tables in database
		## Populating tables in database


####################################################################################
########################### ---------- SETUP ---------- ############################
####################################################################################

### --- IMPORTING MODULES ----------------------------------------------------------

import sqlite3


####################################################################################
########################### ---------- USERS ---------- ############################
####################################################################################

DBNAME = 'communaltable.db'


### --- CREATING DATABASE ----------------------------------------------------------

def create_DB():

	## Connect to Database
	try:
		conn = sqlite3.connect(DBNAME)

	except Error as e:
		print(e)

	cur = conn.cursor()


	### -- USERS TABLE -- ###
	## Drop table if exists
	stmt = """
		DROP TABLE IF EXISTS 'users';
	"""

	cur.execute(stmt)

	## Create table
	stmt = """
		CREATE TABLE 'users' (
		'users_id' INTEGER PRIMARY KEY AUTOINCREMENT,
		'firstname' TEXT,
		'lastname' TEXT,
		'email' TEXT,
		'diet' TEXT,
		'allergy1' TEXT,
		'allergy2' TEXT,
		'allergy3' TEXT
		);
	"""
	cur.execute(stmt)
	conn.commit()


	### -- EVENT TABLE -- ###
	## Drop table if exists
	stmt = """
		DROP TABLE IF EXISTS 'events';
	"""

	cur.execute(stmt)

	## Create table
	stmt = """
		CREATE TABLE 'events' (
		'events_id' INTEGER PRIMARY KEY AUTOINCREMENT,
		'address1' TEXT,
		'address2' TEXT,
		'city' TEXT,
		'state' TEXT,
		'zipcode' INTEGER,
		'diet' TEXT,
		'ingredient1' TEXT,
		'ingredient2' TEXT,
		'ingredient3' TEXT,
		'description' TEXT,
		'allergy1' TEXT,
		'allergy2' TEXT,
		'allergy3' TEXT,
		'donation1' TEXT,
		'donation2' TEXT,
		'user_id' INTEGER,
		'seats' INTEGER,
		'mealTime' DATETIME,
		'name' TEXT,
		'longitude' TEXT,
		'latitude' TEXT
		);
	"""
	cur.execute(stmt)
	conn.commit()


	## Close Database Connection
	conn.close()


### --- POPULATING DATABASE --------------------------------------------------------

def populate_DB():

	## CONNECT TO DATABASE

	try:
		conn = sqlite3.connect(DBNAME)

	except Error as e:
		print(e)

	cur = conn.cursor()


	### --- USERS TABLE --- ###

	users_test = [("Rahul", "Bonnerjee", "rahb@umich.edu", None, None, None, None), ("Mandy", "Shen", "mxshen@umich.edu", "Vegetarian", None, None, None), ("Tammy", "Nguyen", "nguyents@umich.edu",  "Vegan", "Peanuts", None, None), ("Eric", "Gilbert", "eegg@umich.edu", None, "Eggs", "Peanuts", None), ("Kentaro", "Toyama", "toyama@umich.edu", None, None, None, None)]

	for each in users_test:
		data = (None, each[0], each[1], each[2], each[3], each[4], each[5], each[6])
		stmt = """
			INSERT INTO users
			VALUES (?, ?, ?, ?, ?, ?, ?, ?)
		"""

		cur.execute(stmt, data)

	conn.commit()


	### --- EVENTS TABLE --- ###

	event1 = [("777 N University Ave", None, "Ann Arbor", "MI", 48104, "Vegan", "Tofu", "Carrots", "Cucumbers", "Lemongrass Tofu Banh Mi with Salad Rolls", None, None, None, "Pie", "Beer", 1, 2, "2019-04-29 18:00:00", "Banh Mi First, Pie Competition Later.", None, None)]

	event2 = [("333 Maynard St", "5th Floor", "Ann Arbor", "MI", 48104, "Vegetarian", "Pasta", "Tomatoes", "Asparagus", "Burst Cherry Tomato Pasta with Roasted Asparagus", "Eggs", "Peanuts", None, "White Wine", "Side Dish", 2, 4, "2019-04-29 20:00:00", "Vegetarian Pasta and Board Game Night!", None, None)]

	event3 = [("333 Maynard St", "5th Floor", "Ann Arbor", "MI", 48104, None, "BBQ Spicy Pork", "Salad", "Kimchi", "Korean BBQ Spicy Pork with Rice and Side Dishes", None, None, None, "Dessert", "$5", 3, 3, "2019-04-30 19:30:00", "Korean BBQ and Movie Night!", None, None)]

	events = event1 + event2 + event3

	for each in events:
		data = (None, each[0], each[1], each[2], each[3], each[4], each[5], each[6], each[7], each[8], each[9], each[10], each[11], each[12], each[13], each[14], each[15], each[16], each[17], each[18], each[19], each[20])
		stmt = """
			INSERT INTO events
			VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
		"""

		cur.execute(stmt, data)

	conn.commit()

	## Close Database Connection
	conn.close()


####################################################################################
######################## ---------- RUNNING DATA ---------- ########################
####################################################################################
	
## Create Database
create_DB()

## Populate Database
populate_DB()