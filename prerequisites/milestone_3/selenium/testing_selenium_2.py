from selenium import webdriver 
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.find_element(by=By.XPATH, value='//button')