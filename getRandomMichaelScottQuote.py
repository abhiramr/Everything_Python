import HTMLParser
from BeautifulSoup import BeautifulSoup
import urllib2

url_search2="http://www.ack.org/~heffner/michael_scott.php"
html_page = urllib2.urlopen(url_search2)
soup = BeautifulSoup(html_page)
h = HTMLParser.HTMLParser()
print h.unescape(soup.find('p').text)
