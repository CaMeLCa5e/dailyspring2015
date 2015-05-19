#! usr/bin/python 
import MySQLdb

db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# cursor.execute("SELECT VERSION()")

# data = cursor.fetchone()

# print "Database version : %s" %data

# db.close 

sql = """CREATE TABLE EMPLOYEE (
			FIRST_NAME CHAR(20) NOT NULL,
			LAST_NALE CHAR(20),
			AGE INT,
			SEX CHAR(1)
			INCOME FLOAT )"""

cursor.execute(sql)

db.close()

