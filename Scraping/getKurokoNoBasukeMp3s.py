from BeautifulSoup import BeautifulSoup
import urllib2
import re
import urllib

urlsearch1="http://anime.thehylia.com/soundtracks/album/kuroko-no-basket-original-soundtrack"
html_page=urllib2.urlopen(urlsearch1)
soup=BeautifulSoup(html_page)

links=[]
for link in soup.findAll('a'):
    links.append(link.get('href'))

links2=[]
for i in links:
    if "mp3" in i:
        links2.append(i)

counter=1
for j in links2:
    html_page_temp=urllib2.urlopen(j)
    soup=BeautifulSoup(html_page_temp)
    linksh=[]
    for link in soup.findAll('a'):
        linksh.append(link.get('href'))
    urllib.urlretrieve(linksh[-1],str(counter)+".mp3")
    counter=counter+1
