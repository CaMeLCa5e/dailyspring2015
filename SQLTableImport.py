#! usr/bin/env python 
# -*- coding: utf-8 -*-

import sqlite3 as lite 
import sys 

def readData():

	f = open('cars.sql', 'r')

	with f: 
		data = f.read()
		return data

con = lite.connect(':memory:')

with con: 

	cur = con.cursor()
	cur.execute('SELECT * FROM Cars')

	col_names = [cn[0] for cn in cur.description]

	rows = cur.fetchall()

	print "%s %-10s %s" % (col_names[0], col_names[1], col_names[2])

	for row in rows:
		print "%2s %-10s %s" % row

