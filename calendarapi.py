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

# def makeICS(eventList, name):
#     calendar = Calendar()
#     for event in eventList:
#         calendar.add_component(event)
#     calendar.add('prodid', "Carnegie Calendar")
#     calendar.add('version', '2.0')

#     f = open("generatedcals/" + name + ".ics",'wb+')

#     f.write(calendar.to_ical())
#     f.close()

# Used in the renderer to make a nice "January 7, 2020" text from the datetime object
def dateconvert(str):
    timezoneoffset = 0
    try:
        str = str.replace(hour=str.hour-timezoneoffset)
    except:
        pass
    return str.strftime("%-I:%M %p, %B %-d, %Y")
app.jinja_env.globals.update(dateconvert=dateconvert)

def getAllEvents():
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
            "start_time": time.mktime(thing.get('DTSTART').dt.timetuple()), 
            "end_time": time.mktime(thing.get('DTEND').dt.timetuple()), 
            "url": thing.get('URL')
        } 
        for thing in newCal if len(thing.get("DESCRIPTION").strip()) >= 1] # This requirement kicks out a lot of events, but they're events that need to be kicked out

        # Sort eventList by date so it displays properly
    try:
        curTime = time.mktime(time.localtime())
        eventList = [x for x in sorted(eventList, key=lambda event:event["start_time"]) if x["start_time"] > curTime]
    except:
        print("sort by date failed", time.localtime())
    return eventList

def shallow_copy(obj):
    res = {}
    for key in obj:
        res[key] = obj[key]
    return res

def filter_by_search_str (eventList, search_str):
    res = []
    terms = [x.strip().lower() for x in search_str.split(" ")]
    for event in eventList:
        matchval = 0
        for term in terms:
            for field in event.values():
                if (field is not None) and (term in str(field).lower()): matchval += str(field).lower().count(term)
        if (matchval == 0): continue
        event["matchval"] = matchval
        res.append(event)
    try:
        res.sort(key=lambda event: event["matchval"], reverse=True) #sort is stable
    except:
        print("sort by matchval failed")
    for event in res:
        event.pop("matchval", None)
    return res

def filter_by_start_time(eventList, start):
    try:
        start = float(start)
    except: 
        print("Invalid type")
        return eventList
    res = [x for x in eventList if x ["start_time"] >= start]
    return res

def filter_by_end_time(eventList, end):
    try:
        end = float(end)
    except:
        print("Invalid type")
        return eventList
    res = [x for x in eventList if x ["end_time"] <= end]
    return res

def filter_by_pagination(eventList, page_num, page_capacity):
    try:
        page_num = int(page_num)
        page_capacity = int(page_capacity)
    except:
        print("Invalid type")
        return eventList
    if (page_capacity <= 0 or page_num <= 0): return eventList
    res = []
    i = (page_num - 1)*page_capacity
    while (i < len(eventList) and i < page_num*page_capacity):
        res.append(eventList[i])
        i += 1
    return res

@app.route("/", methods=['GET'])
def index():
    return jsonify(getAllEvents())


@app.route("/search", methods=['GET'])
def search():
    search_str = request.args.get('search_str')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    page_num = request.args.get('page_num')
    page_capacity = request.args.get('page_capacity')
    events = getAllEvents()
    empty = []
    if (search_str != ""): 
        events = filter_by_search_str(events, search_str)
    if (start_time != ""): 
        events = filter_by_start_time(events, start_time)
    if (end_time != ""): 
        events = filter_by_end_time(events, end_time)
    if (page_num != "") and (page_capacity != ""): 
        events = filter_by_pagination(events, page_num, page_capacity)
    return jsonify(events)
    
###### FETCH DATA ######

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