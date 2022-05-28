import requests
from bs4 import BeautifulSoup

url = 'https://darksouls.fandom.com/es/wiki/Wiki_Dark_Souls'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

ds = soup.find_all('tr')
print(ds)
archivo = open('Darksouls.txt','w')
archivo.write(str(ds))
archivo.close()
