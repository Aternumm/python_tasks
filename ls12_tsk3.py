def lsElement(x):
    if len(x) > 0:
        return x[-1]
    return None
x = [0, 1, 3]
print(lsElement(x))
x = []
print(lsElement(x))
x = [2, 3, 4, 5, 1]
print(lsElement(x))
