# year/make/model
#image_gallery

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
driver.get('https://www.motortrend.com/cars/bmw')
driver.maximize_window()
time.sleep(5)

# for new tab withoutchrome
def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless=new")
    driver = webdriver.Chrome(options=ops)
    return driver 
driver1 = headless_chrome()

try:

    all_member_data  = pd.DataFrame()
    all_member_data2  = pd.DataFrame()
    year = [i.text.split(' ')[0] for i in driver.find_elements(By.XPATH,"//*[@class='group/card block w-full text-left relative @container']//div//div[2]//div//div//p[1]")]
    model = [i.text.split(' ')[1:] for i in driver.find_elements(By.XPATH,"//*[@class='group/card block w-full text-left relative @container']//div//div[2]//div//div//p[1]")]
    Car_img = [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@class='group/card block w-full text-left relative @container']")]


    d = {
            'Year':year,
            'Model_name':model,

        }
    
    d2 ={

            'IMG_LINK':Car_img
        }
    
    df = pd.DataFrame(d)
    all_member_data  = pd.concat([df,all_member_data])
    all_member_data.index = np.arange(1,len(all_member_data)+1)
    print(all_member_data)

    df2 = pd.DataFrame(d2)
    all_member_data2  = pd.concat([df2,all_member_data2])
    all_member_data2.index = np.arange(1,len(all_member_data2)+1)
    print(all_member_data2)
    all_member_data.to_csv('car_data.csv',index=True)
    all_member_data2.to_csv('car_link.csv',index=True)

    # driver.close()
    # driver.switch_to.window(driver.window_handles[0])


except Exception as e:
    print(e)

time.sleep(10)
driver.close()
