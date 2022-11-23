# Following along with the following tutorial:
# https://www.youtube.com/watch?v=XVv6mJpFOb0
from bs4 import BeautifulSoup
import requests

########################################
# PART 1
# open a file and read the contents of that file
# with open('home.html', 'r') as html_file:
#     content = html_file.read()
    
#     soup = BeautifulSoup(content, 'lxml')
#     # print(soup.prettify())

#     # we want to find the tags that have h5 heading
#     # tags = soup.find('h5') # this only finds the first element of h5
#     courses_html_tags = soup.find_all('h5') # finds all h5 tags
#     for course in courses_html_tags:
#         print(course.text)

#     # write a program that searches for the price of the course 
#     # in the html page
    
#################################
# PART 2
# with open('home_html', 'r') as html_file:
#     content = html_file.read()

#     soup = BeautifulSoup(content, 'lxml')
#     course_cards = soup.find_all('div', class_='card') # note, class_ not class
#     for course in course_cards:
#         course_name = course.h5.text
#         course_price = course.a.text.split()[-1] 

#         print(f"{course_name} costs {course_price}")


########################################################
# PART 3
html_text = requests.get('https://www.udemy.com/courses/search/?src=ukw&q=python')
soup = BeautifulSoup(html_text, 'lxml')
courses = soup.find_all('div', class_="course-card--main-content--2XqiY course-card--has-price-text--1c0ze")
for course in courses:
    course_title = course.h3.text
    print(f"course title: {course_title}")



