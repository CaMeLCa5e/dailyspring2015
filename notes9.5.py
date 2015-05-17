import random 
class MyClass(object):
	def set_random(self):
		self.myrandval = random.randint(1,10)
	def print_value(self):
		if self.myrandval:
			print self.myrandval


a = MyClass()
print a.print_value()

print a.MyClass()


# self is the object 
# When you call a function, the function looks for instance in the attribute and the class.