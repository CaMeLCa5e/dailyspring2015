list = ['3' '444' 'fffsdfsdf' '3']
blankIter = ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',]
# s = ','.join(list)
# s = s.strip(',')
# print s



delimiter = ' '
print delimiter.join(list)


newIter = delimiter.join(list)


D = dict(zip(list, blankIter))

print D