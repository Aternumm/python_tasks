a = int(input("введите 1 сторону"))
b = int(input("введите 2 сторону"))
c = int(input("введите 1 сторону"))
if a+b > c and  a+c>b and b+c>a:
    print("существует")
else:
    print("не существует")
