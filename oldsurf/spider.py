from bs4 import BeautifulSoup
from requests import *
import isEventRegex as ier
import fileio
import wget

import ixml
import time

# url = "https://www.cmu.edu/"





url = "https://www.cs.cmu.edu/calendar"









# url = "https://www.cs.cmu.edu/"







# hello = urllib.request.urlretrieve(url)
# url = "https://engineering.cmu.edu/"
# url = "https://www.cmu.edu/cfa/"
# url = "https://www.cmu.edu/dietrich/"
# url = "https://www.heinz.cmu.edu/"
# url = "https://www.heinz.cmu.edu/events"
# url = "https://www.cmu.edu/mcs/news-events/index.html"
# url = "https://thebridge.cmu.edu/events"
# url = "file:///Users/andykong/PycharmProjects/surf/exSite.html"

# print(hello)

def isEvent(text):
    text = text.replace("\n", " ")
    if ier.findDate(text) != None and ier.findTime(text) != None and ier.findLoc(text) != None:
        return True
    else:
        return False


def download(url,levels):
    # get initial page

    siteLinks = [{url}]
    for depth in range(levels):
        siteLinks.append(set())

        for siteToVisit in siteLinks[depth]:


            processedLink = siteToVisit.strip("/")

            if processedLink.find("http") == -1:
                processedLink = "http://" + processedLink

            rootLink = siteToVisit.strip("/")
            rootLink = rootLink.replace("https://","")
            rootLink = rootLink.replace("http://","")
            if rootLink.find("/") != -1:
                rootLink = rootLink[:rootLink.find("/")]
            rootLink = "https://" + rootLink

            # rootLink = ""
            # print(url)
            try:
                response = get(url)
            except:
                pass
            soup = BeautifulSoup(response.text, "lxml")

            # soup = BeautifulSoup(url,"lxml")

            for script in soup(["script", "style", "aside"]):
                script.decompose()

            for link in soup.find_all("a"):  #soup.find_all("a"):
                linkHref = link.get("href")
                # If the link is youtube, flickr, or a pdf, it breaks and doesn't add
                if linkHref == None or linkHref.find(".pdf") != -1 or \
                        linkHref.find("youtube") != -1 or linkHref.find("facebook") != -1 or linkHref.find("flickr") != -1 or linkHref.find("pgid") != -1\
                        or linkHref.find("..") != -1 or linkHref.find("login") != -1 or linkHref.find("2016") != -1 or linkHref.find("2017") != -1:
                    continue


                # if link is already in our siteLinks, it breaks and doesn't add
                # for i in range(depth):
                #     if link in siteLinks[i]:
                #         break
                if linkHref in siteLinks[depth]:
                    break

                if linkHref.find("www") == -1:
                    linkHref = rootLink + "/" + linkHref#[linkHref.find("www"):]
                siteLinks[depth+1].add(linkHref)
                print(linkHref)
                # if linkHref == "https://www.cmu.edutest.html":
                #     break
    testOnWebsite(siteLinks)



def testOnWebsite(siteLinks):
    print("start testing")
    # for layer in siteLinks:
    #     print(len(layer))

    data = []
    for i in range(5):
        data.append([])

    for s in siteLinks:
        for linq in s:
            # if linq.find("staff") != -1 or linq.find("twitter") != -1 or linq.find("instagram") != -1:
            #     continue
            print(linq)

            try:
                response = get(linq)
            except:
                pass
            # print(linq)

            soup = BeautifulSoup(response.text,"lxml")
            # soup = BeautifulSoup(url, "lxml")

            # print(soup.prettify())
            for script in soup(["script", "style","aside"]):
                script.decompose()

            txt = soup.get_text()
            txt = " ".join(txt.split())

            if isEvent(txt):
                print(txt)
                print("Time: ", ier.findTime(txt))
                print("Date: ", ier.findDate(txt))
                print("Location: ", ier.findLoc(txt))
                try:
                    print(txt[:txt.find("|")])
                except:
                    pass


                data[0].append(ier.findDate(txt))
                times = ier.findTime(txt)
                data[1].append(times[0])
                try:
                    data[2].append(times[1])
                except:
                    data[2].append("")
                data[3].append(ier.findLoc(txt))
                if len(txt[:txt.find("|")]) < 50:
                    data[4].append(txt[:txt.find("|")])
                else:
                    try:
                        data[4].append(txt[txt.find(ier.findLoc(txt)):txt.find(ier.findLoc(txt))+100])
                    except:
                        try:
                            for key in ier.findKey(txt[:5000]):
                                data[4].append(key)
                                break
                        except:
                            data[4].append("NA")

                # f.write(" ".join(txt.split()))
                # try:
                #     print(txt[:txt.find("|")])
                # except:
                #     pass
                # relevant = txt[(txt.find(ier.findDate(txt))-200):(txt.find(ier.findDate(txt))+200)]
                # print(ier.findKey(relevant))
                # print(relevant)
                # print(txt[(txt.find(ier.findDate(txt))-200):(txt.find(ier.findDate(txt))+200)])

                # print(" ".join((txt[txt.find(ier.findTime(txt))-200:txt.find(ier.findTime(txt))+200]).split()))


    fileio.writeToFile(data[0],data[1],data[2],data[3],data[4])


download(url,1)