import word2vec
import csv

# with open("text8",'r') as f:
#     print(f.read())
#     f.close()
#


def checkSim(checkList = []):
    model = word2vec.load("text8.bin")

    for word in checkList:
        i,m = model.similar(word)
        print(word)
        print(model.vocab[i])
        print()

# checkSim(['meet','greet', 'session','training','visit','visiting','meeting'])
checkSim(['fair'])

# def processCSV(file):
