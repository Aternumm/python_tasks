x = []
i = 0
while i < 5:
    tmp = int(input("Введите число "))
    x.append(tmp)
    i = i + 1
a = []
b = []
i = 0
while i < len(x):
    a.append(x[i] ** 0.5)
    b.append(x[i] ** 2)
    i = i+1
print("Корни чисел ", a, "Квадраты ", b)
