n = int(input())
i = 1
count = 0
while i <= n:
    if n % i == 0:
        count = count +1
        print(i)
    i = i + 1
print("Количество",count)
    
