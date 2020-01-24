from bs4 import BeautifulSoup
import requests

xkcd = requests.get('https://xkcd.com')
soup = BeautifulSoup(xkcd.text, "html.parser")
list = []
a = soup.find_all('a', href=True)
img = soup.find_all('img')

for a in img:
    img = str(a['src'])
    img1 = 'https://'+img[2:]
    list.append(img1)

import os
import shutil
import urllib.request

del list[0]
print(list)
varr = 1

print('Downloading started!')
try:
    shutil.rmtree('./ImageCACHE/')
except:
    pass
os.makedirs('./ImageCACHE/')
for x in list:
    x = str(x)
    urllib.request.urlretrieve(x, './ImageCACHE/{}.{}'.format(varr,x[-3:]))
    varr = varr + 1

