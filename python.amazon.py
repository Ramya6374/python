from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
import time

driver.get("https://www.amazon.in/")
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="nav-search-bar-form"]/div[2]/div[1]').click()
search = driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
search.click()
search.send_keys("mobile")
search.send_keys(Keys.ENTER)
time.sleep(3)

driver.find_elements(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[2]/div/div').__getattribute__()
A = driver.find_elements(By.CLASS_NAME,"a-price-whole")[4]
print(A.text)
# time.sleep(3)
# driver.find_element(By.LINK_TEXT,'Inkast Denim Co').click()
# driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span').text()
# time.sleep(10)
# driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div/div[3]/div[1]/h2/a/span').click()
# time.sleep(10)
# print(driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div/div[3]/div[3]/div/a/span/span[2]/span[2]').text())
# time.sleep(10)
               # driver.execute_script("window.scrollBy(0,500);")