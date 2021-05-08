def func(n, a):
    if n==0:
        return 1
    return a*func(n-1, a)
a = int(input())
n = int(input())
print(func(n, a))
