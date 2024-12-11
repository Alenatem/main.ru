from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

driver.get('https://www.saucedemo.com/')
driver.maximize_window()

sleep(10)