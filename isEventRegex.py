import re, datetime
import azure
import regularizeTimenDate as reg

def findDate(contents):
    # regex1 = re.compile('(\d{1,2})?\s{1,3}(?:Jan(?:uary)?|\
    # Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|\
    # Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?)\s{1,3}(\d{1,2})?')

    regex1 = re.compile("(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?)(\s*\d{1,2})")
    regex2 = re.compile("(\d{1,2}\s*)(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?)")

    regex3 = re.compile("[0-1]?[0-9][/-][0-3]?[0-9]([/-][1-2]?[0-9]?[0-9][0-9])?(?!')")

    regex4 = re.compile("(today)?(tomorrow)?")


    dates = []
    dates.append(regex1.search(contents))
    dates.append(regex2.search(contents))
    dates.append(regex3.search(contents))


    now = datetime.datetime.now()
    contextual = regex4.search(contents)
    if contextual.group() != None:
        if contextual.group() == "today":
            dates.append(now.day + " " + now.month)

    dates = [x for x in dates if x is not None]
    # print(dates)
    # print(dates)
    if dates == []:
        return None
    else:
        try:
            return reg.convertDate(dates[0].group())
        except:
            return None



def findTime(contents):

    regex1 = re.compile("(\d{1,2}(:\d{1,2})?)(\s?(PM|AM|pm|am|p\.m\.|a\.m\.|P\.M\.|A\.M\.))")
    regex2 = re.compile("(\d{1,2}:\d{1,2})(\s?(PM|AM|pm|am|p\.m\.|a\.m\.|P\.M\.|A\.M\.)?)")

    times = []
    times.append(regex1.search(contents))
    times.append(regex2.search(contents))


    times = [x for x in times if x is not None]

    if times == []:
        return None
    elif len(times) == 2:
        return [reg.convertTime(times[0].group()),reg.convertTime(times[1].group()).strip()]
    else:
        return [reg.convertTime(times[0].group())]


def findLoc(contents):
    regexLoc1 = re.compile('(BH|CFA|CIC|CYH|DH|EDS|GES|GHC|GYM|HBH|HH|HL|IA|INI|MI|MM|NSH|OFF|PCA|PH|POS|PTC|REH|TEP|SEI|SH|CUC|WH|WEH|Baker (Hall)?|College of Fine Arts|Collaborative Innovation Center|Cyert( Hall)?|Doherty( Hall)?|(Elliot )?(Dunlap )?Smith Hall|Gesling( Stadium)?|Gates (and )?Hillman( Centers)?|Weigand( Gymnasium)?|Hamburg( Hall)|Hamerschlag( Hall)?|Hunt( Library)?|GSIA|4616 Henry( Street)?|Mellon Institute|Margaret Morrison( Carnegie Hall)?|Newell-Simon( Hall)?|Purnell( Center)?( for the Arts)?|Porter( Hall)?|Posner( Center)?|Pittsburgh Technology Center|Roberts( Engineering)?( Hall)?|Tepper( Quad)?|Software Engineering Institute|Scaife( Hall)?|(Cohon )University Center|Warner( Hall)?)\s?(([0-9A-Z]?[0-9]?[0-9][0-9]))')
    regexLoc2 = re.compile('(Peter|Wright|McKenna|Rangos|Connan|McConomy)')
    loc = []

    loc.append(regexLoc1.search(contents))
    loc.append(regexLoc2.search(contents))

    loc = [x for x in loc if x is not None]


    if loc == []:
        return None
    else:
        # print(loc)
        return loc[0].group()

def findKey(contents):
    return azure.keyWordsML(contents)


def readFile(path):
    with open(path, "rt") as f:
        return f.read()