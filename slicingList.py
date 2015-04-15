myList = ['a', 'b', 'c', 'd']

# print myList[1:3]

print myList
newList = myList[1:3]

print newList

lines = open('ex1.txt').readlines()
print lines

# 4
lines = open('ex1.txt').readlines()
lines = lines[3]
els = lines.split[':']
print els 
print els[-1]


# 5
lines = open('ex1.txt').readlines()
slice_lines = lines[0:3]
for line in slice_lines:
	line = line.rstrip()
	print line 

# 6 
lines = open('ex1.txt').readlines()
slice_lines = lines[1:]
print slice_lines



