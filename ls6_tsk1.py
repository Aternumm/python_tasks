x = []
i = 0
while i < 5:
    tmp = int(input("Введите число "))
    x.append(tmp)
    i = i + 1
print("Среднее арифметическое чисел: ", sum(x)/len(x))
