from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from requests import *

url = "https://lists.andrew.cmu.edu/mailman/listinfo"
subfile = "assets/subscribedLinks.txt"

def getLists(url):
    site = get(url)
    soup = BeautifulSoup(site.text,"lxml")
    c = []
    for link in soup.find_all("a"):
        tmp = link.get("href")
        if tmp.find("lists") != -1:
            c.append(tmp)
    return c

def imp(file):
    c = set()
    with open(file,"r") as f:
        ftext = f.read().split(",")
        for thin in ftext:
            c.add(thin.strip())
    return c


def subscribe(url,file):
    email = "cmuhoneypot+1@gmail.com"
    interestedPerson = webdriver.Chrome("assets/chromedriver")
    siteLinks = getLists(url)[1:]
    siteLinks = siteLinks[::-1]

    existingLinks = imp(file)


    print("# of mailing lists online: ",len(siteLinks))
    print("# of mailing lists cached: ",len(existingLinks))
    with open(file,"a") as mem:
        for ml in siteLinks:
            if ml not in existingLinks:
                print(ml)
                interestedPerson.get(ml)
                emailBox = interestedPerson.find_element_by_xpath("/html/body/p/table[4]/tbody/tr[7]/td/ul/table/tbody/tr/td[1]/form/table/tbody/tr[1]/td[2]/input")
                emailBox.send_keys(email)
                time.sleep(.1)
                try:
                    interestedPerson.find_element_by_xpath("/html/body/p/table[4]/tbody/tr[7]/td/ul/table/tbody/tr/td[1]/form/table/tbody/tr[8]/td/center/input").click()
                except:
                    emailBox.send_keys(Keys.RETURN)

                mem.write(ml + ", ")
        mem.close()
    interestedPerson.close()


# subscribe(url,subfile)




# imp(subfile)

#stopped at 16861 or something

# c = []
# with open("assets/subscribedLinks.txt","r") as f:
#     print(len(f.read().split(",")))
#     f.write("")
#     f.close()
#     ftext = f.read().split(",")
#     for thin in ftext:
#         print(thin + "\n")
#