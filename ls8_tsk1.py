n = int(input())
i = 2
while i <= n-1:
    if n % i == 0:
        print("Число не простое")
        break
    i = i + 1
else:
    print("Число простое")
