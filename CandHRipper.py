import os
import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def dates(ystart):
    dm={'01': 31} #,'02': 28,'03': 31,'04': 30,'05': 31,'06': 30,'07': 31,'08': 31,'09': 30,'10': 31,'11': 30,'12': 31}
    for i in range(ystart,ystart+1):
        for x in sorted(dm.keys()):
            for j in range(10,dm.get(x)+1):
                driver = webdriver.Chrome()
                year_final=(str(i)+"/"+str(x)+"/"+str(j))
                driver.get("http://www.gocomics.com/calvinandhobbes/"+year_final)
                wait = WebDriverWait(driver, 30)
                url = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"strip")))
                urllib.urlretrieve(url.get_attribute("src"), str(i)+str(x)+str(j) + ".jpeg")
                driver.close() 
                
years=(raw_input())
while len(years)!=4:
    years=(raw_input())
dates(int(years))
