import re 


def get_utc_leap_seconds():
	with open('tai-utc.dat') as source:		
		decimal_re= '\d+\.?\d*'
		
		mylist = [ ]
		
		
		for text in source:
			
			items = ( re.match('.+ =JD (%s)  TAI-UTC=\s+(%s)\s+S \+ \(MJD - (%s)\) X (%s)'%((decimal_re,)*4),text).groups())
			mylist.append(items) 
	return mylist
			
		
if __name__ == '__main__':
	print get_utc_leap_seconds()
		
	
	
	