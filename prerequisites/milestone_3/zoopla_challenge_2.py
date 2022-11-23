import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=25&pn=1&view_type=list")
html_page = response.content
html_page = BeautifulSoup(html_page, 'html.parser')
# print(html_page.prettify())

house_cards = html_page.find_all('div', class_="PJLV")
for house in house_cards:
    # return the name of the house and the price
    house_price = house.p
    print(f"House price: {house_price}")
