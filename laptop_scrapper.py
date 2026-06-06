from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import pandas as pd

pac=ChromeDriverManager().install()
man=Service(pac)


chrome_options = Options()
chrome_options.add_argument("--headless")



driver=webdriver.Chrome(service=man,options=chrome_options)

driver.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")

wait=WebDriverWait(driver,10)
all_laptops=[]



wait.until(EC.presence_of_element_located((By.CLASS_NAME,"caption")))

laps=driver.find_elements(By.CLASS_NAME,"caption")

for lap in laps:
    nam=lap.find_element(By.CSS_SELECTOR,"div.caption h4 a")
    n=nam.get_attribute("title")
    pric=lap.find_element(By.CSS_SELECTOR,"div.caption h4 span").text
    all_laptops.append({"NAME":n,"PRICE":pric})
    

df=pd.DataFrame(all_laptops)
df.to_csv("laptop_scrapper.csv",index=False)
    
