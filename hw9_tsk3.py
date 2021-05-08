import random
x = []

for i in range(12):
    x.append(random.randint(7500, 15000))

y = sum(x)/len(x)
print("Зарплата ежемесячно: ", x, "Средняя зарплата: ", y)
