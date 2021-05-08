def prime_num(*num):
    count = 0
    for x in num:
        for y in range(2, x):
            if x%y==0:
                break
        else:
            count=count+1
    return count
print(prime_num(8,2,3,1,7))
