import random
x = []

for i in range(4):
    x.append(random.randint(0, 10))
y = x[:]
for i in x:
    y.append(i*i)
print(y, x)
    
