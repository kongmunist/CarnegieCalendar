import os
files = ["downloadhistory.txt","referralhistory.txt","searchhistory.txt"]

for file in files:
    with open(os.path.join('data',file),'w') as f:
        f.write("")