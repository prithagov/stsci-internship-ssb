import re 
import urllib2
import sys
from datetime import datetime 

_DECIMAL_RE = '\d+\.?\d*'

_LEAPSECONDS_RE= re.compile('.+ =JD (%s)  TAI-UTC=\s+(%s)\s+S \+ \(MJD - (%s)\) X (%s)'% ((_DECIMAL_RE,)*4))


_leap_seconds_cache = None 

now = datetime.now() # this figures out the date for today, use this to figure out the difference between this date and the last time _leap_seconds_cache was updated

response = urllib2.urlopen('http://maia.usno.navy.mil/ser7/tai-utc.dat') 

td = now-last_leapsec 
# for all the variable from Jd to modf , i added these because maybe they would help with caluculating but I'm really stuck in trying to figure this out. 
Jd = (year,month,day,hour,minute,second)
int year -=1 
int month += 12 
int day
int hour
int minute 
MJD0= = datetime(_leap_seconds_cache[-1]) 
modf = math.modf
def get_utc_leap_seconds():
	global _leap_seconds_cache
	 if td >= 182.621 
	 	#int(modf(year/400)[1]-intint(modf(year/100)[1])+\ I feel like I should be using this somewhere in my code to help read julian time but I just can't figure out where exactly I am supposed to be placing it. It also confuses me quite a bit , I found some of this from reources that show how to reda julian in python. but I have a feeling this is very off from where I am trying to get to. I was just pluggin things in and experamenting. 
        #int(modf(year/4)[1])  
        # basically I want it to be able to figure out if td is >= 182.621  and have run everything below everything below this comment according to the last time the file was updated.  
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






	
	
