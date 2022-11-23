# follow through: https://www.youtube.com/watch?v=Xjv1sY630Uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.keys import By
import time
PATH = "usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH) 

driver.get("https://techwithtim.net")

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)
print(driver.page_source)

time.sleep(10)
driver.close()