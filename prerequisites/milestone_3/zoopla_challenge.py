import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=25&pn=1&view_type=list")
html = response.content
html = BeautifulSoup(html, "html.parser")
# print(html.prettify())

# scrape data from all the properties on the first page
# store the data in a dictionary
properties = html.find_all("div", {"class": "css-7sotp1 e1f3kzbr14"}) # 25 properties on the first page of Zoopla
for item in properties:
    print(item.prettify())
    print(" ")
    data_in_dict = {
        "title": item.find("a", {"class": "css-1j9wv1e e1f3kzbr13"}),
        "price": item.find("div", {"class": "css-1j9wv1e e1f3kzbr13"}),
        "address": item.find("div", {"class": "css-1j9wv1e e1f3kzbr13"}),
        "bedrooms": item.find("div", {"class": "css-1j9wv1e e1f3kzbr13"}),
        "bathrooms": item.find("div", {"class": "css-1j9wv1e e1f3kzbr13"}),
        "reception": item.find("div", {"class": "css-1j9wv1e e1f3kzbr13"}),
        "parking": item.find("div", {"class": "css-1j9wv1e e1f3kzbr13"}),
        "status": item.find("div", {"class": "css-1j9wv1e e1f3kzbr13"}),
        "link": item.find("a", {"class": "css-1j9wv1e e1f3kzbr13"})}
    print(data_in_dict)
    print(" ")


# print(properties)