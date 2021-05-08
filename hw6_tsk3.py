import random
x = [0, 1, 2, 3, 4, 5, 6, 7]
x[0] = random.randint(0 , 7)
x[1] = random.randint(0 , 7)
x[2] = random.randint(0 , 7)
x[3] = random.randint(0 , 7)
x[4] = random.randint(0 , 7)
x[5] = random.randint(0 , 7)
x[6] = random.randint(0 , 7)
x[7] = random.randint(0 , 7)
x[8] = random.randint(0 , 7)
y = [x[0]*2,x[1]*2, x[2]*2, x[3]*2, x[4]*2, x[5]*2, x[6]*2, x[7]*2, x[8]*2]
print("Список случайных чисел: ", x, "Умноженный на 2: ", y)
