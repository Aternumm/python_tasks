x = int(input("x = "))
y = int(input("Y ="))
d = (x*x + y*y) * 0.5
R = 4
if d > R:
    print("за пределами окружности")
elif d == R:
    print("на окружности")
else:
    print("в окружности")
