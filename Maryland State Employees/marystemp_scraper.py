'''
    # I need the resulting dataset to include data for
    # Year
    # Employer
    # Name
    # Title
    # Annual Wages
    # Source
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()

try:
    all_member_data  = pd.DataFrame()
    for i in range(1,101):
        driver.get(f'https://www.openthebooks.com/maryland-state-employees/?Year_S=2024&pg={i}')
        driver.maximize_window()
        # time.sleep(5)


        Year = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='employer-detail-table']//tbody/tr/td[1]")]
        Employer = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='employer-detail-table']//tbody//tr/td[2]")]
        Name = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='employer-detail-table']//tbody//tr/td[3]")]
        Title = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='employer-detail-table']//tbody//tr/td[4]")]
        Annual_Wages = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='employer-detail-table']//tbody//tr/td[5]")]
        Source = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='employer-detail-table']//tbody//tr/td[6]")]

        d = {
            
            'Year':Year,
            'Employer':Employer,
            'Name':Name,
            'Title':Title,
            'Annual Wages':Annual_Wages,
            'Source':Source

            }

        df = pd.DataFrame(d)
        all_member_data  = pd.concat([df,all_member_data])
        all_member_data.index = np.arange(1,len(all_member_data)+1)
    print(all_member_data)
    all_member_data.to_csv('employee.csv',index=True)

except Exception as e:
    print(e)

time.sleep(10)
driver.close()
