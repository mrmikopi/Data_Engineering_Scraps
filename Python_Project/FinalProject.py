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
tables = soup.find_all('table')

# TODO: Table'lar arasindan bizim attribute'a sahip olani bul.
# tables'in obje tipini begenmedim, resultSet filan sanirim,
# islem yapilmiyor adam akilli.

#Calismadi:
soup.findAll(attrs={'class':'wikitable sortable mw-collapsible jquery-tablesorter mw-made-collapsible'})

