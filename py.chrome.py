from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
import time



driver.get("http://websites.milonic.com/newtours.demoaut.com/")

print(driver.title)

driver.get("http://pavantestingtools.blogspot.in/")
time.sleep(3)

print(driver.title)

driver.back()
print(driver.title)
driver.forward()
time.sleep(3)
print(driver.title)