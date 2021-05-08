import string
x = input().lower()
x = x[:-1]
for item in string.digits:
    while item in x:
        x = x.replase(item, '')
d = {'a', 'e', 'o', 'u', 'i'}
count = 0
for item in d:
    count += x.count(item)
if (len(x) - count) < count:
    print('Гласных больше')
elif (len(x)- count) > count:
    print('Согласных больше')
else: print('Поровну')
