s = input()
s = s.split()
s_ = ''
for i in s:
    s_ += i
print(s_)
 
l = len(s_)
i = 0
f = 1
while i < l//2:
    if s_[i] != s_[-1-i]:
        print('Не палиндром')
        f = 0
        break
    i += 1
if f == 1:
    print('Палиндром')


s = input()
tmp = s[::-1]
if s == tmp:
    print('Палиндром')
else:
    print('Не палиндром')
