#! /usr/bin/env python 
# -*- coding: utf-8 -*- 

import sqlite as lite
import sys 

con = lite.connect('test.db')

with con: 

	cur = con.cursor()
	cur.execute("CREATE TABLE(id INT, Name TEXT, Price INT)")
	cur.execute("INSERT INTO Cars VALUES(1, 'Audi', 54323)")
	cur.execute("INSERT INTO Cars VALUES(2,'Mercedes', 55432)")
	cur.execute("INSERT INTO Cars VALUES(3,'Ford' 22998)")
	cur.execute("INSERT INTO Cars VALUES(4,'Volvo' 24334)")
	