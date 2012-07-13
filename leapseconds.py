import re 
import urllib2
import sys

_DECIMAL_RE = '\d+\.?\d*'

_LEAPSECONDS_RE= re.compile('.+ =JD (%s)  TAI-UTC=\s+(%s)\s+S \+ \(MJD - (%s)\) X (%s)'% ((_DECIMAL_RE,)*4))
	

_leap_seconds_cache = None 

response = urllib2.urlopen('http://maia.usno.navy.mil/ser7/tai-utc.dat') 



def get_utc_leap_seconds():
	global _leap_seconds_cache
	
	try: 
	 _leap_seconds_cache = [_LEAPSECONDS_RE.match(line).groups() for line in response]
	 return _leap_seconds_cache
	except IOError: 
		print 'The program was unable to retrieve the most recent file, the information given is as accurate as possible.'
		if _leap_seconds_cache is not None: 
			return _leap_seconds_cache 
	
		else:
			with open('tai-utc.dat') as source:		
				_leap_seconds_cache = [_LEAPSECONDS_RE.match(text).groups() for text in source]
				return _leap_seconds_cache	     
	
if __name__ == '__main__':
	print get_utc_leap_seconds()
		
	
	
