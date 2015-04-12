mylist = [4,5,6,7,8,5,3,5,6,7,8,9,0]

# mylist.sort()

sorted_list = sorted(mylist)

print mylist
print sorted_list

namelist = ['dd', 'ff', 'a' , 'A', 'akjh']

print sorted(namelist)

print sorted(namelist, key=len)
# passing function len as an argument 
# exaluating based on result 


print len(namelist)

print sorted(namelist, key=str.lower)
print sorted(namelist, key=len)
# the values dont change, they are just evaluated differently. 


scores = {'jeb': 123, 'mithc': 98}
sortedkeys = sorted(scores, key=scores.get)
print sortedkeys
# get takes one key and returns one value the sorted keys are evaluated by the key. 


mydict = scores

for key in sorted(mydict, key = mydict.get):
	print key, mydict[key]



def print_hello():
	print "hello"

print_hello()


def print_greeting(greeting, person):
	full_greeting = greeting + ", " +person 
	print full_greeting

print_greeting('hello', 'python')



def return_greeting(greeting, person):
	full_greeting = greeting + ", " +person 
	return full_greeting

msg = return_greeting('hello', 'parrot')
print msg














