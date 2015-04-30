#! usr/bin/python

filename = "popularnames.txt"
newNameList = []
count = 0
with open(filename) as myfh:
    listOfLines = myfh.readlines()
    newstring = filename.rstrip()

for line in open('popularnames.txt'):
    line = line.rstrip()
    line_words = line.split()
    newNameList.append(line_words[1])
    newNameList.append(line_words[2])

print newNameList

for name in newNameList:
	count += 1
	print (count, name) 


	# if name: 

# print count
# emptyList = emptyList.split()



