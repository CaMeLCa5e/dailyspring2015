def test_var_args(f_arg, *argv):
	print "first normal arg:", f_arg
	for arg in argv:
		print "another arg through *argv :", arg 

test_var_args('yasoob', 'eggs', 'spam', 'test')

def greet_me(**kwargs):
	if kwargs is not None:
		for key, value in kwargs.iteritems():
			print "%s == %s" %(key,value)
print greet_me(name="Jimmy")
