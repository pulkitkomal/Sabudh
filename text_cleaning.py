import re

meaning = {'a.': 'adjective', 'aa.': 'all_adjective', 'n.': 'noun', 'nn.': 'all_nouns'}


def listToString(s):
    str1 = ""
    return (str1.join(s))


def english(string):
    split_eng = re.split("[^a-zA-Z?.-]*", string)
    string_out = listToString(split_eng)
    return string_out


def punjabi(string):
    string_input = list(string)
    split_eng = re.split("[^a-zA-Z?.-]*", string)
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

def create_dict(list_string):
    dict = {}
    tst = ''
    for x in list_string:
        if re.match('^[a-zA-Z]+', english(x)) is not None:
            pun_list = []
            pun_list.append(punjabi(x))
            dict[english(x)] = pun_list
            tst = english(x)
        elif re.match('^[a-zA-Z]+', x) is None:
            dict[tst].append(punjabi(x))
    return dict


list_string = []

with open('./t1.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        list_string.append(line)
        # print(listToString(y))

# print(create_dict(list_string))
dict = create_dict(list_string)

[print('Key:', key,  '\nValue: ', value) for key, value in dict.items()]
print(len(list(dict.keys())))
