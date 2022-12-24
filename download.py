import urllib.request as A
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
import time

driver.get("https://www.google.com/")
# A.urlretrieve(driver.find element (By. xpath,"//*[@id="islrg"]/div[1]/div[13]/a[1]/div[1]/img")'A.png')
# A.get("")
search = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search.click()
time.sleep(2)
search.send_keys("sdd")
time.sleep(2)
search.send_keys(Keys.ENTER)

driver.find_element(By.XPATH,'//*[@id="hdtb-msb"]/div[1]/div/div[3]/a').click()
time.sleep(2)
sdd = driver.find_element(By.XPATH,'//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
time.sleep(2)
img = sdd.get_attribute("src")

A.urlretrieve(img,"sdd.jpg")

