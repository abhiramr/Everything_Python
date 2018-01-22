import re
from BeautifulSoup import BeautifulSoup
import urllib2
import HP_GetCharacterList

la=HP_GetCharacterList.
html_page = urllib2.urlopen("http://www.readfreeonline.net/OnlineBooks/Harry_Potter_and_the_Order_of_the_Phoenix/Harry_Potter_and_the_Order_of_the_Phoenix_38.html")
soup=BeautifulSoup(html_page)
mydivs = soup.find("td",{ "class" : "ContentCss" }).getText()
text=mydivs.replace("&nbsp","\n")
re.findall("[A-Z][a-z]*",text)
