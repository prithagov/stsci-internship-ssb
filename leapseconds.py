import re 


with open('tai-utc.dat') as f:		

	for lines in f:
		total = " "
		
	total +=lines
	matchobj= re.findall('\d+\.?\d*', total)
	
	
if matchobj: 

	print tuple (matchobj) 
