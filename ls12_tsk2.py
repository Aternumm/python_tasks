def triangle_square(a, b, c):
    p = (a+b+c)/2
    S = (p*(p-a)*(p-b)*(p-c))**0.5
    return S
def is_triangle(a, b, c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False
a = int(input())
b = int(input())
c = int(input())
if is_triangle(a, b, c):
    res = triangle_square(a, b, c)
    print(res)
else:
    print("Не треугольник")
