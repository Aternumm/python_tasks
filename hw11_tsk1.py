word = input()
m = 0
b = 0
for i in word:
        if 'a' <= i <= 'z':
                m += 1       
        elif 'A' <= i <= 'Z':
                b += 1
        else:
                pass                   
print(m)
print(b)
