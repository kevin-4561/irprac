import requests
from bs4 import BeautifulSoup

url="https://www.facebook.com"
html=requests.get(url).text
soup=BeautifulSoup(html, 'html.parser')

[print(a['href'])for a in soup.find_all('a', href=True)]

[print(img['src'])for img in soup.find_all('img', src=True)]

[print(f"{m['name']}:{m['content']}")for m in soup.find_all('meta',attrs={'name':True, 'content':True})]
