import re 

_DECIMAL_RE = '\d+\.?\d*'
_LEAPSECONDS_RE= re.compile('.+ =JD (%s)  TAI-UTC=\s+(%s)\s+S \+ \(MJD - (%s)\) X (%s)'% ((_DECIMAL_RE,)*4))


def get_utc_leap_seconds():
	
	with open('tai-utc.dat') as source:		
		
		return [_LEAPSECONDS_RE.match(text).groups() for text in source]		

if __name__ == '__main__':
	print get_utc_leap_seconds()
		
	
	
	