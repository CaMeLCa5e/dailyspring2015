

line = '19260716    0.52   -0.03   -0.58   0.009'
line2 = '19260811   -0.56    0.22    0.38   0.010'
line.split()
line2.split()


# print sorted(line, key=len)
print line 
print line.split()

mylist = [5,6,4,3,3,4,5,7,87,8,6,5,5,5,5,4,4,4,4,5,5]
# mylist.sort()
print mylist
sorted_list = sorted(mylist)

# print mylist
print sorted_list

namelist = ['dd', 'ff', 'a' , 'A', 'akjh']

print sorted(namelist)

# print sorted(namelist, key=len)
# passing function len as an argument 
# exaluating based on result 


print len(namelist)

print sorted(namelist, key=str.lower)
print sorted(namelist, key=len)
# # the values dont change, they are just evaluated differently. 


scores = {'jeb': 123, 'mithc': 98}
# sortedkeys = sorted(scores, key=scores.get)
# print sortedkeys
# # get takes one key and returns one value the sorted keys are evaluated by the key. 


# mydict = scores

# for key in sorted(mydict, key = mydict.get):
# 	print key, mydict[key]



# def print_hello():
# 	print "hello"

# print_hello()


def print_greeting(greeting, person):
	full_greeting = greeting + ", " +person 
	print full_greeting

print_greeting('hello', 'python')



def return_greeting(greeting, person):
	full_greeting = greeting + ", " +person 
	return full_greeting

msg = return_greeting('hello', 'parrot')
print msg


# def by_lastname(name):
# 	fname, lname = name.split()
# 	return lname 

# names = ['bill cunningham']
# print separated(names, key=by_lastname)




