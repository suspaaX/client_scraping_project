from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time

driver = webdriver.Chrome()
link = 'https://www.yellowpages.com.au/search/listings?clue=interior+designer'
driver.get(link)
driver.maximize_window()

business_link = [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@class='Box__Div-sc-dws99b-0 fYIHHU']/a")]
business_name = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='MuiTypography-root MuiLink-root MuiLink-underlineNone MuiTypography-colorPrimary']/h3")]
business_address =[i.text for i in driver.find_elements(By.XPATH,"//*[@class='Box__Div-sc-dws99b-0 bKFqNV']//p")]


d = {'BUSINESS_NAME':business_name,
     'Business_link':business_link,
     'Business_address':business_address
     }

df = pd.DataFrame(d)
df.index = np.arange(1,len(df)+1)

print(df)
df.to_csv('Interior_Designer.csv',index=True)

time.sleep(10)
driver.close()

