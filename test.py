import re
line ="(ਰਸਾ)ਸੌਡੇਦਾਕਲੋਰਾਈਡ,ਲ੍ਣ‌"
a = ['a']
b = []

for x in a:
    z = a.index(x)
    print(x)
    print(z)
    if re.match('^[a-zA-Z]+', line) is not None:
        print('{} {}'.format(x,line))

print(a)