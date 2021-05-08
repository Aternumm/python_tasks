num = [3.5, 5, 2, -5]

def getsum(num):
    i = 0
    for item in num:
        i = i + item
    return i
    
numSum = getsum(num)
print(numSum)
