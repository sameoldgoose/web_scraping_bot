# importing the required libraries
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

data = []
# selenium setup
options = Options()
options.add_experimental_option('detach', True)
website = 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'
os.environ['PATH'] += r"C:\Users\richi\Desktop\ABC\java\python\webscrape\Selenium\chromedriver"
driver = webdriver.Chrome()
driver.get('https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787')
WebDriverWait(driver, timeout=30).until( EC.presence_of_element_located((By.ID, "1")))
inner_list = []
'''
GETTING DATA FOR FIRST ROW AS IT DOESNT HAVE AN ID
'''
tds = driver.find_elements(By.TAG_NAME,'td')
a = tds[1].find_element(By.TAG_NAME,'a')
act = a.get_attribute('onclick')
driver.execute_script(act,a)
WebDriverWait(driver, timeout=30).until( EC.presence_of_element_located((By.CLASS_NAME, 'posting-second-header')))
close = driver.find_element(By.CLASS_NAME,'posting-second-header').find_elements(By.TAG_NAME,'b')
print(close[2].text)
inner_list.append(close[2].text)
trs = driver.find_elements(By.TAG_NAME,'tr')
est=trs[18].find_elements(By.TAG_NAME,'td')[1].text
print(trs[18].find_elements(By.TAG_NAME,'td')[1].text)
inner_list.append(est)
desc = trs[21].find_elements(By.TAG_NAME,'td')[1].text
inner_list.append(desc)
print(trs[21].find_elements(By.TAG_NAME,'td')[1].text)
data.append(inner_list)
driver.get('https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787')

'''
GETTING DATA FOR LAST 4 ROW WITH ID
'''

for i in range(1,5):
    inner_list=[]
    WebDriverWait(driver, timeout=30).until( EC.presence_of_element_located((By.ID, "1")))
    tr = driver.find_element(By.ID,str(i))
    tds = tr.find_elements(By.TAG_NAME,'td')
    a = tds[1].find_element(By.TAG_NAME,'a')
    act = a.get_attribute('onclick')
    driver.execute_script(act,a)
    WebDriverWait(driver, timeout=30).until( EC.presence_of_element_located((By.CLASS_NAME, 'posting-second-header')))
    close = driver.find_element(By.CLASS_NAME,'posting-second-header').find_elements(By.TAG_NAME,'b')
    print(close[2].text)
    inner_list.append(close[2].text)
    trs = driver.find_elements(By.TAG_NAME,'tr')
    est = trs[18].find_elements(By.TAG_NAME,'td')[1].text
    desc = trs[21].find_elements(By.TAG_NAME,'td')[1].text 
    print(trs[18].find_elements(By.TAG_NAME,'td')[1].text)
    print(trs[21].find_elements(By.TAG_NAME,'td')[1].text)
    # adding Est. Value Notes to inner list
    inner_list.append(est)
    # adding Description to inner list
    inner_list.append(desc)
    # appending inner_list to data which will be added to csv file
    data.append(inner_list)
    driver.get('https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787')
with open('data.csv', 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    # writing the data rows 
    csvwriter.writerows(data)
# closes the browser
driver.quit()