from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
import time



driver.get("https://www.alankaram.in/")
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="fmtpl_tab_ca4261f-tab"]/span').click()

B = []
A = driver.find_elements(By.CLASS_NAME,"product-item-wrap")
# A = driver.find_element(By.XPATH,'//*[@id="fmtpl_tab_ca4261f"]/div/ul/li[3]/div')
print(A)
# driver.execute_script("window.scrollBy(0,3500);")
for i in A:
    B.append(i.text)
    print(i.text)
# driver.execute_script("window.scrollBy(0,3000);")
print(B)    


# Y = []
# X = driver.find_elements(By.CLASS_NAME,"price")
# print(X)
# for i in X:
#     Y.append(i.text)
#     print(i.text)
#     # Y.append(X)  
# print(Y)

# for keys,values in A.items():
#     print(keys,values)

# for keys, values in A.items():
#     print(keys,values)
# for key in A.keys():
#     print(key)
# for value in X.values():
#     print(value)


# print(driver.find_element(By.XPATH,'//*[@id="ap-none"]/div/div/div[2]').text())
time.sleep(3)