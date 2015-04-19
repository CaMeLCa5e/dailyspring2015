myints = [0,1,5,7,8,9,444,5,356]
myposints = []
for el in myints: 
	if el > 0: 
		myposints.append(el)

print myposints


myposints2 = [el for el in myints if  el > 0 ]

print myposints2