from nltk.tokenize import word_tokenize
list_string = []

with open('./t1.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        list_string.append(line)

def is_ascii(string):
    return all(ord(c) < 128 for c in string)

lst = []
lst_eng = []
lst_pun = []
for x in list_string:
    lst.append(word_tokenize(x))

for lst in lst:
    tempPun = []
    tempEng = []
    for string in lst:
        if is_ascii(string):
            tempEng.append(string)
        elif not is_ascii(string):
            tempPun.append(string)
    lst_eng.append(" ".join(tempEng))
    lst_pun.append(" ".join(tempPun))

print(lst_eng)
print(lst_pun)
