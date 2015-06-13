import re
from BeautifulSoup import BeautifulSoup
import random
import urllib2


def getCharacters():
    html_page3 = urllib2.urlopen("http://www.happychild.org.uk/ifs/wordsearch/harrypottercharactersindex.htm")
    souphp=BeautifulSoup(html_page3)
    lihp=souphp.findAll("font")
    lahp=[]
    for i in lihp:
        if i.getText()==(i.getText()).upper() and len(i.getText())>1 and ("CHARACTER" not in i.getText()) and ("CHARACTERS" not in i.getText()) and ("(" not in i.getText()):
            lahp.append(i.getText())
    count=int(random.random()*1000) 
    fname="hpchars"+str(count)+".txt"
    f=open(fname,"w")  
    lahpf=lahp[22:-8]
    for i in lahpf:
        f.write(i)
        f.write("\n")
    f.close() 
    return lahpf

if __name__=="__main__":
    fin_list=getCharacters()    
