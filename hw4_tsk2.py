x = int(input("Введите Х "))
y = int(input("Введите У"))
if x >= 0 and y >= 0:
    print("В 1 четверти")
elif x >= 0 and y <= 0:
    print("В 4 четверти")
elif x <= 0 and y <= 0:
    print("в 3 четверти")
else:
    print("Во 2 четверти")
