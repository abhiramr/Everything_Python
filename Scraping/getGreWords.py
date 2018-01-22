from BeautifulSoup import BeautifulSoup
import urllib2
import random
url_search="http://www.majortests.com/gre/wordlist_0"
links={}
for i in range(1,11):
    html_page = urllib2.urlopen(url_search+str(i))
    soup = BeautifulSoup(html_page)
    #links = {}
    for i in soup.findAll('tr'):
        links[i.fetch('th')[0].getText()]=i.fetch('td')[0].getText()
for key in sorted(links):
    print "%s:                              %s" % (key, links[key])
print "Number of words = ",len(links.keys())

#    print("Random=")
#    k1=random.choice(links.keys())
#    print str(k1)," : ",str(links[k1])
    #for key,value in links.items():
    #     print key,value
