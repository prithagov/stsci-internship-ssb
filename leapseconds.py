import re 


with open ('tai-utc.dat') as myfile: 
	head = myfile.readline()
	print head
	head = re.sub( '\D', '',head) 
	print head
	