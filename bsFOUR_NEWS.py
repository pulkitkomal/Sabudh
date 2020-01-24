from bs4 import BeautifulSoup
import requests

desc_LIST = []
Date_LIST = []
Headlines_LIST = []
id = []
id_var = 1
testlst = []


def listToString(s):
    str1 = " "
    return (str1.join(s))


for x in range(2,10):

    gktoday = requests.get('https://currentaffairs.gktoday.in/page/{}'.format(x))
    soup = BeautifulSoup(gktoday.text, "html.parser")

# print(soup.prettify())
    h1 = soup.find_all('h1')
    p = soup.find_all('p')
    date = soup.find_all('span', class_="meta_date")
    for date in date:
        Date_LIST.append(date.text)
        # print(date.text)
    # print(len(p))
    # print(len(h1))

    for h1 in h1:
        id.append(id_var)
        h1text = str(h1.text)
        Headlines_LIST.append(h1text.replace(';'," "))
        # print(h1.text)
        id_var = id_var + 1


    for p in p:
        txt = p.text
        # print(p.text)
        testlst.append(txt)
        # print(testlst)
        if p.text[-3:] == 'App':
            lst = listToString(testlst)
            desc_LIST.append(lst)
            testlst = []
            continue



# print(len(desc_LIST))
for x in range(0,len(Headlines_LIST)):
    print(id[x])
    print(Date_LIST[x])
    print(Headlines_LIST[x])
    print(desc_LIST[x])

import pandas as pd
dataset = list(zip(id, Date_LIST, Headlines_LIST,desc_LIST))
df = pd.DataFrame(data=dataset, columns=["ID", "DATE", "HEADLINES","DESC"])
df.to_csv("tempDATA.csv", index=False, header=True)
