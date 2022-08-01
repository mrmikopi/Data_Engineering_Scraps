from operator import attrgetter
from bs4 import BeautifulSoup as bs
import html5lib
import requests
import pandas as pd

# Veri cekilecek sayfa:
# https://en.wikipedia.org/wiki/List_of_largest_banks

htmlUrl = 'https://en.wikipedia.org/wiki/List_of_largest_banks'

r = requests.get(htmlUrl)
print(r.status_code)

soup = bs(r.text, 'html5lib')
headers = soup.find_all('th')

for header in headers:
    if 'Market cap' in header.contents:
        marketHeader = header

rows = marketHeader.parent.parent.find_all('tr')
rows = rows[1:]

# DataFrame olustur
cols=['Country','Bank Name','Market Cap']
df = pd.DataFrame(columns=cols)

# Rowlari dolas
for row in rows:
    span = row.find(name='span',attrs={'class':'flagicon'})
    # country
    country = span.find('img').get('alt')
    # bank name
    for sibling in span.next_siblings:
        if sibling.name == 'a':
            name = sibling.get_text()
    # capital has \n character next to it
    capital = span.find_next('td').get_text().split()
    # capital has Reference link
    capital = capital[0].split('[')
    capital = capital[0]

    # Add to Dataframe. append method is deprecated. 
    df.loc[df.shape[0]] = [country,name,capital]
    # df = df.append(pd.Series([country,name,capital],index=cols),ignore_index=True)

# DataFrame'i yazdir
df.to_json('Largest_Banks.json',orient='records')
# with open('Largest_Banks.json','w') as jsonFile:
#     jsonFile.write()