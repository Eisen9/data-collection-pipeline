'''
In this file, you find a different method for bypassing cookies.
'''

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
driver = webdriver.Chrome()

# Using Selenium, create a ScrapeWeb class that scrapes the following website:
# https://www.johnlewis.com/


# The ScrapeWeb class should contain the following methods:
# scroll - this method should scroll to the bottom of the page
# click_next_button - this method should click the next button
# bypass_cookies_and_login - this method should bypass the cookies and login popups. Create
# an exception if the website does not require the user to accept cookies or login.


class ScrapeWeb:
    '''
    The ScrapeWeb class defines the methods used to scrape the John Lewis website.
    It contains the following methods:
    scroll - this method scrolls to the bottom of the page
    click_next_button - this method clicks the next button
    '''
    def __init__(self, driver):
        '''
        The __init__ method initialises the ScrapeWeb class.
        It takes the following arguments:
        driver - the Selenium driver

        It contains the following attributes:
        driver - the Selenium driver
        url - the url of the website to be scraped
    
        It contains the following actions:
        1. The driver is assigned to the driver attribute
        2. The url is assigned to the url attribute
        3. The driver navigates to the url
        4. The driver waits for 10 seconds
        5. The driver maximises the window
        6. The driver scrolls to the bottom of the page
        '''
        self.driver = driver
        self.url = "https://www.johnlewis.com/"
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    def scroll(self):
        '''
        The scroll method scrolls to the bottom of the page.
        It takes no arguments.
        It contains the following actions:
        1. The driver scrolls to the bottom of the page
        2. The driver waits for 2 seconds
        '''
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        
    def click_next_button(self):
        '''
        The next_button method clicks the next button.
        It takes no arguments.
        It contains the following actions:
        1. The driver clicks the next button
        2. The driver waits for 2 seconds
        '''
        self.driver.find_element_by_class_name("next").click()
        time.sleep(2)

    def bypass_cookies_and_login(self):
        '''
        The bypass_cookies_and_login method bypasses the cookies and login popups.
        It takes no arguments.
        It contains the following actions:
        1. The driver waits for the cookies popup to appear
        2. The driver clicks the accept cookies button
        3. The driver waits for the login popup to appear
        4. The driver clicks the login button
        5. The driver waits for the login popup to disappear
        '''
        driver = self.driver 
        URL = self.url
        driver.get(URL)
        delay = 10
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cookie-script-tags"]')))
            print("Frame Ready!")
            driver.switch_to.frame('cookie-script-tags') # switch to the iframe with the cookie popup
            accept_cookies_button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="save"]'))) 
            print("Accept Cookies Button Ready!")
            accept_cookies_button.click()
            time.sleep(1) 
        except TimeoutException:
            print("Loading took too much time!")
        return driver         

            
        


# create an instance of the ScrapeWeb class
# 
john_lewis = ScrapeWeb(driver)