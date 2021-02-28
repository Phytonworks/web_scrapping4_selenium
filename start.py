import selenium as selenium
from selenium import webdriver
import os

driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver.exe'))
driver.get('https://www.detik.com/')
