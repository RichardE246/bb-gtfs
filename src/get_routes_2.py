import requests
from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd

# url = 'https://nimbus.wialon.com/locator/7e1577e50406418aa22aaa89cb5ea76a/'
url = 'https://nimbus.wialon.com/locator/7e1577e50406418aa22aaa89cb5ea76a/route/54147'
r = requests.get(url)


p = Path('routes_2.html')
if not p.exists():
    p.write_text(r.text)

# soup = BeautifulSoup(r.content, 'html5lib')

# bus_routes = []

# routes = soup.find('div', id ='routes-list') 

# print(routes)