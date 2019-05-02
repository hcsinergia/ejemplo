# -*- coding: utf-8 -*-

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","123456","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data


# execute SQL query using execute() method.
cursor.execute("SELECT * FROM PRODUCTO")

data = cursor.fetchone()

print data
# disconnect from server
db.close()