# Libraries
import requests
from bs4 import BeautifulSoup
import csv
import time

url = "https://news.ycombinator.com/newest"
def get_response(url):
    response = requests.get(url)
    return response

 # Extract data fields
titles = []
scores = []
timess = []
comms = []
links = []
def request_Data(content):
    for title in content.findAll('span', {'class': 'titleline'}):
        titles.append(title.text)
    for score in content.findAll('span', {'class': 'score'}):
        scores.append(score.text)
    for times in content.findAll('span', {'class': 'age'}):
        timess.append(times.text)
    for comm in content.findAll('span', {'class': 'subline'}):
        comms.append(comm.findChildren("a",recursive=True)[4].text)
    for link in content.findAll('span', {'class': 'titleline'}):
        result = link.find("a").get("href")
        link = "https://news.ycombinator.com/"
        if result.startswith('item'):
            result = link + result
        links.append(result)

print('HTTP GET: %s | Status code: %s' % (get_response(url).url, get_response(url).status_code))
content = BeautifulSoup(get_response(url).text, 'lxml')

request_Data(content)

print(titles[1])
print(scores[1])
print(timess[1])
print(comms[1])
print(links[1])
