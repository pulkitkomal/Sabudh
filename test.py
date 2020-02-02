import re
line ="ab sh (ਰਸਾ)ਸੌਡੇਦਾਕਲੋਰਾਈਡ,ਲ੍ਣ‌"
a = ['a']
b = []

for x in a:
    z = a.index(x)
    # print(x)
    # print(z)
    # if re.match('^[a-zA-Z]+', line) is not None:
    #     re.

z = re.findall('^[a-zA-Z\s]+', line)
print(z)
# print(a)