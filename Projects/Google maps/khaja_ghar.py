from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import json 
import re 

chrome_options = webdriver.ChromeOptions()

service = Service('d:\Python\Web scrapping\Selenium\chromedriver.exe')

driver = webdriver.Chrome(service=service, options=chrome_options)

keyword = "newari+khaja+ghar"
driver.get(f'https://www.google.com/maps/search/{keyword}/')

# try:
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR))


# scrolling the screen

# scrollable_div = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"]')
# driver.execute("""
#     var scrollable_div = arguments[0];
#     fucntion scrollW

# """)

items = driver.find_elements(By.CSS_SELECTOR, 'div[role-"feed"]>div>div[jsaction]')
results = []
for item in items:
    data = {}
# time.sleep(10)
# driver.quit()

