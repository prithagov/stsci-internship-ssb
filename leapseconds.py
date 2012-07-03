import re 
import itertools as it

def get_utc_leap_seconds():
	with open('tai-utc.dat') as source:		
		decimal_re= '\d+\.?\d*'
		
		for text in source:
			
			
			
			new=re.match('.+ =JD (%s)  TAI-UTC=\s+(%s)\s+S \+ \(MJD - (%s)\) X (%s)'%((decimal_re,)*4),text).groups()
			
			return [new]
		
if __name__ == '__main__':
	get_utc_leap_seconds()
	