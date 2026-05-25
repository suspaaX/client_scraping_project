# Fields Required
# - Park Name
# - Site Street Address
# - Site City
# - Site State
# - Site Zip Code
# - Site County
# - Website
# - Number of RV Sites (if available)
# - Source(s) (which directory or directories the entry came from)  


# Deliverables 
# - campendium__rv_parks.xlsx / .csv
# - goodsam__rv_parks.xlsx / .csv
# - rvparkstore__rv_parks.xlsx / .csv
# - master__rv_parks.xlsx / .csv (merged + deduped with site counts + source flags)


# Campendium.com


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
all_member_data  = pd.DataFrame()
for i in range(1,5):
    driver.get(f'https://www.rvparkstore.com/rv-park-directory/alabama/all/page/{i}?view=no_map')
    driver.maximize_window()
    time.sleep(1)



    


    Park_Name = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='item-title-box']/a")]

    try:
        Site_Street_Address = [i.text for i in driver.find_elements(By.XPATH,"//*[@itemprop='streetAddress']")]
        if len(Site_Street_Address) < len(Park_Name):
            diff = len(Park_Name) - len(Site_Street_Address)
            Site_Street_Address.extend([""] * diff)
    except Exception  :
            None

    try:
        Site_city = [i.text for i in driver.find_elements(By.XPATH,"//*[@itemprop='addressLocality']")]
        if len(Site_city) < len(Park_Name):
            diff = len(Park_Name) - len(Site_city)
            Site_city.extend([""] * diff)
    except Exception  :
            None


    # try:
    #     Site_state = [i.text for i in driver.find_elements(By.XPATH,"//*[@itemprop='addressRegion']")]
    #     if len(Site_state) < len(Park_Name):
    #         diff = len(Park_Name) - len(Site_state)
    #         Site_state.extend([""] * diff)
    # except Exception  :
    #         None

    try:
        Site_Zip_Code = [i.text for i in driver.find_elements(By.XPATH,"//*[@itemprop='postalCode']")]
        if len(Site_Zip_Code) < len(Park_Name):
            diff = len(Park_Name) - len(Site_Zip_Code)
            Site_Zip_Code.extend([""] * diff)
    except Exception  :
            None

    
    d = {

        'Park Name':Park_Name,
        'Site Street Address':Site_Street_Address,
        'Site City':Site_city,
        # 'Site State':Site_state,
        'Site Zip Code':Site_Zip_Code,


        }


    df = pd.DataFrame(d)
    all_member_data  = pd.concat([df,all_member_data])
    all_member_data.index = np.arange(1,len(all_member_data)+1)
print(all_member_data)
all_member_data.to_csv('rvparkstore__rv_parks.csv',index=True)

# #page lose krne same window page open krne ke lye 
#     driver.close()
#     driver.switch_to.window(driver.window_handles[0])



time.sleep(10)
driver.close()
