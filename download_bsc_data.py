#IMPORT PACKAGES
import numpy as np
import pandas as pd 
import urllib.request
from html_table_parser.parser import HTMLTableParser
import urllib3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from webdriver_manager.chrome import ChromeDriverManager

#SCRAPE TABLES FROM THE BIG SKY CONFERENCE
  #generative ai was used to help trouble shout this code 
link = 'https://www.bigskyconf.com/stats.aspx?path=wsoc&year=2023'
webdriver_path = '/.wdm/drivers/chromedriver/mac64/127.0.6533.88/chromedriver-mac-x64/chromedriver'
driver = webdriver.Chrome(service=webdriver.ChromeService(webdriver_path))  
wait = WebDriverWait(driver, 30) # wait 30 seconds
driver.get(link)

try:
    # Wait for a specific element to indicate page load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'sidearm-table-overflow')))
    
    # Or, wait for a partial URL match
    # wait.until(EC.url_contains("stats.aspx?path=wsoc"))

    page_source = driver.page_source
    df = pd.read_html(page_source)
    print(df)

except TimeoutException:
    print(f"Timeout waiting for URL to change or page to load")
    print(f"Current URL: {driver.current_url}") 

#CREATING TABLES
table_objects = {} 

for i in range(len(df)):  
    table_name = f"table_{i+1}" 
    table_objects[table_name] = df[i].copy() 

#MINOR FORMATING AND EXPORTING
  #tables 1 - 10 are team tables 
table_1 = table_objects['table_1']
table_1.set_index('Team', inplace=True) 
table_1.to_csv('bsc_table_1.csv') 

table_2 = table_objects['table_2']
table_2.set_index('Team', inplace=True) 
table_2.to_csv('bsc_table_2.csv')

table_3 = table_objects['table_3']
table_3.set_index('Team', inplace = True)
table_3.to_csv('bsc_table_3.csv')

table_4 = table_objects['table_4']
table_4.set_index('Team', inplace = True)
table_4.to_csv('bsc_table_4.csv')

table_5 = table_objects['table_5']
table_5.set_index('Team', inplace = True)
table_5.to_csv('bsc_table_5.csv')

table_6 = table_objects['table_6']
table_6.set_index('Team', inplace = True)
table_6.to_csv('bsc_table_6.csv')

table_7 = table_objects['table_7']
table_7.set_index('Team', inplace = True)
table_7.to_csv('bsc_table_7.csv')

table_8 = table_objects['table_8']
table_8.set_index('Team', inplace = True)
table_8.to_csv('bsc_table_8.csv')

table_9 = table_objects['table_9']
table_9.set_index('Team', inplace = True)
table_9.to_csv('bsc_table_9.csv')

table_10 = table_objects['table_10']
table_10.set_index('Team', inplace = True)
table_10.to_csv('bsc_table_10.csv')

#tables 11 - 20 are player tables
table_11 = table_objects['table_11']
table_11.to_csv('bsc_table_11.csv')

table_12 = table_objects['table_12']
table_12.to_csv('bsc_table_12.csv')

table_13 = table_objects['table_13']
table_13.to_csv('bsc_table_13.csv')

table_14 = table_objects['table_14']
table_14.to_csv('bsc_table_14.csv')

table_15 = table_objects['table_15']
table_15.to_csv('bsc_table_15.csv')

table_16 = table_objects['table_16']
table_16.to_csv('bsc_table_16.csv')

table_17 = table_objects['table_17']
table_17.to_csv('bsc_table_17.csv')

table_18 = table_objects['table_18']
table_18.to_csv('bsc_table_18.csv')

table_19 = table_objects['table_19']
table_19.to_csv('bsc_table_19.csv')

table_20 = table_objects['table_20']
table_20.to_csv('bsc_table_20.csv')

#tables 21 - 35 are result and location tables 
table_21 = table_objects['table_21']
table_21.to_csv('bsc_table_21.csv')

table_22 = table_objects['table_22']
table_22.to_csv('bsc_table_22.csv')

table_23 = table_objects['table_23']
table_23.to_csv('bsc_table_23.csv')

table_24 = table_objects['table_24']
table_24.to_csv('bsc_table_24.csv')

table_25 = table_objects['table_25']
table_25.to_csv('bsc_table_25.csv')

table_26 = table_objects['table_26']
table_26.to_csv('bsc_table_26.csv')

table_27 = table_objects['table_27']
table_27.to_csv('bsc_table_27.csv')

table_28 = table_objects['table_28']
table_28.to_csv('bsc_table_28.csv')

table_29 = table_objects['table_29']
table_29.to_csv('bsc_table_29.csv')

table_30 = table_objects['table_30']
table_30.to_csv('bsc_table_30.csv')

table_31 = table_objects['table_31']
table_31.to_csv('bsc_table_31.csv')

table_32 = table_objects['table_32']
table_32.to_csv('bsc_table_32.csv')

table_33 = table_objects['table_33']
table_33.to_csv('bsc_table_33.csv')

table_34 = table_objects['table_34']
table_34.to_csv('bsc_table_34.csv')

table_35 = table_objects['table_35']
table_35.to_csv('bsc_table_35.csv')
