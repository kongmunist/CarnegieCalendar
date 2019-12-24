
import isEventRegex as ier
from bs4 import BeautifulSoup
from requests import *
import wget
from selenium import webdriver

#
# url = "https://thebridge.cmu.edu/event/2549283"
# browser = webdriver.PhantomJS()
# browser.get(url)
# html = browser.page_source
# soup = BeautifulSoup(html, 'lxml')
# a = soup.find('section', 'wrapper')


# r = get(url)
# soup = BeautifulSoup(r.text,"lxml")



# txt = soup.get_text()
# print(txt)
# print("time: ", ier.findTime(txt))
# print("date: ", ier.findDate(txt))
# print("location: ", ier.findLoc(txt))
#





# url = "https://www.cmu.edu/news/stories/archives/2019/february/army-ai-task-force.html"
# response = get(url)
#
# soup = BeautifulSoup(response.text,"xml")
# a = soup.get_text()
# b = ""
#
# totalLen = 0
# it = 0
# for line in a.split("\n"):
#     thing = line.strip()
#     if thing != "" and len(thing) > 172:
#         totalLen += len(thing)
#         it += 1
#         b += thing + "\n"
#
#
# c = b.split("\n")
# c.append("nah")

# c = """ SCS Faculty Candidate
# with MRINMAYA SACHAN
# FEB
# 11
# 10AM
# TALKS
#
# Gates Hillman Centers
# ASA Conference Room 6115"""

# c = """Hi everyone,
#
# This week we'll have our regular PPP meeting. We'll be primarily working on Plaid CTF problem development (and testing) during the meeting, but we'll also have the floor open for CTF problem demos.
#
# What: PPP Meeting
# When: Friday, February 8th, 5:00 PM
# Where: CIC 1201
#
# Corwin
# _______________________________________________
# Plaid-parliament-pwning mailing list
# Plaid-parliament-pwning@lists.andrew.cmu.edu
# https://lists.andrew.cmu.edu/mailman/listinfo/plaid-parliament-pwning
# """


# c = """Are you interested in doing undergraduate research in math but are unsure of what opportunities are available? Thankfully, Math Club has a solution for you. This Wednesday (2/6) at in Porter Hall 100 (PH100) we will be having Dr. Irina Gheorghicuic and Dr. Jason Howell talk about what research opportunities exist for undergraduates both at CMU and elsewhere. For more information, see below!"""

#
# c = """The Center for Student Diversity & Inclusion and the University Lecture Series invite you to this year’s Martin Luther King, Jr. Keynote Lecture:
#
# Khalil G. Muhammad
# Professor of History, Race and Public Policy at Harvard Kennedy School and Suzanne Young Murray Professor at the Radcliffe Institute for Advanced Study
#
# Who Controls the Past Controls the Future:
# Race, Inequality and American Democracy
#
# Monday, February 11
# 4:30 p.m.
# McConomy Auditorium, Cohon University Center
# A reception will immediately follow.
#
# The United States’ global dominance has long been the envy of the world. But the role of race to native born and newcomer alike has been treated often as aberrational, an unfortunate artifact of the nation’s past.
#
# The event is free and open to the public.
#
# Sponsored by the President's Office, University Lecture Series, Center for Student Diversity & Inclusion and Dietrich College Humanities Scholars Program.
#
# Questions? Contact University Events."""

# c = """This is a reminder that we have a town hall meeting today at 12pm.    Lunch will be provided.
# The meeting will be held on the 4th floor of the CIC building in Panther Hollow room 4101.    """

#
# c = """Forwarding this message on behalf of our friends at Morgan Stanley!
#
# ---
#
# We wanted to reach out to let you know that Morgan Stanley will on-campus on Wednesday, February 13th for a Technology Panel, and I’m hoping you can help get the word out to your friends and classmates. A marketing flyer can be found attached, but also please find the details information below:
#
#
#
# Event: CMU Technology Panel Presentation
#
# Date: Wednesday, February 13, 2019
#
# Time: 5:30 - 6pm
#
# Location: Posner Hall, Room A35
#
# To register for the event, please click here
#
#
#
# We hope to see you there! J
#
#
#
# Kindest Regards,
#
# Alyssa
#
#
#
# Alyssa Fleischman
# Consultant | Human Resources
# 1585 Broadway, 19th Floor | New York, NY  10036
# Phone: +1-212-761-3908
# Alyssa.Fleischman@morganstanley.com   """
#
def isEvent(text):
    text = text.replace("\n", " ")
    if ier.findDate(text) != None and ier.findTime(text) != None and ier.findLoc(text) != None:
        return True
    else:
        return False
