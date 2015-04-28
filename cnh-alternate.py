__author__ = 'Abhiram'
# Downloads CnH comics

import urllib

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


num = 1
driver = webdriver.Firefox()
driver.get("http://explosm.net/comics/latest/")
while 1:
    wait = WebDriverWait(driver, 10)
    url = wait.until(EC.element_to_be_clickable((By.ID, "main-comic")))
    urllib.urlretrieve(url.get_attribute("src"), str(num) + ".jpeg")
    button = driver.find_element_by_class_name("previous-comic")
    button.click()
    num += 1