from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
driver.get('https://pandektis.ekt.gr/pandektis/handle/10442/4968/browse?type=title&submit_browse=Title&sort_by=1')
driver.maximize_window()
time.sleep(5)


# for new tab withoutchrome
def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless=new")
    driver = webdriver.Chrome(options=ops)
    return driver 

# for new tab with without window 
driver1 = headless_chrome()

all_items = [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@class='hoverbox_no_image']/ul/li/a")]



try:

    all_member_data  = pd.DataFrame()
    for item in all_items[0:7] :
        driver.switch_to.new_window('tab')
        driver.get(item)
        
        old_name_gr = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='ekt_met_main-column']/div[6]/div[2]")]
        old_name_en = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='ekt_met_main-column']/div[6]/div[4]")]
        new_name_gr = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='ekt_met_main-column']/div[9]/div[2]")]
        new_name_en = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='ekt_met_main-column']/div[9]/div[4]")]
        prefecture = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='ekt_met_main-column']/div[1]/div[4]")]
        province =     [i.text for i in driver.find_elements(By.XPATH,"//*[@class='ekt_met_main-column']/div[2]/div[4]")]
        renaming_date = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='ekt_met_main-column']/div[7]/div[4]")]


        d = {
            'Old_name_gr':old_name_gr,
            'Old_name_en':old_name_en,
            'New_name_gr':new_name_gr ,
            'New_name_en':new_name_en ,
            'Prefecture': prefecture,
            'Province': province,
            'Rnaming_date': renaming_date,

            }


#     # code for merge multiple data in data frame

        df = pd.DataFrame(d)
        all_member_data  = pd.concat([df,all_member_data])
        all_member_data.index = np.arange(1,len(all_member_data)+1)

#     # #page lose krne same window page open krne ke lye 
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print(all_member_data)
        all_member_data.to_csv('Pandektis_scraper.csv',index=True)


except Exception as e:
    print(e)

time.sleep(10)
driver.close()
