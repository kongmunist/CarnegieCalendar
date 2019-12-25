from flask import Flask, render_template, url_for, render_template_string, Markup, redirect, request, send_file, session


import re
import sys
import os
import time
from icalendar import *

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = os.urandom(16)

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
# export FLASK_ENV=development

forbidden_searches = ['pizza', 'lunch', 'food', 'free', 'swag', 'merch', 'dinner'] # Maybe use these if you commercialize

# To get instance of event type, we use example.ics
g = open('static/example.ics', 'rb')
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
    # print(calendar)

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


@app.route("/", methods=['GET', 'POST'])
def index():
    eventList = []
    header = ""

    g = open("../calendars/current.ics", 'rb')
    cal = Calendar.from_ical(g.read())
    cal = cal.walk()[1:]

    if len(cal) < 5:
        g = open("../calendars/currentBackup.ics", 'rb')
        cal = Calendar.from_ical(g.read())
        cal = cal.walk()[1:]


    # When user submits the form with a search,
    if request.method == 'POST':
        # Tell us what they searched for and Record search terms
        orig_search_form = request.form['search']
        if orig_search_form.strip() == "":
            Everything = True
            open("data/searchhistory.txt", 'a+').write("everything, ")
            print("search for everything")
        else:
            Everything = False
            open("data/searchhistory.txt", 'a+').write(orig_search_form + ", ")
            print("search for", orig_search_form)

        # Make list out of search terms
        searchterm = [x.strip().lower() for x in orig_search_form.split(",")]
        print(searchterm)

        # Filter for separate search terms
        newCal = []
        uniques = set()
        for t in cal:
            for term in searchterm:
                if t.get("SUMMARY") not in uniques and (term.lower() in t.get("SUMMARY").lower() or term.lower() in t.get(
                    "DESCRIPTION").lower()):
                    newCal.append(t)
                    uniques.add(t.get("SUMMARY"))

        # Generate an eventList for the main.html template to fill in
        eventList = [
            [thing.get('SUMMARY'), remove_tags(thing.get('DESCRIPTION')),
             thing.get('LOCATION'),
             thing.get('DTSTART'), thing.get('DTEND'), thing.get('URL')] for
            thing in newCal if len(thing.get("DESCRIPTION").strip()) >= 1]

        # Sort eventList by date so it displays properly
        try:
            eventList = [x for x in sorted(eventList,
                             key=lambda event: time.mktime(event[3].dt.timetuple()))]
        except:
            print("sort by date failed")

        # Generate search header
        header = str(len(eventList)) + " events containing \'" + orig_search_form + "\'"

        # Create naming convention for file downloads
        if Everything:
            filename = "everything"
        else:
            filename = "".join(searchterm)
        makeICS(newCal, filename)
        session['search'] = filename

    else:
        newCal = []
        uniques = set()
        for t in cal:
            if t.get("SUMMARY") not in uniques:
                uniques.add(t.get("SUMMARY"))
                newCal.append(t)

        # Generate an eventList for the main.html template to fill in
        eventList = [
            [thing.get('SUMMARY'), remove_tags(thing.get('DESCRIPTION')),
             thing.get('LOCATION'),
             thing.get('DTSTART'), thing.get('DTEND'), thing.get('URL')] for
            thing in newCal if len(thing.get("DESCRIPTION").strip()) >= 1]

        # Sort eventList by date so it displays properly
        try:
            eventList = [x for x in sorted(eventList,
                                           key=lambda event: time.mktime(
                                               event[3].dt.timetuple()))]
        except:
            print("sort by date failed")

        # Generate search header
        header = str(len(eventList)) + " events happening soon..."
        session['search'] = "everything"


    return render_template('main.html', events = eventList, header = header)


@app.route("/exportcalendar")
def downloadCalendar():
    open("data/downloadhistory.txt", 'a+').write(session['search'] + ", ")

    try:
        print('downloading', session['search'])
        return send_file("generatedcals/" + session['search'] + '.ics', as_attachment=True, attachment_filename='CarnegieCalendar.ics')
    except Exception as e:
        print("download failed")
        return str(e)

@app.route("/about")
def about_page():
    return render_template('about.html')



@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response



# @app.route('/<path:searchterm>/')
# def page(searchterm):
#     print(searchterm)
#
#     g = open("static/current.ics", 'rb')
#     cal = Calendar.from_ical(g.read())
#     cal = cal.walk()[1:]
#     newCal = []
#     for t in cal:
#         if searchterm in t.get("SUMMARY") or searchterm in t.get("DESCRIPTION"):
#             newCal.append(t)
#
#     eventList = [
#         [thing.get('SUMMARY'), thing.get('DESCRIPTION'), thing.get('LOCATION'),
#          thing.get('DTSTART'), thing.get('DTEND'), thing.get('URL')] for thing
#         in newCal]
#     return render_template('main.html', resultsfound = len(eventList), events=eventList, defaultTerm = searchterm)


if __name__ == "__main__":
    app.run(port=8000)
