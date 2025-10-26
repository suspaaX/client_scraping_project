from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
driver.get('https://markcubancompanies.com')
driver.maximize_window()
time.sleep(10)


Brand_name = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='pos-abs-cover']/p")]
brand_website = [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@class='pos-abs-cover']")]
# print(len(brand_website))

# company_click = driver.find_element(By.XPATH,"//*[@class='company-item grid-item shuffle-item shuffle-item--visible']").click()
for i in brand_website:
    driver.switch_to.new_window(i)
    time.sleep(2)
    




# d = {
#         'BRAND_NAME':Brand_name,
#         'BRAND_WEBSITE':brand_website
#     }

# df = pd.DataFrame(d)
# df.index = np.arange(1,len(df)+1)
# print(df)
# df.to_csv('markcubancompanies.csv',index=True)

time.sleep(10)
driver.close()
