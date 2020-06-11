import calendar, string

MONTHS = set()
DAYS = set()

for i in range(1, 13):
    MONTHS.add(calendar.month_name[i].lower())

for i in range(7):
    DAYS.add(calendar.day_abbr[i].lower())


def readFile(path):
    with open(path, "rt") as f:
        return f.read()


def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)


def getEvent(text):
    eventDay = []
    eventMonth = []
    eventDate = []
    eventTime = []
    eventLoc = []
    text = text.lower()
    #   get name, date, time, notes, loc etc.

    lines = set(tuple(text.splitlines()))
    for line in lines:
        words = line.split()
        for month in MONTHS:
            if month in line:
                eventMonth.append(month)
                for word in words:
                    try:
                        eventDate.append(int(word))
                    except:
                        pass

        for day in DAYS:
            if day in line:
                eventDay.append(day)
        for word in words:
            if ("am" in word) or ("pm" in word) or (":" in word):
                time = True
                for c in word.replace("am", "").replace("pm", "").replace(":",
                                                                          ""):
                    if not (c in string.digits):
                        time = False
                        break
                if time:
                    eventTime.append(word)

    eventSummary = (eventDay, eventMonth, eventDate, eventTime, eventLoc)
    # for var in eventSummary:
    #     if ((eventDay == set()) and (eventMonth == set())):
    #         eventSummary = None
    # for var in eventSummary:
    #     if var == []:
    #         return None

    print(eventSummary)
    if eventDate == [] or eventTime == []:
        return None
    return True


def isEvent(text):
    return getEvent(text) != None


def createCSV(path):
    contents = ""
    (eventDay, eventMonth, eventDate, eventTime, eventLoc) = getEvent(path)
    eventSummary = (eventDay, eventMonth, eventDate, eventTime, eventLoc)
    if isEvent(path):
        for i in range(len(eventDay)):
            for elem in eventSummary:
                try:
                    contents += elem[i] + ", "
                except:
                    contents += "n/a, "
            contents = contents[:-1]
            contents += "\n"
    return contents[:-1]


#       event -> txt or csv ->save that to object


def createISC(text):
    pass