#
# c = "CMU - Department of Materials Science and Engineering - Carnegie Mellon University Carnegie Mellon University ——— Search Search Search this site only Department of Materials Science and Engineering Welcome to MSE The Department of Materials Science and Engineering (MSE) is one of seven academic departments in Carnegie Institute of Technology, the engineering college at Carnegie Mellon. MSE has a long and distinguished tradition in materials education and research, and today our faculty continue to address the more important and challenging issues at the forefront of science and technology. Materials Science and Engineering is an interdisciplinary activity that applies the principles of basic sciences and engineering to understanding the behavior of materials, their development and applications. Both our undergraduate and graduate students are exposed to this interdisciplinary approach. Spring 2019 - Fridays at 11:30am - Doherty Hall 2210 Application Submission Cycles Fall Term of Entry Ph.D.: October 1 – December 15 M.S.: October 1 – January 15 Spring Term of Entry Ph.D.: July 1 – September 26 MSE EMPLOYMENT OPPORTUNITY Materials Characterization Facilities Specialist, MSE-2011151 Tweets by cmu_mse Materials Research Recent Research Highlights Make an impact in MSE today!Visit giving.cmu.edu/mse Carnegie Mellon College of Engineering Directions Carnegie Mellon University5000 Forbes AvenueWean Hall 3325Pittsburgh, PA 15213412-268-2700 Fax 412-268-7596 Legal Info www.cmu.edu © 2019 Carnegie Mellon University News & Events Newsletters Departmental Seminar Series People Faculty Research MSE Alumni Faculty Faculty-Courtesy Faculty-Emeritus Faculty-Adjunct Staff MSE Staff - Point of Contact Graduate Program Graduate Student Advisory Committee GSAC Summer Seminar Series Graduate Student Symposium Master of Science Programs Master of Science In Additive Manufacturing Dual Degree Programs Master of Science In Materials Science Master of Science In Materials Science and Engineering Doctor Of Philosophy Undergraduate Program Undergraduate Curriculum Objectives, Outcomes, Mission, Accreditations Core Course Content B.S. in MSE Sample Schedule MSE Additional Major Programs Research Opportunities Integrated Master and Bachelor (IMB) Degrees Careers Facilities SEM Training Course TEM Training Course Research Research Centers Computational Materials Science Inorganic Functionall Materials Manufacturing and Materials Microstructure Materials for Healthcare"


c = """There will be a midterm review session tomorrow (2/10) at 4 pm in GHC 4215. We'll be going over examples for the topics that could be on the midterm. Please come with questions and post below with any topics you want to make sure are covered in the review!
This week's lab will be focused on midterm review (attendance is still required). Since the lab is the day before the midterm, we will be releasing the lab early to give you more time to work with it. We'll update this post when it's released.
Sunday Office Hours start this week! I'm sorry for the delay on this, but they are starting tomorrow. They'll be """#every Sunday 12-6 in BH 235B."""

print(isEvent(c))
print(ier.findTime(c),ier.findDate(c),ier.findLoc(c))

# url = "https://hcii.cmu.edu/news"
# url = "https://thebridge.cmu.edu/events"


# soup = BeautifulSoup(response.text,"lxml")
#
# for script in soup(["script", "style", "aside"]):
#     script.decompose()

# for thing in soup.find_all("a"):
#     txt = thing.get("href")
#     print(txt)


#     try:
#         r = get(txt)
#         s = BeautifulSoup(r.text, "lxml")
#         for scrip in s(["script","style","aside"]):
#             script.decompose()
#         txt = s.get_text()
#
#         if isEvent(txt):
#             print("YOUR SHIT WORKED")
#             print(ier.findLoc(txt), ier.findDate(txt), ier.findTime(txt))
#             print(txt)
#     except:
#         pass





# def getA(link):
#     response = get(link)
#     soup = BeautifulSoup(response.text,"lxml")
#
#     for script in soup(["script", "style", "aside"]):
#         script.decompose()
    # for thing in soup.find_all("a"):

        # print(thing.get("href"))
    # return soup.find_all("a")
# print(soup.find_all("h1"))
# print(soup.get_text())

# for script in soup(["script", "style"]):
#     script.decompose()
#
# print()


# c = c.replace("\n"," ")

# print(repr(c))
# print(ier.findDate(c))
# print(ier.findTime(c))



# print(b)
# print(isEvent.isEvent(b))

# print(thing/it)