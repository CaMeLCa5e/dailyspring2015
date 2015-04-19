# Set operations 

a = set(['a', 'b', 'c'])
b = set(['b', 'c', 'd'])
print a.difference(b)		#set(['a'])
print a.union(b)			#set(['a', 'b', 'c', 'd'])
print a.intersection(b)     #set(['b', 'c'])

a = ['hello', 'there', 'harry']
print [ var.upper() for var in a if var.startswith('h') ]



# lambda *****

# names = ['Joe Wilson']