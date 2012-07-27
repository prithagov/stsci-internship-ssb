import re 
import urllib2
import sys
from datetime import datetime 

_DECIMAL_RE = '\d+\.?\d*'

_LEAPSECONDS_RE= re.compile('.+ =JD (%s)  TAI-UTC=\s+(%s)\s+S \+ \(MJD - (%s)\) X (%s)'% ((_DECIMAL_RE,)*4))


_leap_seconds_cache = None 

now = datetime.now() # this figures out the date for today, use this to figure out the difference between this date and the last time _leap_seconds_cache was updated

response = urllib2.urlopen('http://maia.usno.navy.mil/ser7/tai-utc.dat') 

#last_leapsec= datetime(_leap_seconds_cache[-1]) , for inside the () figure out how to get the program to read the date in the last line of the file 

#td = now-last_leapsec , for figuring out whether or not the file needs to be updated


def get_utc_leap_seconds():
	global _leap_seconds_cache
	# if td >= 182.621 , once you figure out how to have the program understand reading the julian date in _leap_seconds_cache[-1]
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






	
	
