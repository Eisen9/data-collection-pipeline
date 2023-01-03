import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

# Using Selenium, create a ScrapeWeb class that scrapes the following website:
# https://www.johnlewis.com/


# The ScrapeWeb class should contain the following methods:
# scroll - this method should scroll to the bottom of the page
# click_next_button - this method should click the next button


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


# create an instance of the ScrapeWeb class
john_lewis = ScrapeWeb(driver)