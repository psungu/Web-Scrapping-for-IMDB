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

chrome_path='/Users/pinar/Downloads/chromedriver'

driver = webdriver.Chrome(chrome_path)#,chrome_options=chrome_options)

filmName=[]
rest=[]
for i in range(1,10000,50):
    #print(i)
    url="https://www.imdb.com/search/title?title_type=feature&year=2017-01-01,2017-12-31&sort=alpha,asc&start="+str(i)+"&ref_=adv_nxt"
    driver.get(url)
    containers = driver.find_elements_by_xpath('//h3[@class="lister-item-header"]')
    others=driver.find_elements_by_xpath('//div[@class="lister-item mode-advanced"]')
    print(containers)
    for c in containers:
        tempFilmName= c.find_element_by_css_selector('a').text
        filmName.append(tempFilmName)
    for a in others:
        string=a.find_elements_by_css_selector('p')[2].text
        rest.append(string)
        # bas=string.split(":")
        # dir=bas[1].split("|")
        # directors.append(dir[0][1:-1])
        # print(bas[2][1:-1])
        # stars.append(bas[2][1:-1])

df = pd.DataFrame({'movie2017': filmName,'director&actor': rest})

df.to_csv('../taskrabbit/imdbss.csv', index=False)
print(df)

#flm2017,director&actor
