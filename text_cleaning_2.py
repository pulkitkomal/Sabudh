import re
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer


meaning = {'a.': 'adjective', 'aa.': 'all_adjective', 'n.': 'noun', 'nn.': 'all_nouns'}


def listToString(s):
    str1 = ""
    return (str1.join(s))


def english(string):
    split_eng = re.split("[^a-zA-Z?.,()-]*", string)
    # print(split_eng)

    string_out = listToString(split_eng)
    return string_out


def punjabi(string):
    string_input = list(string)
    split_eng = re.split("[^a-zA-Z?.,()-]*", string)
    string_pun = list(split_eng)

    for x in string:
        for y in string_pun:
            if x == y:
                try:
                    string_input.remove(x)
                except:
                    pass
    out_pun = listToString(string_input).lstrip().rstrip()

    return out_pun



list_string = []

with open('./t1.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        y = line.split()
        list_string.append(word_tokenize(line))


# print(list_string)
lst_eng = []
lst_pun = []
dict = {}
tst = ''
for x in range(0, len(list_string)):
    lst1 = []
    lst = []
    pun_list = []
    for y in range(0, len(list_string[x])):
        z = list_string[x][y]
        if re.match('^[a-zA-Z.]+', english(z)) is not None:
            lst.append(z)
            lst_eng.append(lst)

        elif re.match('^[a-zA-Z.]+', english(z)) is None:
            ky = TreebankWordDetokenizer().detokenize(lst)
            tmp = punjabi(z)
            if tmp == '':
                continue
            pun_list.append(tmp)
            dict[ky] = pun_list






# for x in lst_eng:
#     print(x)
#
# for x in lst_pun:
#     print(x)
[print('Key:', key,  '\nValue: ', value) for key, value in dict.items()]



