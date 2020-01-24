from bs4 import BeautifulSoup
import requests

xkcd = requests.get('https://xkcd.com')
soup = BeautifulSoup(xkcd.text, "html.parser")

a = soup.find_all('a', href=True)
img = soup.find_all('img')

for a in img:
    print(a)