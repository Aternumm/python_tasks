x = []
i = 0
while i < 5:
    tmp = input("Введите фамилию ")
    x.append(tmp)
    i = i + 1
lt = input("Введите  букву ")
i = 0
while i < len(x):
    if x[i].startswith(lt):
        print(x[i])
    i = i+1
