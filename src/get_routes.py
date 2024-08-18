import requests
from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd

url = 'https://www.transportboard.com/route-finder/'
r = requests.get(url)


p = Path('./routes.html')
if not p.exists():
    p.write_text(r.text)

soup = BeautifulSoup(r.content, 'html5lib')

bus_routes = []

routes = soup.find('ul', attrs = {'id':'bus-route-list'}) 

for row in routes.find_all('li', attrs={'class':'clearfix'}):
    br = {}
    # print(row.button.find_all('span')[0].text)
    br['id'] = row.button['data-busid']
    br['bus-number'] = row.button.find_all('span')[4].text
    br['name'] = row.button.find_all('span')[0].text
    br['from'] = row.button.find_all('span')[1].span.text.replace('From', "", 1)
    br['to'] = row.button.find_all('span')[3].text.replace('to', "", 1)
    bus_routes.append(br)

file = pd.DataFrame.from_dict(bus_routes)
file.to_csv('./routes.csv')
