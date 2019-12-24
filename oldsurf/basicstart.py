from bs4 import BeautifulSoup
from requests import *

def getSCS():
    # Returns a list of lists that have structure
    # [DayTime, Event Category, Title,
    url = """https://www.cs.cmu.edu/calendar?page=0
    """

    eventList = []

    for page in range(3):
        r = get(url[:-2]+str(page))
        soup = BeautifulSoup(r.text,'xml')

        text = soup.get_text()
        text = text[text.rfind("Subscribe to RSS feed")+21 : text.rfind("Pages")].strip()
        eventList.extend(text.split("\n\n\n\n\n\n\n\n"))

    for i in range(len(eventList)):
        eventList[i] = [x.strip() for x in eventList[i].split("\n")]
        try:
            eventList[i].remove("")
            eventList[i].remove("")
        except:
            pass
        while len(eventList[i]) > 4:
            eventList[i][2] = eventList[i][2] + " " + eventList[i].pop(3)
    eventList = [x for x in eventList if len(x) > 3]



    return eventList

events = getSCS()