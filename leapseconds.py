import re 

lines = open ('tai-utc.dat', 'r').readlines() 
total = " " 
for line in lines: 
	total +=line

	matchobj= re.findall('[\d]+\.?\d+',total)
	
if matchobj:
	print tuple(matchobj) 
	
