'''
✅ Name
✅ Clinic Name
✅ Email (only if publicly listed)
✅ Phone
✅ City & State
✅ Website URL

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
driver.get('https://www.fertilityiq.com/fertilityiq/provider_search?location_type=all_us&type=doctor')
driver.maximize_window()

def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless=new")
    driver = webdriver.Chrome(options=ops)
    return driver 
driver1 = headless_chrome()

try:

    all_data = pd.DataFrame()
    all_doc_links =  [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@class='search-results-card js-marker-hover search-results-card--doctor  ']")]

    for doctor in all_doc_links:
        driver1.switch_to.new_window('tab')
        driver1.get(doctor)
    
        doct_name = [i.text for i in driver1.find_elements(By.XPATH,"//*[@class='provider__title']")]
        # clinic_Name = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='']/")]
        # # Email = 
        # phone_1 = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='']/")]
        # address_1 = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='']/")]
        # phone_2 = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='']/")]
        # address_2 = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='']/")]
        # Website_URL = 

        d = {

            'Doctor_Name':doct_name,
            # 'Clinic Name': clinic_Name,
            # # 'Email':
            # 'Phone':phone_1,
            # 'Address1':address_1,
            # 'Address2':address_2,
            # 'Website URL':

            }


        df = pd.DataFrame(d)
        all_data = pd.concat([all_data,df])
        all_data.index = np.arange(1,len(all_data)+1)
        # driver.close()
        # driver.switch_to.window(driver.window_handles[0])
        print(all_data)

    print(all_data)
    all_data.to_csv('doctors.csv',index=True)



except Exception as e:
    print(e)

time.sleep(10)
driver.close()
