from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
driver.get('https://www.datacenters.com/locations/australia')
driver.maximize_window()
time.sleep(10)


company_name = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='flex flex-col gap-1']/div[1]")]
dc_name = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='flex flex-col gap-1']/div[2]")]
dc_address = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='flex flex-col gap-1']/div[3]")]

d = {
        'COMPANY_NAME':company_name,  
        'DATA_CENTRE_NAME':dc_name,
        'DATA_CENTRE_ADDRESS':dc_address
    }

df = pd.DataFrame(d)
df.index = np.arange(1,len(df)+1)
print(df)
df.to_csv('data_centre.csv',index=True)

time.sleep(10)
driver.close()



