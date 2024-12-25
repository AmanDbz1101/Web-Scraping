import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#import module to use keys 
from selenium.webdriver.common.keys import Keys
import time

Service = Service('d:\Python\Web scrapping\Selenium\chromedriver.exe')

driver = Chrome(service=Service)
driver.get('https://www.google.com')

input_element = driver.find_element(By.CLASS_NAME, 'gLFyf')
input_element.send_keys('Python'+Keys.ENTER)


time.sleep(10)
driver.quit()
