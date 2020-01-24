from bs4 import BeautifulSoup
import requests


gktoday = requests.get('https://www.ndtv.com/top-stories?pfrom=home-topstories')
soup = BeautifulSoup(gktoday.text, "html.parser")

# print(soup.prettify())

a = soup.find_all('a')
print(a)
for a in a:
    print(a.text)