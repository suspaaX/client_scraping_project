# Job Title, 
# Company, 
# Location, 
# Link 
# nikal

# insurance broker


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
driver.get('https://www.ziprecruiter.com/Jobs/Insurance-Broker/3?lk=XhiBoMjj2XskCwSXEUmxuw')
driver.maximize_window()
time.sleep(5)



def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless=new")
    driver = webdriver.Chrome(options=ops)
    return driver 

driver1 = headless_chrome()

try:


    all_member_data  = pd.DataFrame()
    Job_Title = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='font-bold text-primary text-header-md md:text-header-md-tablet']")]
    Company = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='grid gap-y-8']/a")]
    Location = [i.text.split('.')[0] for i in driver.find_elements(By.XPATH,"//*[@class='mb-24']/p")]
    # Link  = [driver.current_url]

    
    d = {

        'Job Title':Job_Title,
        'Company':Company,
        'Location':Location,
        # 'Link':Link

        }


    df = pd.DataFrame(d)
    all_member_data  = pd.concat([df,all_member_data])
    all_member_data.index = np.arange(1,len(all_member_data)+1)
    print(all_member_data)


    # driver.close()
    # driver.switch_to.window(driver.window_handles[0])


except Exception as e:
    print(e)

time.sleep(10)
driver.close()
