# episode_id
# episode_title
# episode_url
# platform
# publish_date


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
driver.get('https://podcasts.apple.com/us/podcast/the-spin-sucks-podcast-with-gini-dietrich/id1356305060')
driver.maximize_window()
see_all_button = driver.find_element(By.XPATH,"//a[normalize-space()='See All (378)']").click()
time.sleep(5)


def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless=new")
    driver = webdriver.Chrome(options=ops)
    return driver 
driver1 = headless_chrome()

try:
    all_member_data  = pd.DataFrame()

    al_links = [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@class='link-action svelte-1c9ml6j']")]
    print(len(al_links))
    for i in al_links:
        driver.switch_to.new_window('tab')
        driver.get(i)


        try:
            platform = ['Apple Podcast']

            publish_date = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='metadata svelte-16t2ez2']/li[1]")]
            if len(publish_date) < len(platform):
                diff = len(platform)-len()
                publish_date.extend([""] * diff)

        
            episode_id = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='information svelte-sy8mrl']//li[5]//div[2]")]
            if len(episode_id) < len(platform):
                diff = len(platform)-len(episode_id)
                episode_id.extend([""] * diff)
            
            episode_len = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='information svelte-sy8mrl']//li[4]//div[2]")]
            if len(episode_len) < len(platform):
                diff = len(platform)-len(episode_len)
                episode_len.extend([""] * diff)
            
            episode_title = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='headings__title svelte-1uuona0']/span")]
            if len(episode_title) < len(platform):
                diff = len(platform)-len(episode_title)
                episode_title.extend([""] * diff)


            episode_link = [driver.current_url]
            if len(episode_link) < len(platform):
                diff = len(platform)-len(episode_link)
                episode_link.extend([""] * diff)
        

        except Exception :
            None


        d = {

            'Episode_title':episode_title,
            'Platform': platform,
            'Episode_id':episode_id,
            'Episode_url':episode_link,
            'Publish_date':publish_date,
            'Episode_Length':episode_len

            }
        

        
        df = pd.DataFrame(d)
        all_member_data  = pd.concat([df,all_member_data])
        all_member_data.index = np.arange(1,len(all_member_data)+1)
        time.sleep(1)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    print(all_member_data)
    all_member_data.to_csv('podcast.csv',index=True)

except Exception as e:
    print(e)

time.sleep(10)
driver.close()

