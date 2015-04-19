



# lot = mydict.items()
# ptint lot 

# def by_tup_val(arg):
# 	return arg[1]

# rlot = sorted(lot, key=by_tup_val)
# rlot = sorted(lot, key=by_tup_val, reverse=Tru)


# rlot = sorted(lot, key=lambda arg: arg[1], rev.True)
import operator 

mydict = {1: 'a', 2: 'b'}

for key, val in mydict.items():
	print key, '=', val

mydict_items = mydict.items()
mydict_items.sort(key=operator.itemgetter(1))

for key, val in mydict_items:
	print "{0} = {1}".format(key, val)

