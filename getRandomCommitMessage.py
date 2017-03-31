import random
import csv
path="/Users/aramesh/Desktop/Coding/Git_Self/PythonScripts/CommitMessages.csv"
with open(path, 'rb') as f:
    reader = csv.reader(f)
    print ""
    for row in reader:
        print row[int(random.random()*100)%len(row)]
