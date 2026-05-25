# - First name
# - Last name 
# - Profile (e/g trainingpeaks.com/coach/palmares)
# - Email address
# Website




from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
driver.get('https://www.trainingpeaks.com/coaches/search')
driver.maximize_window()



# for new tab withoutchrome
def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless=new")
    driver = webdriver.Chrome(options=ops)
    return driver 

# for new tab with without window 
driver1 = headless_chrome()

try:



    all_member_data  = pd.DataFrame()
    all_profile = [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@class='profile-image']/a")]

    for profile in all_profile:
        driver.switch_to.new_window('tab')
        driver.get(profile)
        
        Name = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='u-flex u-flex-col u-items-start u-mt-4 sm:u-mt-0 sm:u-ml-6']//span[1]")]

        try:
            Website = [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@aria-label='Coach Website']")]

            if len(Website) < len(Name):
                diff = len(Name) - len(Website)
                Website.extend([""] * diff)
        except Exception  :
            None


        d = {
                'Name':Name,
                'Profile' :profile,
                'Website':Website
            }

        df = pd.DataFrame(d)
        all_member_data  = pd.concat([df,all_member_data])
        all_member_data.index = np.arange(1,len(all_member_data)+1)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        

    print(all_member_data)
    all_member_data.to_csv('trainingpeaks_coaches.csv',index=True)


except Exception as e:
    print(e)

time.sleep(10)
driver.close()
