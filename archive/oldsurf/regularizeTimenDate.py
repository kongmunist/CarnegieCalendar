from ics import Calendar, Event
import datetime, calendar
import isEventRegex as eRegex

MONTHS = []
MONTHS_ABBR = []

for i in range(1, 13):
    MONTHS.append(calendar.month_name[i].lower())

for i in range(1, 13):
    MONTHS_ABBR.append(calendar.month_abbr[i].lower())


def convertDate(date):
    now = datetime.datetime.now()
    if ('/' in date):
        month = date.split('/')[0]
        day = date.split('/')[1]
    elif ('-' in date):
        month = date.split('-')[0]
        day = date.split('-')[1]
    else:
        for elem in date.split():
            if elem.lower() in MONTHS:
                month = elem
            elif 1 <= int(elem) <= 31:
                day = elem
    if int(day) < 10:
        day = '0' + day
    if month.lower() in MONTHS or month.lower() in MONTHS_ABBR:
        month = str(MONTHS.index(month.lower()) + 1)
    if int(month) < 10:
        month = "0" + month



    date = str(now.year) + month + day
    return date


def convertTime(time):
    hour = time.split(':')[0]
    hour = hour.replace("pm", "").replace("am", "")
    if "pm" in time.lower():
        hour = hour.replace("pm", '')
        hour = str(int(hour) + 12)
    elif "am" in time.lower():
        time = time.replace("am", "")
        hour = str(int(hour))
    if len(hour) < 2:
        hour = '0' + hour

    try:
        if int(hour) > 12:
            hour = str(int(hour) % 10)
    except:
        pass
    try:
        minute = time.split(':')[1]
    except:
        minute = "00"
    if len(minute) < 2:
        minute = '0' + minute

    return hour + ':' + minute


def convertICS(contents):
    c = Calendar()
    for text in contents:
        event = Event()
        start = convertDate(eRegex.findDate(event)) + " " + convertTime(
            eRegex.findTime(event)[0]) + ":00"
        event.begin = start
        event.name = start.replace(":", "")
        c.events.append(event)
        now = datetime.datetime.now()
        with open(str(
                now.year + now.month + now.day + now.hour + now.minute) + '.ics',
                  'w') as f:
            f.writelines(c)