import csv

def writeToFile(dates, beginTimes, endTimes, locations, keywords):
    with open("eventOther.csv", mode="w") as employFile:
        writeObject = csv.writer(employFile,delimiter=',')
        writeObject.writerow(["Date", "Start Time", "End Time", "Location", "Keywords"])
        for i in range(len(dates)):
            writeObject.writerow([dates[i],beginTimes[i],endTimes[i],locations[i], keywords[i]])


def readFromFile(filename):
    with open(filename, mode = "r") as eventFile:
        readObj = csv.reader(eventFile, delimiter = ",")
        it = 0
        data = []
        lineLen = 0
        for row in readObj:
            if it == 0:
                lineLen = len(row)
                for i in range(len(row)):
                    data.append([row[i]])
            else:
                for i in range(lineLen):
                    data[i].append(row[i])
            it += 1
        return data

# print(readFromFile("event.csv"))