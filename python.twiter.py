from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
import time



driver.get("https://www.twitter.com/login")

time.sleep(10)
# driver.find_element (By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div').click()
driver.find_element(By.XPATH,"//input[@autocomplete='username']").send_keys('summaacc10')
time.sleep(2) 
driver.find_element(By.XPATH,"//*[text()='Next']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@autocomplete='current-password']").send_keys('charulatha')
time.sleep(5)

driver.find_element(By.XPATH,"//*[text()='Log in']").click()
time.sleep(5)
# driver.find_element(By.XPATH,"//span[@role = 'button']").click()

# driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys('summaacc10')
# driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
# time.sleep(10)
# driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys('charulatha')
# time.sleep(10)
# # driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span').click()
# time.sleep(10)
driver.execute_script("window.scrollBy(0,1500);")
time.sleep(5)