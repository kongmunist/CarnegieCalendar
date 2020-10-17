from flask import Flask, render_template, url_for, render_template_string, Markup, redirect, request, send_file, session, jsonify


import re
import sys
from datetime import datetime
import os
import time
from icalendar import *
import atexit
import calendarfetch
from multiprocessing import Process

from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = os.urandom(16)

DEBUG = False
FLATPAGES_AUTO_RELOAD = DEBUG
# export FLASK_ENV=development

forbidden_searches = ['pizza', 'lunch', 'food', 'free', 'swag', 'merch', 'dinner'] # Maybe use these if you commercialize

# To get instance of event type, we use example.ics
g = open('example.ics', 'rb')
cal = Calendar.from_ical(g.read())
eventTypeRef = type(cal.walk()[-1])

TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(text):
    return TAG_RE.sub('', text)

def makeICS(eventList, name):
    calendar = Calendar()
    for event in eventList:
        calendar.add_component(event)
    calendar.add('prodid', "Carnegie Calendar")
    calendar.add('version', '2.0')

    f = open("generatedcals/" + name + ".ics",'wb+')

    f.write(calendar.to_ical())
    f.close()

# Used in the renderer to make a nice "January 7, 2020" text from the datetime object
def dateconvert(str):
    timezoneoffset = 0
    try:
        str = str.replace(hour=str.hour-timezoneoffset)
    except:
        pass
    return str.strftime("%-I:%M %p, %B %-d, %Y")
app.jinja_env.globals.update(dateconvert=dateconvert)


@app.route("/", methods=['GET'])
def index():
    eventList = []

    g = open("calendars/current.ics", 'rb')
    cal = Calendar.from_ical(g.read())
    cal = cal.walk()[1:]
    newCal = []

    uniques = set()
    for t in cal:
        # print(t.get("SUMMARY"), str(t.get("DTSTART").dt))
        try:
            if t.get("SUMMARY")+str(t.get("DTSTART").dt) not in uniques:
                uniques.add(t.get("SUMMARY")+str(t.get("DTSTART").dt))
                newCal.append(t)
        except:
            print("default page unique filter fail")
    # print(uniques)
        # Generate an eventList for the main.html template to fill in
    eventList = [
        {
            "summary": thing.get('SUMMARY'), 
            "description": remove_tags(thing.get('DESCRIPTION')),
            "location": thing.get('LOCATION'),
            "start_time": thing.get('DTSTART').dt, 
            "end_time": thing.get('DTEND').dt, 
            "url": thing.get('URL')
        } 
        for thing in newCal if len(thing.get("DESCRIPTION").strip()) >= 1] # This requirement kicks out a lot of events, but they're events that need to be kicked out

        # Sort eventList by date so it displays properly
    try:
        curTime = time.mktime(time.localtime())-43200
        eventList = [x for x in sorted(eventList,
                                       key=lambda event: time.mktime(
                                           event[3].dt.timetuple())) if time.mktime(
                                           x[3].dt.timetuple()) > curTime]
    except:
        print("sort by date failed", time.localtime())
    print(eventList[0])
    return jsonify(eventList)

def newDataAsync():
    pro = Process(
        target=calendarfetch.fetchCurrentCalendar,
        daemon=True
    )
    pro.start()

scheduler = BackgroundScheduler()
scheduler.add_job(func=newDataAsync, trigger="interval", seconds=3600)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    app.run(port=5050)


