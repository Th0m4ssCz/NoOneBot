import requests
from bs4 import BeautifulSoup

url='https://www.coingecko.com/'

r =requests.get(url)

soup=BeautifulSoup(r.text,'html.parser')

crypto_table=soup.find('table',class_='sort table mb-0 text-sm text-lg-normal table-scrollable')

for crypto in crypto_table.find_all('tbody'):
    rows= crypto.find_all('tr')
    for row in rows:
        name_crypto=row.find('span',class_='lg:tw-flex font-bold tw-items-center tw-justify-between').text.strip()
        price_crypto=row.find('span',class_='no-wrap').text.strip()
        print("Name: "+name_crypto+"    Price: "+price_crypto)
