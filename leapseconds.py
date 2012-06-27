def get_utc_leap_seconds():
	f = open(tai-utc.dat, "r") 
	text = f.read() 
	
	import re 
	for r in text: 
		if re.search('.001' , r): 
			print r  
	