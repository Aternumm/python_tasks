   x = int(input("введите число "))
a = x % 10
b = (x // 10) % 10
c = ((x // 10) // 10) % 10
d = ((x // 10 ) // 10)//10%10
D = str(a) + str(b) + str(c) + str(d)
print(D) 
