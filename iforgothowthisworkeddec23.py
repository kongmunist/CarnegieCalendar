from icalendar import *
import datetime
import pytz
import requests as r
import time
import re

g = open("calendars/current.ics", 'rb')
cal = Calendar.from_ical(g.read())
cal = cal.walk()[1:]

for e in cal:
    tmp = e['DTSTART'].dt
    print(type(tmp), time.mktime(tmp.timetuple()))

sortedEvents = [x for x in sorted(cal, key=lambda event: time.mktime(event['DTSTART'].dt.timetuple()))]