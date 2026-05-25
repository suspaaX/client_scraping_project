# CompanyName	            FirstName	LastName	Address1	        Address2	City	    State	ZipCode	    Phone	        Email	                    Web	Source                  Link
# MV Auction Center (MVAC)	Mark	    Abare	    141 NH-101A	        Unit B3	    Amherst	    NH	    03031	    603-688-0430	MVauctioncenter@gmail.com	www.MVauctioncenter.com	    https://www.auctionzip.com/NH-Auctioneers/1254442.html


from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()

driver.get('https://www.auctionzip.com/Auctioneer-Directory/')
driver.maximize_window()
time.sleep(10)

def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless=new")
    driver = webdriver.Chrome(options=ops)
    return driver 
driver1 = headless_chrome()

try:

    all_member_data  = pd.DataFrame()

    all_alphabet_link =[i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@class='auc-directory-inner']/section[1]/a")]
    for alphabet in all_alphabet_link[0:1]:
        driver.switch_to.new_window('tab')
        driver.get(alphabet)

        person_profile_link = [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@class='auc-directory__table--header--auc-name']/a")]
        
        for person in person_profile_link:
            driver.switch_to.new_window('tab')
            driver.get(person)        

            comp_name = [j.text for j in driver.find_elements(By.XPATH,"//*[@class='col-md-9']/hgroup/h1")]
            fname = [i.text.split(' ')[0] for i in driver.find_elements(By.XPATH,"//*[@class='auc-home__info col-md-6']/ul/li[1]")]
            lname = [i.text.split(' ')[1] for i in driver.find_elements(By.XPATH,"//*[@class='auc-home__info col-md-6']/ul/li[1]")]
            # city =  [i.text.split(' ')[0] for i in driver.find_elements(By.XPATH,"//*[@class='auc-home__info col-md-6']/ul/li[3]")]
            # state = [i.text.split(' ')[1] for i in driver.find_elements(By.XPATH,"//*[@class='auc-home__info col-md-6']/ul/li[3]")]
            # Address1 = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='auc-home__info col-md-6']/ul/li[2]")]
            # Address2 = [i.text.split(',')[0] for i in driver.find_elements(By.XPATH,"//*[@class='auc-home__info col-md-6']/ul/li[3]")]
            # ZipCode	=[i.text.split(' ')[2] for i in driver.find_elements(By.XPATH,"//*[@class='auc-home__info col-md-6']/ul/li[3]")]
            # Phone = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='auc-home__info col-md-6']/ul/li[4]")]
            # Email = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='auc-home__info col-md-6']/ul/li[5]//a")]
            # Web_Source =[i.text for i in driver.find_elements(By.XPATH,"//*[@class='auc-home__info col-md-6']/ul/li[6]//a")]

            d = {

                'CompanyName':comp_name,
                'FirstName':fname,
                'LastName':lname,
                # 'Address1':Address1,
                # 'Address2':Address2,
                # 'City':city,
                # 'State':state,
                # 'ZipCode':ZipCode,
                # 'Phone':Phone,
                # 'Email':Email,
                # 'WebSource':Web_Source,
                # 'Link':person
                
                }

            df = pd.DataFrame(d)
            all_member_data  = pd.concat([df,all_member_data])
            all_member_data.index = np.arange(1,len(all_member_data)+1)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    print(all_member_data)
    all_member_data.to_csv('AuctionZip.csv',index=True)

except Exception as e:
    print(e)

time.sleep(10)
driver.close()





























    # comp_name = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='auc-directory__table--header--auc--company']//a")]
    # fname = [i.text.split(',')[1] for i in driver.find_elements(By.XPATH,"//*[@class='auc-directory__table--header--auc-name']")]
    # lname = [i.text.split(',')[0] for i in driver.find_elements(By.XPATH,"//*[@class='auc-directory__table--header--auc-name']")]
    # city =  [i.text.split(',')[0] for i in driver.find_elements(By.XPATH,"//*[@class='auc-directory__table--header--auc--city-state']")]
    # state = [i.text.split(',')[1] for i in driver.find_elements(By.XPATH,"//*[@class='auc-directory__table--header--auc--city-state']")]