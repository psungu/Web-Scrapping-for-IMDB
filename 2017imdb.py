from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import itertools

timeStarted=time.time()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

def wait():
    driver.implicitly_wait(15)
    WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located and EC.visibility_of_all_elements_located)

timeout=30

chrome_path='C:/Users/pinar.sungu/Downloads/chromedriver'

driver = webdriver.Chrome(chrome_path)  #,chrome_options=chrome_options)

filmName=[]
rest=[]
for i in range(1,10000,50):
    #print(i)
    url="https://www.koton.com/tr/koton/c/M01?sort=price-asc&columnType=triple"+str(i)+"&rel=next"

    driver.get(url)
    containers = driver.find_element_by_xpath("//div[@class='productGrid col-xs-12']") 
    #others=driver.find_elements_by_xpath('//div[@class="lister-item mode-advanced"]')
    print(containers)

    #containers = driver.find_elements_by_tag_name("img")
    #for image in containers :
    #    print(image.get_attribute("src"))
    filmName.append(containers)

    #for a in others:
        #string=a.find_elements_by_css_selector('p')[2].text
        #rest.append(string)
        # bas=string.split(":")
        # dir=bas[1].split("|")
        # directors.append(dir[0][1:-1])
        # print(bas[2][1:-1])
        # stars.append(bas[2][1:-1])

df = pd.DataFrame({'movie2017': filmName})

df.to_csv('../taskrabbit/imdbss.csv', index=False)
print(df)

#flm2017,director&actor
