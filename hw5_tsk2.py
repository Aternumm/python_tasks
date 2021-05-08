x = int(input("Введите Х"))
y = int(input("Введите Y"))
if (x*x+y*y)**0.5 == 4:
    print("на окружности")
elif (x*x+y*y)**0.5 < 4:
    print("внутри окружности")
else:
    print ("снаружи окружности")
