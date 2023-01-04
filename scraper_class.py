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
# link_to_page - gets link to each page where the details can be found, store these in a list


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
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/button[1]')))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")

        # try and except for the login popup
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/header/div/div/div/div[3]/nav/ul/li[1]/div/div')))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")

    def link_to_page(self):
        '''
        The link_to_page method gets the link to each page where the details can be found.
        It takes no arguments.
        It contains the following actions:
        1. The driver finds the links to each page
        2. The driver waits for 2 seconds
        3. The driver stores the links in a list
        '''
        self.driver.find_elements_by_xpath("//a[@class='product-card__link']")
        time.sleep(2)
        list = self.driver.find_elements_by_xpath("//a[@class='product-card__link']")
        return list

        


# create an instance of the ScrapeWeb class
# 
john_lewis = ScrapeWeb(driver)