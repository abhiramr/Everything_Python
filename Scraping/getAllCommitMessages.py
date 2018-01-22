from BeautifulSoup import BeautifulSoup
import urllib2
import csv
def getCommits(n):
    li=[]
    url="http://whatthecommit.com/index.txt"
    for i in range(1,n):
        htmlp=urllib2.urlopen(url)
        soup=BeautifulSoup(htmlp)
        li.append(str(soup))
    myfile = open("CommitMessages.csv","wb")
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(li)
    return li
num=int(raw_input("How many commit messages to pull?"))
li2=[]
li2=getCommits(num)
