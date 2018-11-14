from bs4 import BeautifulSoup
import requests
from source import *
for problem in source:
    page = requests.get(problem)
    soup = BeautifulSoup(page.content, 'html.parser')
    link = 'http://ntucoder.net' + soup.findAll("div", {"class": "submission-title"})[0].find_all('a')[1]['href']
    name = link
    name = name.split('/')[-1]
    code = soup.find_all('textarea')[0].contents[0]
    code = code.replace("\n", "")
    print(name)
    file = open('sourcecodes/' + name + '.txt', 'w', encoding="utf-8");
    file.write(link + '\n\n')
    file.write(code)
    file.close()
