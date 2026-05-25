# Attorney Name
# Full Office Address (street, city, state, ZIP)
# Email address (only if publicly available on Avvo or official site)


# Source: Avvo
# County: Los Angeles County
# State: California
# Attorney Type: Family Law Attorneys


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
driver.get(f'https://www.avvo.com/family-lawyer/ca/los_angeles.html')
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
    for i in range(1,192):
        driver.get(f'https://www.avvo.com/family-lawyer/ca/los_angeles.html?page={i}')


        Attorney_Name = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='profile-name']/a")]
        try:
            Attorney_address = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='address']")]
            if len(Attorney_address) < len(Attorney_Name):
                diff = len(Attorney_Name) - len(Attorney_address)
                Attorney_address.extend([""] * diff)
        except Exception  :
            None
            

        d = {
            
            'Attorney_name':Attorney_Name,
            'Attorney_address':Attorney_address

            }

        df = pd.DataFrame(d)
        all_member_data  = pd.concat([df,all_member_data])
        all_member_data.index = np.arange(1,len(all_member_data)+1)
        print(i)


    print(all_member_data)
    all_member_data.to_csv('family attorney.csv',index=True)

except Exception as e:
    print(e)

time.sleep(10)
driver.close()
