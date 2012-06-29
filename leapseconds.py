import re 


with open ('tai-utc.dat') as myfile: 
	head = myfile.readline()
	#print head
	head = re.sub('\D','',head) 
	#print head
	matchobj= re.search ( '2437300.5',head )

if matchobj: 
	print tuple (matchobj.group())
