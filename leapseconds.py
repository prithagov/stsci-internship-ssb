import re 


_DECIMAL_RE = '\d+\.?\d*'

_LEAPSECONDS_RE= re.compile('.+ =JD (%s)  TAI-UTC=\s+(%s)\s+S \+ \(MJD - (%s)\) X (%s)'% ((_DECIMAL_RE,)*4))
	

_leap_seconds_cache = None 

def get_utc_leap_seconds():
	global _leap_seconds_cache
	with open('tai-utc.dat') as source:		
		_leap_seconds_cache = [_LEAPSECONDS_RE.match(text).groups() for text in source]
	if _leap_seconds_cache == None: 
		return get_utc_leap_seconds()
	else:
		return _leap_seconds_cache
if __name__ == '__main__':
	print get_utc_leap_seconds()
		
	
	
