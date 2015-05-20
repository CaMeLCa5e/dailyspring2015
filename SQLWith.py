#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sqlite3 as lite
import sys 

con = lite.connection('test.db')

with con: 

	cur = con.cursor()
	cur.execute('SELECT SQLITE_VERSION()')

	data = cur.fetchone()

	print "SQLite version: %s" % data

	