from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
driver.get('https://recruitment.farmers.com/industry-recruiter-locator/us')
driver.maximize_window()

try:


    all_data = pd.DataFrame()

    try:
        all_state = [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@class='c-directory-list-content']//li//h2//a")]
        for state in all_state[0:5]:
            driver.switch_to.new_window('tab')
            driver.get(state)


            try:
                st_all_profess = [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@class='c-directory-list-content-wrapper']/ul/li/h2/a")]
                for profess in st_all_profess:
                    driver.switch_to.new_window('tab')
                    driver.get(profess)



                    First_Name = [i.text.split(' ')[0] for i in driver.find_elements(By.XPATH,"//*[@class='LocationName']")]
                    Last_Name = [i.text.split(' ')[-1] for i in driver.find_elements(By.XPATH,"//*[@class='LocationName']")]


                    Address_line_1 = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='c-address']/div[1]/span")]
                    Address_line_2 = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='c-address']/div[2]/span")]

                    City = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='c-address']/div[3]/span[1]")]
                    State = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='c-address']/div[3]/abbr")]
                    Zip_Code = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='c-address']/div[3]/span[2]")]

                    Phone = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='Core-phone']/div/a")]
                    Email = [i.get_attribute('href').split(':')[1] for i in driver.find_elements(By.XPATH,"//*[@class='Core-email']/a")]
                    Image_link = [i.get_attribute('src') for i in driver.find_elements(By.XPATH,"//*[@class='AgentImage AgentImage--fallback AgentImage--hero']")]

                    # Company = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='LocationName']")]
                    # URL_Address = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='LocationName']")]

                    d = {

                            'First Name':First_Name,
                            'Last Name':Last_Name,
                            # 'Company':First_Name,
                            'Address line 1':Address_line_1,
                            'Address line 2':Address_line_2,
                            'City':City,
                            'State':State,
                            'Zip Code':Zip_Code,
                            'Phone':Phone,
                            # 'Email':Email,
                            # 'URL Address':profess,
                            # 'Image link':Image_link,

                        }

                    df = pd.DataFrame(d)
                    all_data = pd.concat([all_data,df])
                    all_data.index = np.arange(1,len(all_data)+1)
                    driver.close()          # 👈 YAHAN (profile tab band)
                    driver.switch_to.window(driver.window_handles[-1])
            except Exception as e:
                print(e)
        print(all_data)
        all_data.to_csv('industry-recruiter_data.csv',index=True)
        driver.close()          # 👈 YAHAN (state tab band)
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print(e)

except Exception as e:
    print(e)

time.sleep(10)
driver.close()