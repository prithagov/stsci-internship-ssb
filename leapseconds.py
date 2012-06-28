import re 



ins = open ('tai-utc.dat' , 'r')
array = [ ]

for line in ins: 
	array.append(line) 

with open ('tai-utc.dat') as myfile: 
	head = [myfile.next() for x in xrange (1)] 
	print tuple (head)

	
	
	