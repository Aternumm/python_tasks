def rec(n):
    print(n)
    if n == 0:
        return
    return rec(n - 1)
n = int(input())
print(rec(n))
