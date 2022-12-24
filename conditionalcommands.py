from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
import time


driver.get("https://demo.guru99.com/test/newtours/")

ele = driver.find_element(By.NAME,"userName")
print(ele.is_displayed())
print(ele.is_enabled())

pwd_ele = driver.find_element(By.NAME,"password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled()) 
ele.send_keys("mercury")
pwd_ele.send_keys("merkury")

driver.find_element(By.NAME,"submit").click()