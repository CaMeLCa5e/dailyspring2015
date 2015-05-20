#! /usr/bin/env python 
# -*- coding: utf-8 -*- 

import sqlite as lite
import sys 

cars = (
	(1, 'Ford', 19000)
	(2, 'VW', 18000)
	(3, 'Bently', 87989)
	(4, 'Hummer', 198232)
)

con = lite.connect('test.db')

with con: 

	cur = con.cursor()

	cur.execute("DROP TABLE IF EXISTS Cars")
	cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
	cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)