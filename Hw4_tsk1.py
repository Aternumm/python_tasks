x = int(input("введите год"))
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print("в этом году 366 дней")
else:
    print("В ЭТОМ ГОДУ 365 ДНЕЙ")