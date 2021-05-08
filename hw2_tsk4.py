a = int(input("введите а "))
b = int(input("введите b "))
c = int(input("введите c "))
D = b ** 2 - 4 * a * c
if D > 0:
    d = D ** 0.5
    x = (-b+d)/(2*a)
    X = (-b-d)/(2*a)
    print("Х равен ",X,x)
else:
    if D == 0:
        d = D ** 0.5
        x = (-b + d) / (2 * a)
        print("Х равен ",x)
    else:
        print("Error")

        
