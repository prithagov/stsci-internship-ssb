

import re 


with open('tai-utc.dat') as source:		
	
	for text in source:
		total = " " 
		total+= text
		matchobj = re.findall('\d+\.?\d*',total)
		
		print tuple (matchobj) [2:6]
		
	