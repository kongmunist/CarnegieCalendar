from flask import Flask, render_template, url_for, render_template_string, Markup, redirect, request
from flask_flatpages import FlatPages, pygmented_markdown
from flask_bootstrap import Bootstrap
from flask_frozen import Freezer

import sys
from icalendar import *

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG

g = open('static/example.ics', 'rb')
cal = Calendar.from_ical(g.read())
eventTypeRef = type(cal.walk()[-1])

def dateconvert(str):
    timezoneoffset = 0
    try:
        str = str.replace(hour=str.hour-timezoneoffset)
    except:
        pass
    return str.strftime("%-I:%M %p, %B %d, %Y")
app.jinja_env.globals.update(dateconvert=dateconvert)

@app.route("/", methods=['GET', 'POST'])
def index():
    eventList = []
    header = ""

    if request.method == 'POST':
        print(request.form['search'])
        searchterm = request.form['search']

        g = open("../calendars/current.ics", 'rb')
        cal = Calendar.from_ical(g.read())
        cal = cal.walk()[1:]

        newCal = []
        for t in cal:
            if searchterm.lower() in t.get("SUMMARY").lower() or searchterm.lower() in t.get(
                    "DESCRIPTION").lower():
                newCal.append(t)

        eventList = [
            [thing.get('SUMMARY'), thing.get('DESCRIPTION'),
             thing.get('LOCATION'),
             thing.get('DTSTART'), thing.get('DTEND'), thing.get('URL')] for
            thing
            in newCal if len(thing.get("DESCRIPTION")) > 1]
        try:
            eventList.sort(key=lambda x: x[3].dt)
        except:
            pass

        header = str(len(eventList)) + " events containing \'" + searchterm + "\'"

    return render_template('main.html', events = eventList, header = header)#eventList[:100])


@app.route('/<path:searchterm>/')
def page(searchterm):
    print(searchterm)
    print(searchterm)

    g = open("static/current.ics", 'rb')
    cal = Calendar.from_ical(g.read())
    cal = cal.walk()[1:]
    newCal = []
    for t in cal:
        if searchterm in t.get("SUMMARY") or searchterm in t.get("DESCRIPTION"):
            newCal.append(t)

    eventList = [
        [thing.get('SUMMARY'), thing.get('DESCRIPTION'), thing.get('LOCATION'),
         thing.get('DTSTART'), thing.get('DTEND'), thing.get('URL')] for thing
        in newCal]

    return render_template('main.html', resultsfound = len(eventList), events=eventList, defaultTerm = searchterm)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        # Builds the website into a static site and runs "firebase deploy" to update the site
        freezer.freeze()
    else:
        app.run(port=8000)
