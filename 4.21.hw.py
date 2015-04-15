"""Reading from file ex2.txt, create a dictionary where the key is the user id and the value
is the second field in the line (a 2-digit or 3-digit integer). Sort the dictionary by value,
using a standard dict "sort by value" method.
Expected output 

axe99 142
jk43 23
jab44 27
ap172 33
jb23 48"""

import os
files = os.listdir('/Users/j/GitHub/dailyspring2015') # replace with your directory path
sorted_files = sorted(files, key=by_filesize, reverse=True)


ap172,33,212-583-1173
jab44,27,212-581-4342
axe99,142,212-582-5959
jk43,23,201-285-2927
jb23,48,212-227-2271)


print ex2

