from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/playlist?list=PLfqMhTWNBTe137I_EPQd34TsgV6IO55pt')
driver.maximize_window()
time.sleep(5)


# for new tab withoutchrome
# def headless_chrome():
#     ops = webdriver.ChromeOptions()
#     ops.add_argument("--headless=new")
#     driver = webdriver.Chrome(options=ops)
#     return driver 

# for new tab with without window 
# driver1 = headless_chrome()

try:

    title = [i.text for i in driver.find_elements(By.XPATH,"//*[@id='video-title']")]
    title_link = [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@id='video-title']")]
    
    d = {
        'Title':title,
        'Title_link':title_link
        }

    df = pd.DataFrame(d)
    df.index = np.arange(1,len(df)+1)
    print(df)
    df.to_csv('dsa.csv',index=True)


except Exception as e:
    print(e)

time.sleep(10)
driver.close()
