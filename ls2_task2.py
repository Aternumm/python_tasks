x = int(input("введите день месяца"))
d = x%7
if 1<= d <=5:
    print("рабочий день")
else:
    print("выходной")
