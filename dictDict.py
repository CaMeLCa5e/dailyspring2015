dod = {'a': {'ia': 1, 'ib':2},
		'b':{'ia': 3, 'ib':4},
		'c':{'ia': 5, 'ib': 6} }

for key in dod: 
	print key 
	for ikey in dod[key]: 
		print '  ', ikey, '=', dod[key][ikey]
	

