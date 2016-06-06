import sqlite3
conn = sqlite3.connect('../tutorial.db')
c = conn.cursor()

#for creating the table
def create_table() :
	c.execute('CREATE TABLE IF NOT EXISTS busDetails(BusNo TEXT, BusRoute TEXT, latitude REAL, longitude REAL,time TEXT)')

#filling the data to the table
def data_entry() :
	c.execute("INSERT INTO busDetails VALUES('401b','yalahanka to kengeri',12.236,14.36,'12:20')")
	conn.commit()


#reading the data from the database
def read_from_db() :
	c.execute('SELECT * FROM busDetails')
	#data = c.fetchall()
	result = "";
	for row in c.fetchall():
		result += row

		

# read_from_db()
# create_table()
# data_entry()
