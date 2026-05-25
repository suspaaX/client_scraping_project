#   - use columns: school name, city, state, phone, website, enrollment size

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
driver.get('https://www.niche.com/k12/search/best-private-schools/')
driver.maximize_window()
time.sleep(5)


# # for new tab withoutchrome
# def headless_chrome():
#     ops = webdriver.ChromeOptions()
#     ops.add_argument("--headless=new")
#     driver = webdriver.Chrome(options=ops)
#     return driver 

# # for new tab with without window 
# driver1 = headless_chrome()

try:

    school_name = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='MuiTypography-root MuiTypography-headlineMedium nss-fiu0ds']/")]
    # city = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='']/")]
    # state = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='']/")]
    # phone = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='']/")]
    # website = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='']/")]
    # enrollment_size = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='']/")]

    # for new tab with new window 
    # for name in Company_name[0:1]:
    #     driver.switch_to.new_window('tab')
    #     driver.get(name)

    d = {
        
        'school name':school_name,
        # 'city':city,
        # 'state':state,
        # 'phone':phone,
        # 'website':website,
        # 'enrollment size':enrollment_size

        }

    df = pd.DataFrame(d)
    df.index = np.arange(1,len(df)+1)
    print(df)
    df.to_csv('Private School Data.csv',index=True)

# code for merge multiple data in data frame
    # all_member_data  = pd.DataFrame()
    # ##########some code########
    # df = pd.DataFrame(d)
    # all_member_data  = pd.concat([df,all_member_data])
    # all_member_data.index = np.arange(1,len(all_member_data)+1)
    # print(all_member_data)

#page lose krne same window page open krne ke lye 
    # driver.close()
    # driver.switch_to.window(driver.window_handles[0])


except Exception as e:
    print(e)

time.sleep(10)
driver.close()
