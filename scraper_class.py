# This class will contain all methods used to scrape data from your chosen website.

# Once you have created your methods to navigate the website and get the required data, you should be able to initialise an instance of this class and use it to scrape the website selected.

# Remember: you are using John Lewis as an example here, but you should be able to use this class to scrape any website you choose.
class Scraper:
    def __init__(self, driver):
        self.driver = driver

    def get_data(self): # TODO: note sure about this 
        # This method should return a list of dictionaries. Each dictionary should contain the data you want to scrape from the website.
        # The keys of the dictionary should be the column names of the table you are creating in the database.
        # The values of the dictionary should be the data you are scraping from the website.
        # The list of dictionaries should contain one dictionary for each row of data you want to store in the database.
        # You can use the following code to test your method:
        # data = self.get_data()
        # for row in data:
        #     print(row)
        #     print()
        return []
    def get_url(self):
        # This method should return the url of the website you want to scrape.
        return ""
    def get_name(self):
        # This method should return the name of the website you want to scrape.
        return ""
    def get_description(self):
        # This method should return a description of the website you want to scrape.
        return ""
    def get_website(self):
        # This method should return the url of the website you want to scrape.
        return ""
    def get_logo(self):
        # This method should return the url of the logo of the website you want to scrape.
        return ""
    def get_tags(self):
        # This method should return a list of tags that describe the website you want to scrape.
        return []
    def get_item_url(self, item):
        # This method should return the url of the item you want to scrape.
        return ""
    def get_item_name(self, item):
        # This method should return the name of the item you want to scrape.
        return ""
    def get_item_description(self, item):
        # This method should return a description of the item you want to scrape.
        return ""
    def get_item_image(self, item):
        # This method should return the url of the image of the item you want to scrape.
        return ""
    def get_item_tags(self, item):
        # This method should return a list of tags that describe the item you want to scrape.
        return []
    

