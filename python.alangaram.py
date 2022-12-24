from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
import time


driver.get("https://www.alankaram.in/")
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="fmtpl_tab_ca4261f-tab"]/span').click()

driver.execute_script("window.scrollBy(0,1000);")
# driver.find_element(By.CLASS_NAME,'woocommerce-loop-product__title').click()
time.sleep(3)
# driver.execute_script("window.scrollBy(0,500);")


# driver.find_elements(By.XPATH,'//*[@id="fmtpl_tab_ca4261f"]/div/ul/li[5]/div/div[2]/h2/a').click()
time.sleep(3)

A = driver.find_elements(By.CLASS_NAME,"woocommerce-loop-product__title")[4]
print(A.text)
x = driver.find_elements(By.CLASS_NAME,"price")[4]
print(x.text)


# search.click()
# search.send_keys("mobile")
# search.send_keys(Keys.ENTER)
# time.sleep(3)