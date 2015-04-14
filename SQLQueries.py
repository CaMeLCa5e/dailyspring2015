class Person(models.Model):
	first_name = models.CharField()
	last_name = models.CharField()
	birth_date = models.DateField()

for p in Person.objects.raw('SELECT * FROM myapp_person'):
	print p 

Person.objects.raw('SELECT id, first_name, last_name, birth_date FROM myapp_person')

Person.objects.raw('SELECT last_name, birth_date, first_name, id FROM myapp_person')


Person.objects.raw('SELECT first AS first_name, last AS last_name, bd AS birth_date, pk AS id, FROM some_other_table')

name_map = {'first': 'first_name', 'last': 'last_name', 'bd': 'birth_date', 'pk': 'id'}
person.objects.raw(SELECT * FROM some_other_table, translations=name_map)


first_person = Person.objects.raw('SELECT * FROM myapp_person')[0]

first_person = Person.objects.raw('SELECT * FROM myapp_person LIMIT 1')[0]

people = Person.objects.raw('SELECT id, first_name FROM myapp_person')

for p in Person.objects.raw('SELECT id, first_name FROM myapp_person'):
	print (p.first_name
		   p.last_name)	






















