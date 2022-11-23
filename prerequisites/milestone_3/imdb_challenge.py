# IMDB Challenge
# This link shows the IMDB page of the movie Pulp Fiction: https://www.imdb.com/title/tt0110912/?ref_=nv_sr_srsg_0 
# Get a list of all the actors/actresses in the movie
# Store the data in a dictionary along with the link to the actor's/actress' IMDB page
# Visit each actor's IMDB page and scrape the data corresponding to the movies in which the actor/actress has played
# The dictionary should have the following structure: 5a. {name: [], link: [], movies: [{title: [], year: []}]}

import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.imdb.com/title/tt0110912/?ref_=nv_sr_srsg_0")
html = response.content
html = BeautifulSoup(html, "html.parser")
# print(html.prettify)
# print(html.title)
# print(html.title.name)
# print(html.title.parent.name)
# print(html.title.string)
for link in html.find_all('a'):
    print(link.get('href'))

# Get a list of all the actors/actresses in the movie
# Store the data in a dictionary along with the link to the actor's/actress' IMDB page
# Visit each actor's IMDB page and scrape the data corresponding to the movies in which the actor/actress has played
# The dictionary should have the following structure: 5a. {name: [], link: [], movies: [{title: [], year: []}]}

# list_of_actors = html.find_all("title-cast-item")[2:]
# print(list_of_actors)
# for actor in list_of_actors:
#     print(actor.prettify())
