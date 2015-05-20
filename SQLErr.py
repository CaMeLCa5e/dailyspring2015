#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

try:
	con = lite.connect('test.db')

	cur = con.cursor()

	cur.executescript("""
		DROP TABLE IF EXISTS Cars;
		CREATE TABLE Cars(Id INT, Name TEXT, Price INT);
		INSERT INTO Cars VALUES(1, 'Ford', 34000)
		INSERT INTO Cars VALUES(2, 'Bently', 278999)
		""")

	con.commit()

except lite.Error, e:

	if con: 
		con.rollback()

	print "Error %s:" % e.args[0]
	sys.exit(1)

finally:

	if con: con.close()

	