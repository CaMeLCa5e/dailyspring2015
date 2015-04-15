# lol = [
# 	['']
# 	['']
# 	['']
# 	['']
# ]

myList = []

iList = [1,2,3,4]
iList2 = [5,6,7,8]

myList.append(iList)
myList.append(iList2)

print myList.append(iList)

print myList[1:-1]
print myList[1][-1]
# list number one.  then last item of list one. 


# mylist [1] [0]

sum = 0 
for iList in myList:
	sum = sum + iList[0]
print sum
# this is 5 + 1 

print myList

for iList in myList:
	for el in iList:
		print el

dod = {
	'db13': {
			'fname': 'Joe',
			'lname': 'wilson',
			'tel': '9898989',
			},

	'db14': {
			'fname': 'Joe',
			'lname': 'wilson',
			'tel': '9898989',
			}
}

print dod ['db14'] ['fname']
print dod ['db13'] ['tel']


# print dod [0] [0] this will not run because there are no value numbers in a dict. 

# tabular data organized in dicts.  used for look up facility. 

# doi = 'db11': {
# 			'fname': 'Joe',
# 			'lname': 'wilson',
# 			'tel': '9898989',
# 			},

for key, val in dod.items():
	print key, val 



# for key, val in doi.items():
# 	print key, val 


# for key in date_values:
# 	print 'values_for ', key
# 	for ikey in date_values[key]:
# 		print ikey, '=', date_values[key][ikey]
# 	print 

filename = 'FF.txt'
# THIS IS THE HOMEWORK
# for line in open(filename)[6:-3]
# 	date, mktrf, smb, rf, hml, = line.split()

# 	id = {}
# 	id['mktrf'] = mktrf
# 	id['smb'] = smb
# 	id['hml'] = hml
# 	id['rf'] = rf

# 	od[date] = id

id = {}
id['a'] = ['hh']
id['1984'] = ['gg']
id['1964'] = ['ee']
id['1987'] = ['ll']

print id['1987']

id['1987'].append('3.4')
# print id.append('a')
print id['1987']







































