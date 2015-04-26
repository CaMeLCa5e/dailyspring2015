import re

# str = 'hello'

# if re.search(r'hello', str):
# 	print 'hello'

# for filename in os.listdir(r'/path/to/directory'):
# 	if re.search(r'\.txt$', filename): 
# 		print filename

input7 = '13333234'
input2 = '12378'

if re.search(r'^\d\d\d\d$', input7):
	print 'match'