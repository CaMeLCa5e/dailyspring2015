# # bindings

# # var_a = 5

# # del var_a

# # label is not the object

# var = 10 
# var2 = var
# print id(var)
# print id(var2)

# x = ['a','b','c']

# y = x

# print id(y)
# print id(x)

# y.append('e')
# print id(y)
# print id(x)

# print x
# print y

# xx = [['a','b','c'],['a','b','c']]
# print id(xx[0])
# print xx[0]

# l = 1
# print id(l)


# x = 5
# y = x 
# del x 
# print y


# w = 7
# myList = [1,2,3,4,5,w]

# del w 
# print myList





# def myfunc(var):
# 	print var 
# 	print "var: ", id(var)

# x = 10 
# print "x: ", id(x) 
# myfunc(x)
# var = 7
# print "x: ", id(x) 
# print myfunc(x)



def myfunc(var): 
	var.append(4)

x = [1,2,3]
myfunc(x)
print x

