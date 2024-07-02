from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

url = 'https://stepik.org/catalog'

soup = BeautifulSoup(requests.get(url).text, "lxml")
urls = soup.find_all('a', href=True)
domen = set()
for url in urls:
    link = urlparse(url.get("href")).hostname
    if link:
        domen.add(link)


print(*sorted(domen), sep='\n')
